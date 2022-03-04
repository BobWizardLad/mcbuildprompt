from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def build_prompt():
    return render_template("builds.html")
    pass

@app.route("/decor")
def decor_prompt():
    return render_template("decor.html")

@app.route("/lore")
def lore_prompt():
    return render_template("lore.html")

@app.route("/rooms")
def room_prompt():
    return render_template("rooms.html")

@app.route("/theme")
def theme_prompt():
    return render_template("theme.html")