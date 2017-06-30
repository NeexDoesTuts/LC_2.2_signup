from flask import Flask, redirect

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def signup():
    return "Hello"

if __name__ == "__main__":
    app.run()