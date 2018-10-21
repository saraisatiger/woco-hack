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


app = Flask(__name__)

# Get HTML content from URL
htmlList = [
        urlopen('https://www.shelterlistings.org/city/west_palm_beach-fl.html'),        # shelter
        urlopen('http://www.crosministries.org/contactus.php?CROSpagename=contactus')   # food
        # , urlopen('<jobs.url>')
    ]

# Convert HTML content BeautifulSoup object
soupList = []
for html in htmlList:
    soupList.append(BeautifulSoup(html.read(), 'html5lib'))

# Parse relevant HTML content (as HTML)
shelterContent = soupList[0].find('tbody')
foodContent = soupList[1].find('article', {'class' : 'grid_6'})
# jobsContent = soupList[2].find('tbody')

@app.route('/')
def main():
    with open("includes/shelter.html", "w") as file:
        file.write(str(shelterContent))

    with open("includes/food.html", "w") as file:
        file.write(str(foodContent))

    # with open("includes/jobs.html", "w") as file:
        # file.write(str(jobContent))

    return "Kthanksbye!"
