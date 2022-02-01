from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template("prompt.html")

@app.route("/steve")
def steve_page():
    return render_template("prompt.html", name="Steve")