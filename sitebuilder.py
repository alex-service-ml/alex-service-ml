import sys
import argparse
import os

from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_bootstrap import Bootstrap
from markdown_checklist.extension import ChecklistExtension

DEBUG = True
# Various config flags
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['tables', 'codehilite', 'fenced_code', ChecklistExtension()]
FLATPAGES_EXTENSION_CONFIGS = { 'codehilite': {'use_pygments': True}, 'tables': [], 'fenced_code': []  }
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
    articles = filter(lambda x: x['title'], pages)
    articles = sorted(list(articles), reverse=True, key=lambda x: x.meta['date'])
    return render_template('index.html', pages=articles)

@app.route('/resume.html')
def resume():
    return page('resume')


@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('page', path=page.path)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true', help='Builds static html pages from readmes')
    return parser.parse_args()

def build_site():
    freezer.freeze()
    
    # Github pages CSS fix
    # adds project name to local path for bootstrap-flask
    for pagename in os.listdir(FREEZER_DESTINATION):
        print(f"Building {pagename}")
        if pagename.endswith('.html'):
            with open(os.path.join(FREEZER_DESTINATION, pagename)) as f:
                contents = f.read().replace('/bootstrap/static/', 'alex-service-ml/bootstrap/static/')
            with open(os.path.join(FREEZER_DESTINATION, pagename), 'w') as f:
                f.write(contents)

if __name__ == '__main__':
    args = parse_args()
    if args.build:
        freezer.freeze()
        # build_site()
    else:
        app.run(host='0.0.0.0', port=5000)

