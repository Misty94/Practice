from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.post_model import Post
# from flask_app.models.user_model import User

@app.route('/dashboard')
def display_dashboard():
    if 'email' not in session:
        return redirect('/')
    
    posts = Post.get_all_with_users()
    return render_template("dashboard.html", posts = posts)


@app.route('/create/post', methods=['POST'])
def process_post():
    if 'email' not in session:
        return redirect('/')