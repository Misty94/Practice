from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.post_model import Post
from flask_app.models.message_model import Message
from flask_app.models.comment_model import Comment

@app.route('/dashboard')
def display_dashboard():
    if 'email' not in session:
        return redirect('/')
    
    posts = Post.get_all_with_users()
    # comments = Comment.get_all_with_posts()
    comments = Comment.connect_comment_to_post()
    return render_template("dashboard.html", posts = posts, comments = comments)


@app.route('/create/post', methods=['POST'])
def process_post():
    if 'email' not in session:
        return redirect('/')
    
    if Post.validate_post(request.form) == False:
        return redirect('/dashboard')
    
    data = {
        **request.form,
        "user_id": session['user_id']
    }
    Post.save(data)
    return redirect('/dashboard')


@app.route('/create/message', methods=['POST'])
def process_message():
    if 'email' not in session:
        return redirect('/')

    data = {
        "content": request.form['content'],
        "user_id": request.form['user_id'],
        "friend_id": request.form['friend_id']
    }
    Message.save(data)
    return redirect('/dashboard')


@app.route('/create/comment', methods=['POST'])
def process_comment():
    if 'email' not in session:
        return redirect('/')

    data = {
        **request.form,
        "user_id": session['user_id']
    }
    Comment.save(data)
    return redirect('/dashboard') # Can we redirect to the page they were on - we would need the id???