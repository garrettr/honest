from flask import Flask, render_template
from flaskext.flatpages import FlatPages

app = Flask(__name__)
app.debug = True

pages = FlatPages(app)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'flatpage.html')
    return render_template(template, page=page)

if __name__ == "__main__":
    app.run()
