from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message
from flask_bcrypt import Bcrypt
# from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
# from geopy.geocoders import Nominatim

bcrypt = Bcrypt(app)

@app.route('/')
def display_advertisement():
    # try:
    #     cn_a2_code = country_name_to_country_alpha2(col)
    # except:
    #     cn_a2_code = 'Unknown'
    # try:
    #     cn_continent = country_alpha2_to_continent_code(cn_a2_code)
    # except:
    #     cn_continent = 'Unknown'

    # cn_a2_code = cn_a2_code, cn_continent = cn_continent
    markers = [
        {
            'lat': 0,
            'lon': 0,
            'popup': 'This is the middle of the map.'
        }
    ]
    return render_template("advertisement.html", markers = markers)


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


@app.route('/create/profile/<int:id>', methods=['POST'])
def process_profile(id):
    if 'email' not in session:
        return redirect('/')

    used_username = User.get_one_by_username(request.form)
    if used_username != False:
        flash("This username is already in use; please choose another.", "error_profile_username")
        return redirect(f'/profile/{id}')
    
    profile_data = {
        **request.form,
        "id": id
    }
    User.finish_profile(profile_data)
    return redirect(f'/profile/{id}')