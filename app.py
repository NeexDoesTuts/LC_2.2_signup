from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def display_signup():
    return render_template('signup_form.html')


@app.route("/signup", methods=["POST"])
def signup_user():
    return "THIS IS POST"

if __name__ == "__main__":
    app.run()