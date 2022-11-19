from flask_app import app
from flask import render_template, request, redirect, session, flash
# import more later

@app.route('/')
def display_advertisement():
    return render_template("advertisement.html")