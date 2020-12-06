import sys
import argparse

from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_bootstrap import Bootstrap

DEBUG = True
# Various config flags
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_DESTINATION = 'docs'

# bootstrap-flask flags
BOOTSTRAP_BOOTSWATCH_THEME = 'lux'
BOOTSTRAP_SERVE_LOCAL = True

app = Flask(__name__)
app.config.from_object(__name__)
bootstrap = Bootstrap(app)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@freezer.register_generator
def pagelist():
    print('pages:', pages)
    for page in pages:
        yield url_for('page', path=page.path)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true', help='Builds static html pages from readmes')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.build:
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port=5000)

