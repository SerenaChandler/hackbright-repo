"""Greeting Flask app."""

from random import choice
from flask import Flask, request



# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'bad','poopy','stupid'
]
@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html><body> <h1>Hi! This is the home page.<h1>
    <h2><a href="/hello"/> click here to go to hello! </h2>

    </body>
    
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/dis">
          What's your name? <input type="text" name="person">
          <div>
            <select name="type">
              <option value="compliment">Compliment</option>
              <option value="dis">Insult</option>
            </select>
          </div>
          <input type="submit" value="Submit">
        </form>
        <h2><a href="/"/>click here to go back to home</h2>
      </body>
    </html>
    """


@app.route('/compliment')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/dis')
def insult_person():
  """insults user"""
  player = request.args.get("person")
  insult = choice(INSULTS)
  return f"""
  <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
