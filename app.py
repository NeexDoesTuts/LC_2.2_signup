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
    
    # Check for emptiness and assign error messages
    username_error = "User field cannot be left empty." if is_empty(username) else ""
    password_error = "Password field cannot be left empty." if is_empty(password) else ""
    password_repeat_error = "Password field cannot be left empty." if is_empty(password_repeat) else ""

    return render_template('signup_form.html', 
            username_error=username_error, 
            password_error=password_error, 
            password_repeat_error=password_repeat_error)



if __name__ == "__main__":
    app.run()