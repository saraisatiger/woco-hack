"""
    Usage:
        --- Do this first, once ---
        # Install python interpreter: https://www.python.org/downloads/release/python-2715/
        # Install packages:
            $ pip install flask
            $ pip install BeautifulSoup
            $ pip install urllib2
            $ pip install html5lib
        # Import app
            $ export FLASK_APP = app
        ---
        # Start app on http://localhost:5000
"""
from flask import Flask
from bs4 import BeautifulSoup
from urllib2 import urlopen
import html5lib
import json
from pprint import pprint


app = Flask(__name__)

# Get HTML content from URL
html = urlopen('http://www.crosministries.org/contactus.php?CROSpagename=contactus')

# Convert HTML content BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html5lib');

# Parse relevant HTML content (as HTML)
htmlContent = soup.find('article', {'class':'grid_6'})

@app.route('/')
def main():
    return str(htmlContent) # hack to dump content; TODO need to write out to .html file in subdirectory
