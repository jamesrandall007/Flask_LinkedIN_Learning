from application import app
from flask import render_template
from flask import send_from_directory
import os

server_status = os.getenv('FLASK_ENV')


@app.route('/')
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/courses")
def courses():
    return render_template("courses.html", login=True)


@app.route("/register")
def register():
    return render_template("register.html", login=True)


@app.route('/james')
def james():
    return f"<H1>Hi JAMES</H1> the system is in {server_status} MODE "


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico')
