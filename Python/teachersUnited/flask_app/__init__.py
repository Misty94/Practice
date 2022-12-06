from flask import Flask
import re

app = Flask(__name__)
app.secret_key = "t*69y?jkr$/bipwsq721~"

DATABASE = "teachers_united_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')