from application import app
from flask import render_template
import os

server_status = os.getenv('FLASK_ENV')


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/james')
def james():
    return f"<H1>Hi JAMES</H1>" \
           f"the system is in {server_status} MODE "
