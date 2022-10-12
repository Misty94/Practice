from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def display_login_registration():
    return render_template("login.html")


@app.route('/register/user', methods=['POST'])
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

    return redirect('/wall')


@app.route('/login/user', methods=['POST'])
def process_login():

    current_user = User.get_one_by_email(request.form)
    if current_user == False:
        flash("Wrong email/password", "error_login_credentials")
        return redirect('/')
    if current_user != False:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Wrong email/password", "error_login_credentials")
            return redirect('/')
        else:
            session['first_name'] = current_user.first_name
            session['email'] = current_user.email
            session['user_id'] = current_user.id
            return redirect('/wall')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')