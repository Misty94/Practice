# ----------------INSTALLATION COMMANDS ----------------------------------------------------------------------
# The HTTP request is made & hits the server.py file
# Based on the route we give, it gathers up any HTML, CSS, JS, & data
# Then it responds back to the browser with what we return

# Virtual Environment = a way to keep organized & avoid conflicts when working on different projects with different versions and packages.

# To Install WIndows: pip install pipenv
# To Install Mac: pip3 install pipenv

# You can create a folder, navigate into that folder using the terminal & use pipenv to create the environment & install Flask in one step
# pipenv install flask

# After running pipenv install, it creates 2 files: Pipfile & Pipfile.lock, which are needed to use the installed packages
# Pipfile will display the packages installed
# Pipfile.lock will have specific details on what version is being used

# If there is an error using pipenv, you may need to import it as a module first before it can be run as a script, EVERY time you use pipenv
# Windows: python -m pipenv <command to use>
# Mac: python3 -m pipenv <command to use>

# Activate the environment: pipenv shell (if an environment hasn't been created yet, this command will create one & activate it)

# Type the command: pip list (to see a list of what is currently installed)

# Deactivate the environment: exit

# DO NOT Create a Virtual Environment Within Another Virtual Environment

# Inside the created folder, create a file called server.py
# server.py will be our 'server' file where we set up all of our routes to handle requests

# Inside server.py:
from flask import Flask  # Import Flask to allow us to create our app -- this line is needed for every application built with Flask
app = Flask(__name__)    # Create a new instance of the Flask class called "app" -- this line is needed for every application built with Flask
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# You should see (name_of_folder) as the terminal prompt if your virtual environment is active

# To start the application, navigate to your project directory and run the server.py file
# Windows: (folder_name) $ python server.py
# Mac: (folder_name) $ python3 server.py
# Navigate to localhost:5000/ in your browser and see the message "Hello World!" --- this is a web server

# localhost:5000 -- the Flask web server listens for an HTTP request on this port
# Whenever a request is sent to the port, the server looks at the URL being requested & sends the appropriate response.
# If you go to route "/", the the hello_world() function will run - the client called the function, they receive what the function returns

# Running the app takes all of the routing rules that we set up & actually starts up the server

# Changing the port if localhost:5000 is already in use & can't be closed (8000 is a good alternative)
app.run(debug=True, host="localhost", port=8000)

# -------------------------------------ROUTES------------------------------------------------------------------------------------------------

# Routes - like a variable name we assign to a request - it communicates to the server what kind of information the client needs
# The route name is attached to a route on our server that points towards a specific set of instructions.
# These instructions contain information about how to interpret the dada being sent, operations that need to be completed, & the response that should be sent back
# Every route has two parts: HTTP method (GET, POST, PUT, PATCH, DELETE) and the URL

# adding another route to the server.py
@app.route('/success')
def success():
    return "success"
    
    # app.run(debug=True) should be the very last statement! 

# If the client requests localhost:5000/ the hello_world function will run
# If the client requests localhost:5000/success the success function will run

# Adding in variable rules:
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

# Type Converters - by default, a route variable is passed as a string. Designate int as the converter to indicate an integer is being passed
# Here the second parameter is cast into an integer before being passed to the function
@app.route('/hello/<name>/<int:num>') 
def hello(name, num):
    return f"Hello, {name * num}" # localhost:5000/hello/Misty/3 ---> Hello, MistyMistyMisty

# In python, when you multiply a string by an integer, it'll make a longer string with the original string repeated num number of times
# In python, if you multiply a string by another string, it will give an error

# If you went to localhost:5000/hello/Misty/rainbow ---> 404 Not Found --- would happen because 'rainbow' cannot be converted into an integer

# ---------------------------------------------TEMPLATES------------------------------------------------------------

# In Flask, create a directory alongside the server.py file called templates where all the HTML files will go

from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route('/')                           
def hello_world():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html')  
    
if __name__=="__main__":
    app.run(debug=True)                   

# ------------------------------------------JINJA---------------------------------------------------------------------

# Jinja --- Flask's templating engine (has a lot of great built-in features that allow dynamic information on HTML pages)

# Since the browser doesn't understand Python code, the render_template function sends the HTML file along with any data passed through the template engine to resolve any code into HTML
# The final product is the response to the client

@app.route('/hello')
def hello():
    return render_template("index.html", phrase="Hello! ", times = 5)

# Two Special Inputs to use to insert Python-like code into our Flask Templates
# {{ some variable }}
# {% some expression %}

# project_folder/templates/index.html

# <p> Phrase: {{ phrase }} </p> 
# <p> Times: {{ times }} </p>

# {% for x in range(0, times): %}
    # <p> {{ phrase }} </p>
# {% endfor %}

# {% if phrase == "Hello!" %}
    # <p> The phrase says hello </p>
# {% endif %}

# For Loops -- How many times something gets rendered
# If Statement -- Control what gets rendered
# Printing values to our rendered html

# Try to limit the amount of logic put into the templates & do the bulk of the logic in the Python code!
# Putting too much logic in your template may slow down the server response time

# -----------------------------------------STATIC-------------------------------------------------------------

# Static Content --- any content that can be served up to the client without being modified, generated, or processed by the server
# Create a directory called static to house all Stylesheets, Images, and JavaScript files

# Inside a static folder is: my_img.png, my_script.js, and my_style.css

