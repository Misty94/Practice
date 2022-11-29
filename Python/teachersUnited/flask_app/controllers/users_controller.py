from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message
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

    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def process_login():

    current_user = User.get_one_by_email(request.form)
    if current_user == False:
        flash("Wrong email/password!", "error_login_credentials")
        return redirect('/')
    if current_user != False:
        if not bcrypt.check_password_hash(current_user.password, request.form['password']):
            flash("Wrong email/password!", "error_login_credentials")
            return redirect('/')
        else:
            session['first_name'] = current_user.first_name
            session['email'] = current_user.email
            session['user_id'] = current_user.id
            return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/profile/<int:id>')
def display_profile(id):
    if 'email' not in session:
        return redirect('/')

    data = {
        "id": id
    }
    one_user = User.get_one(data)
    messages = Message.get_my_messages(data)
    return render_template("profile.html", one_user = one_user, messages = messages)


@app.route('/create/about', methods=['POST'])
def process_about():
    if 'email' not in session:
        return redirect('/')
    
    data = {
        **request.form,
        "user_id": session['user_id']
    }
    User.save(data)
    return redirect('/dashboard')