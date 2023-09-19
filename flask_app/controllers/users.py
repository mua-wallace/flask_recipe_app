from flask_app import app
from flask import render_template


# register and login route
@app.route("/")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

