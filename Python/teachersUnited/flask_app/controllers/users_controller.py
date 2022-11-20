from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def display_advertisement():
    return render_template("advertisement.html")


@app.route('/register', methods=['POST'])
def process_registration():
    if User.validate_user(request.form) == False:
        return redirect('/')

    user_already_exists = User.get_one_by_email(request.form)
    if user_already_exists != False:
        flash("This email already exists!", "error_registration_email")
        return redirect('/')
    
    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)
    user_id = User.save(data)

    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect('/dashboard') # where to?