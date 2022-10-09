from application import app
from flask import render_template


@app.route('/')
@app.route("/index")
def index():
    return "<h1>I am here, from {{testing_count}} James C {{FLASK_DEBUG}}  Randall. app ini no Debug is active</h1>"
