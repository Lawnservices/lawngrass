from flask import Flask, render_template

app = Flask(__name__)

@app.route("/facecom/index")
def index():
    return render_template("index.html")

@app.route("/facecom/login")
def login():
    return render_template("login.html")

@app.route("/facecom/register")
def register():
    return render_template("register.html")

@app.route("/facecom/profile")
def profile():
    return render_template("profile.html")

@app.route("/facecom/settings")
def settings():
    return render_template("settings.html")

@app.route("/facecom/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
