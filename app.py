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
			$ flask run

		# Rerun app (after code changes)
			$ sudo lsof -i:5000
			$ sudo kill <the_process_running_on_port_5000>
"""

from flask import Flask
from bs4 import BeautifulSoup
from urllib2 import urlopen
import html5lib

app = Flask(__name__)
html = urlopen("https://www.python.org/")
res = BeautifulSoup(html.read(),"html5lib");

@app.route("/")
def main():
	return "Hello, World! It's me, new string!"
