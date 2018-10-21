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
html = urlopen('https://thelordsplace.org/what-we-do/employment-training/')

# Convert HTML content BeautifulSoup object
soup = BeautifulSoup(html.read(), 'html5lib');

# Parse relevant HTML content (as HTML)
htmlContent = soup.find('div', {'class':'content-primary'})

@app.route('/')
def main():
    # return str(htmlContent) # hack to dump content; TODO need to write out to .html file in subdirectory
	with open("jobs.html", "w") as f:
		f.write(str(htmlContent))
		
	return "Done"
