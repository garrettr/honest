from flask import Flask
from flaskext.flatpages import FlatPages

from run import build_pages_hierarchy

app = Flask(__name__)
pages = FlatPages(app)

print build_pages_hierarchy(pages)
