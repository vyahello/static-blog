[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Build Status](https://travis-ci.org/vyahello/static-blog.svg?branch=master)](https://travis-ci.org/vyahello/static-blog)
[![Actions Status](https://github.com/vyahello/static-blog/workflows/Code%20analysis/badge.svg)](https://github.com/vyahello/static-blog/actions)
[![Netlify Status](https://api.netlify.com/api/v1/badges/12678110-3433-4e2b-b92b-7a2ed3f9dd63/deploy-status)](https://app.netlify.com/sites/vyahello/deploys)

# Static blog

> This project contains static blog template powered by [pelican](https://github.com/getpelican/pelican) static site generator 
> and [netlify](https://www.netlify.com) hosting source.

_Note: please take into account that it is built for demo purpose but not for actual usage. 
Use it as a template source._

## Tools
- front-end
  - html5
  - css3
  - bootstrap3
- back-end
  - python 3.6 | 3.7 | 3.8
  - [pelican](https://github.com/getpelican/pelican)
- [netlify](https://www.netlify.com/) hosting
- code analysis
  - [black](https://black.readthedocs.io/en/stable/)
  - [pylint](https://www.pylint.org/)
  - [travis](https://travis-ci.org/) CI
  - [github](https://github.com/vyahello/static-blog/actions?query=workflow%3A%22Code+analysis%22) CI

## Usage

### Quick start

Please check https://vyahello.netlify.com to see how it looks like.

### Source code

Move to output content folder and launch server locally:
```bash
cd output
python -m http.server 5001
```
Then please open [localhost:5001](http://localhost:5001) endpoint.

## Development notes

### Generate site

- Configure project:
```bash
pelican-quickstart
```
- Create markdown page in [content/](content/) folder
- Generate site:
```bash
pelican content
```
- Take a look at generated files under [output/](output/) folder
- Build site on [netlify](https://www.netlify.com) (note it supports either `3.7` or `3.5` versions)

### CI

Project contains CI support in terms of running static code analysis procedure followed by [code-analysis.yml](.github/workflows/code-analysis.yml) file.

### Meta

Author – _Volodymyr Yahello_.

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all development project dependencies
