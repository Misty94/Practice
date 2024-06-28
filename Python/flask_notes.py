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

