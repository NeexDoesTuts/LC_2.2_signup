from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return redirect("/signup")

@app.route("/signup")
def display_signup():
    return render_template('signup_form.html')


def is_empty(str):
    if str == "":
        return True
    else:
        return False

@app.route("/signup", methods=["POST"])
def validate_signup_form():
    username = request.form["username"]
    password = request.form["password"]
    password_repeat = request.form["password_repeat"]
    email = request.form["email"]
    
    if is_empty(username) and (is_empty(password) or is_empty(password_repeat)):
        return render_template('signup_form.html', 
                username_error="User field cannot be left empty.", 
                password_error="Password fields cannot be left empty.")
    elif is_empty(username):
        return render_template('signup_form.html', username_error="User field cannot be left empty.")
    elif is_empty(password) or is_empty(password_repeat):  
        return render_template('signup_form.html', password_error="Password fields cannot be left empty.")
    else: 
        return render_template("signup_form.html", welcome="all good!")


if __name__ == "__main__":
    app.run()