# On your HTML file:
# <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">     --- linking a css stylesheet

# <script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>     --- linking a javascript file

# <img src="{{ url_for('static', filename='my_img.png') }}">     --- linking an image


# For better organization, inside the static folder, create directories called css, js, and img

# <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style.css') }}">     --- linking a css stylesheet

# <script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>     --- linking a javascript file

# <img src="{{ url_for('static', filename='img/my_img.png') }}">     --- linking an image

# Note: When using static files, your browser will likely cache them, so if needed while updating these files, do a hard refresh of the page
# Hard Refresh on Windows: ctrl + shift + r
# Hard Refresh on Mac: cmd + shift + r


# -----------LISTS IN JINJA-------------------------------------------------------------

# In server.py
@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

# project_folder/templates/lists.html
# <h1> Random Numbers </h1>
# {% for number in random_numbers %}
    # <p> {{ number }} </p>
# {% endfor %}
# <h1> Students </h1>
# {% for student in students %}
    # <p> {{ student['name'] }} - {{ student['age'] }} </p>
# {% endfor %}

# On the Browser:

# Random Numbers
# 3
# 1
# 5
# Students
# Michael - 35
# John - 30
# Mark - 25
# KB - 27

# --------------------POST FORM SUBMISSION--------------------------------------------------------------------

# GET -- requests that display information from the server to the user
# POST -- requests where the client sends information to the server

# The modern internet is User-Driven where much of the content of a website is generated by the Users of a website
# Users provide content to a website using FORMS!
# HTML Forms are the way users are able to pass data to the back end of a websit, where the data is processed & stored
# Processing form data correctly is a huge part of what it takes to become a back-end developer

@app.route('/form') # This route will SHOW the form
def form():
    return render_template('form.html')

# Create a form.html in the templates folder
# <form action='/users' method='post'>    --- This says that the POST request should be handled with the route /users
    # <label for='name'>Name:</label>
    # <input type='text' name='name'>    --- Each element should have a Unique Value for it's name attribute!!!
    # <label for='email'>Email:</label>
    # <input type='text' name='email'>
    # <input type='submit' value='Create User'>
# </form>


from flask import Flask, render_template, request, redirect # added request and redirect
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

# The name given to each HTML input is significant. 
# On the server-side, we can access data that was input into a field form from a user through the request.form dictionary 
# by providing the name of the input as the key
# To see what's in your request object, try printing request.form

# The type of anything that comes in through request.form will be a 'string' no matter what
# If you want the value to be identified as an actual number, you'll have to type cast it

# -----------------REDIRECTING------------------------------------------------------------------------------------------------

# NEVER render a template on a POST request!!!  (it could duplicate data in the app or over-charge credit cards)
# ALWAYS redirect after handling POST data to avoid data being handled more than once!

# When the POST data is finished processing, we can prefrom a GET request on behalf of the client which redirects them

from flask import Flask, render_template, request, redirect # don't forget to import redirect!
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    return redirect("/show")	 
    
# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form) # <---- This did not show the info that was just submitted on the form!
    return render_template("show.html")

#-----------------------SESSION------------------------------------------------------------------------------------

# Each method that is handling a route doesn't know anything about any of the other routes

# The HTTP request/response cycle is STATELESS - each request/response cycle is independent & ignorant of all other requests before or after

# Above, we made one request to POST the form data, then a second request to GET the /show route & redirect.
# The second request has no access to the first request

# Many sites make use of Persistent Data Storage. One form of persistence is Session.

# Session - saving or writing certain valuable pieces of data for use in future cycles & reading that data we've stored in previous cycles
# With session, we can establish a relationship with the client
# With session, the user can have a conversation with a website, where the user makes decisions that can be tracked & the server can create a more cohesive user experience

# State - the data that Outlives the process (HTTP request/response) that generated it
# State allows our site to know a lot of useful info like:
# Whether there is a user logged in, who the current user is, what links a user has previously viewed 

# We get to decide what to save about our clients --- session is a tool for developers to use to their advantage
# We keep state data in session to help us solve problems down the line i.e. in subsequent HTTP requests

# Persistent data storage helps us bridge the gap between a stateless protocol (HTTP) with the stateful data generated through it
# Databases are another tool fro persistent data storage

# ** DON'T abuse the amount of information you store in session!!! Store ONLY what you need!!! **

# Cookies - some frameworks, including Flask, use cookies to store session data
# Flask uses secure hashing of session data to send a packet of information from server to client -- that packet is known as a cookie!
# Once a client's browser has recieved this cookie, it writes the information contained in it to a small file on their hard drive

# While hashed, COOKIES ARE NOT INCREDIBLY SECURE, so DON'T save anything private in them!!

from flask import Flask, render_template, request, redirect, session # Import session

# To use session in Flask, it also requires you give your app a Secret Key
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# The create_user method is the method we receive the information from the POST request, write the information to session in this method
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

# Previously in our show_user function, we didn't have access to the name & email from the form submission.
# Now, because of session, we have a way to access the name & email in a different function

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

# Now we're passing the information stored in session to the templates using named arguments
# Session data is also available directly in our templates, so now we can do this:

@app.route('/show')
def show_user():
    return render_template('show.html')

# project_folder/templates/show.html

# <h1>User:</h1>
# <h3>{{session['username']}}</h3>
# <h3>{{session['useremail']}}</h3>

