from app import app 
from flask import render_template, url_for





@app.route('/')
@app.route('/index')
def index():
    return(render_template("index.html"))

@app.route("/containers")
def containers():
    return("Hello containers")


@app.route("/images")
def images():
    return("Hello images")


@app.route("/settings")
def settings():
    return("Hello settings")


@app.route("/status")
def status():
    return("Hello status")