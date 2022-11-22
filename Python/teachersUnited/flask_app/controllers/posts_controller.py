from flask_app import app
from flask import render_template, request, redirect, session, flash

@app.route('/dashboard')
def display_dashboard():
    return render_template("dashboard.html")