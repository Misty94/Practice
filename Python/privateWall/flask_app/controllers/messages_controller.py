from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.message_model import Message

@app.route('/wall')
def wall_home():
    if 'email' not in session:
        return redirect('/')

    return render_template("wall.html")


@app.route('/create/message', methods=['POST'])
def process_new_message():
    if Message.validate_message(request.form) == False:
        return redirect('/wall')

    data = {
        **request.form,
        "user_id": session['user_id']
    }
    Message.save(data)
    return redirect('/wall')


@app.route('/delete/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.delete_one(data)
    return redirect('/wall')