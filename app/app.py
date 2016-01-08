import os

from flask import Flask, render_template
app = Flask(__name__)
from flaskext.lesscss import lesscss
app.config.from_object('config')
lesscss(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user")
def get_user():
    return "famani3"
