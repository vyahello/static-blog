[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Actions Status](https://github.com/vyahello/static-blog/workflows/Code%20analysis/badge.svg)](https://github.com/vyahello/static-blog/actions)

# Static blog

This project contains static blog site powered by [pelican](https://github.com/getpelican/pelican) static site generator
and [netlify](https://www.netlify.com) hosting source.

## Tools
- python 3.8
- [pelican](https://github.com/getpelican/pelican)
  - html5
  - css3
  - bootstrap3
  - [markdown](https://pypi.org/project/Markdown)
- [travisCI](https://travis-ci.org/)
- [netlify](https://www.netlify.com/)
- code analysis
  - [black](https://black.readthedocs.io/en/stable/)
  - [pylint](https://www.pylint.org/)

## Usage

Move to output content folder and launch server locally:
```bash
➜ cd output
➜ python -m http.server 5001
Serving HTTP on :: port 5001 (http://[::]:5001/) ...
```
Then please open [localhost:5001](http://localhost:5001) endpoint.

## Development notes

### Generate site

- Start with `pelican-quickstart` tool to configure project:
```bash
➜ pelican-quickstart
```
- Create markdown page in [content/](content/) folder
- Generate site:
```bash
➜ pelican content
```
- Take a look at generated files under [output/](output/) folder

### CI

Project contains CI support in terms of running static code analysis procedure followed by [code-analysis.yml](.github/workflows/code-analysis.yml) file.

### Meta

Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all development project dependencies