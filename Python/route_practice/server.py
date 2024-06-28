from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:num>/<word>') # localhost:5000:/repeat/6/Snow
def repeat(num, word):
    return f"{word * num}" # SnowSnowSnowSnowSnowSnow

@app.route('/<name>') # localhost:5000:/misty
def name(name):
    return f"Hi {name.capitalize()}!" # Hi Misty!

@app.route('/<int:num>/<string:word>') # localhost:5000:/10/glitter
def repeat_word(num, word):
    output = ''
    for i in range(0, num):
        output += f"<p>{word}</p>" # 10 lines of glitter, 1 on each line
    return output

if __name__ == "__main__":
    app.run(debug=True)