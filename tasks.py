# -*- coding: utf-8 -*-

import os
import shutil
import sys
from invoke import task
from livereload import Server
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)
CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    # Port for `serve`
    "port": 8000,
}


@task
def clean(_):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(option):
    """Build local version of site"""
    option.run("pelican -s {settings_base}".format(**CONFIG))


@task
def rebuild(option):
    """`build` with the delete switch"""
    option.run("pelican -d -s {settings_base}".format(**CONFIG))


@task
def regenerate(option):
    """Automatically regenerate site upon file modification"""
    option.run("pelican -r -s {settings_base}".format(**CONFIG))


@task
def serve(_):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

        def str_name(self):
            return self.__class__.__name__

    server = AddressReuseTCPServer(CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler)

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(option):
    """`build`, then `serve`"""
    build(option)
    serve(option)


@task
def preview(option):
    """Build production version of site"""
    option.run("pelican -s {settings_publish}".format(**CONFIG))


@task
def livereload(option):
    """Automatically reload browser tab upon file modification."""
    build(option)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG["settings_base"], lambda: build(option))
    # Watch content source files
    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_blob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        server.watch(content_blob, lambda: build(option))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS["THEME"]
    server.watch("{}/templates/*.html".format(theme_path), lambda: build(option))
    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file = "{0}/static/**/*{1}".format(theme_path, extension)
        server.watch(static_file, lambda: build(option))
    # Serve output path on configured port
    server.serve(port=CONFIG["port"], root=CONFIG["deploy_path"])


@task
def publish(option):
    """Publish to production via rsync"""
    option.run("pelican -s {settings_publish}".format(**CONFIG))
    option.run(
        'rsync --delete --exclude ".DS_Store" -pthrvz -c '
        '-e "ssh -p {ssh_port}" '
        "{} {ssh_user}@{ssh_host}:{ssh_path}".format(CONFIG["deploy_path"].rstrip("/") + "/", **CONFIG)
    )
