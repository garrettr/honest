from flask import Flask, render_template, redirect, request
from flaskext.flatpages import FlatPages

import sys, os

import torcheck

app = Flask(__name__)

pages = FlatPages(app)

@app.route('/')
def home():
    return redirect('/home')

@app.route('/upload/', methods=['GET'])
def upload():
    '''
    Checks if this request came over the Tor network.
    
    If so, redirects to hidden service.
    Otherwise, displays a warning and a link to the docs on safe uploading.
    '''
    if torcheck.is_using_tor(request):
        # redirect to hidden service
        redirect_to("http://www.google.com")
    else:
        return render_template("upload.html")

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'flatpage.html')
    return render_template(template, page=page)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--heroku":
            port = int(os.environ.get("PORT", 5000))
            app.run(host='0.0.0.0', port=port)
        elif sys.argv[1] == "--dev":
            app.debug = True
            app.run()
        else:
            print "What?"
            sys.exit(1)
    else:
        print "USAGE: python run.y [--heroku, --dev]"
        sys.exit(1)

