from flask import Flask, render_template, request
from flask_pymongo import PyMongo

DATABASE_URI = 'mongodb+srv://drparking:qwertyuiop@earth.qvsht3g.mongodb.net/kuchhbhi'

app = Flask(__name__)
app.config["SECRET_KEY"] = "<KEY>"
app.config["MONGO_URI"] = DATABASE_URI
db = PyMongo(app).db

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(db.accounts.find_one({"email": email}))

        if (db.accounts.find_one({"email": email}) and db.accounts.find_one({"password": password})) is None:
            return render_template("login.html", disblay="incorrect username or password")
        else:
            return "Login Successful"

    return render_template('login.html', disblay="")


@app.route('/ForgotPassword', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        # Here you'd handle the logic for sending a password reset email.
        return "Password reset link sent"

    return render_template('Forgor.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            return render_template('Register.html', disblay="Passwords do not match")

        # Here you'd handle the logic to store the new user in the database.
        return "Registration Successful"

    return render_template('Register.html', disblay="")

if __name__ == '__main__':
    app.run(debug=True)