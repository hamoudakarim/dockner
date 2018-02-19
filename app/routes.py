from app import app 
from flask import render_template, url_for




@app.route('/')
@app.route('/home')
def index():
    return(render_template("index.html"))

@app.route("/containers")
def containers():
    return(render_template("containers.html"))


@app.route("/images")
def images():
    return(render_template("images.html"))


@app.route("/settings")
def settings():
    return(render_template("settings.html"))


@app.route("/status")
def status():
    return(render_template("status.html"))