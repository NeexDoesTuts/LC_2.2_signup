# Signup Form
## LC 101 Assignment 2.2
[Assignment text as of 2017/07/04](https://github.com/LaunchCodeEducation/web-fundamentals/blob/2fbda27ea3bdf489f04eb9e0770860a1a4778883/assignments/user-signup/README.md)

### Major requirements
1. If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:
    * [x] The user leaves any of the following fields empty: username, password, verify password.
    * [x] The user's password and password-confirmation do not match.
    * [x] The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
    * [x] Each feedback message should be next to the field that it refers to.
2. [x] For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.
3. [x] If all the input is valid, then you should show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"
4. [x] Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.