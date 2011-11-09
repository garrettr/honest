# Notes

Honest Appalachia's website. Separate from the file upload infrastructure.

Page infrasturcture is to be similar to Jekyll. You can place HTML files optionally containing Markdown in `/pages`. They will be rendered and served at the url that matches their filename. For example, the file `pages/home.html` renders to `/home/`. Files to be rendered as flat pages must have a `.html` extension.

# Quickstart

To get started with working on this code, first clone the repo

    git clone git@github.com:handsomeransoms/haps.git

We're developing for Python 2.6 right now.
You will need to install Python library dependencies to use this code. To do this easily and without cluttering up your system, use [virtualenv]. Here's how to setup virtualenv:

1.  cd into the directory of the cloned repo
2.  `virtualenv env` creates a new virtualenv and installs Python into it.
3.  `. env/bin/activate` activates the virtualenv. You will see `(env)` prepended to your bash prompt.
4.  Install the dependencies

## Dependencies

We recommend using pip to install these packages: `easy_install pip`, and installing into your virtualenv.

1.  [Flask web microframework]: `pip install flask`
2.  [pydns]: `pip install pydns`

[virtualenv]: http://www.arthurkoziel.com/2008/10/22/working-virtualenv/
[Flask web microframework]: http://flask.pocoo.org/
[pydns]: http://pydns.sourceforge.net/
