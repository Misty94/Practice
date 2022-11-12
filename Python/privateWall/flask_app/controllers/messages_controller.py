from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models import message_model, user_model

@app.route('/wall')
def wall_home():
    if 'email' not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }
    user = user_model.User.get_one(data)
    messages = message_model.Message.get_my_messages(data)
    users = user_model.User.get_all()

    return render_template("wall.html", user = user, users = users, messages = messages)


@app.route('/create/message', methods=['POST'])
def process_new_message():
    if 'user_id' not in session:
        return redirect('/')

    if message_model.Message.validate_message(request.form) == False:
        return redirect('/wall')

    data = {
        "content": request.form['content'],
        "user_id": request.form['user_id'],
        "friend_id": request.form['friend_id']
    }
    message_model.Message.save(data)
    return redirect('/wall')


@app.route('/delete/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    message_model.Message.delete_one(data)
    return redirect('/wall')