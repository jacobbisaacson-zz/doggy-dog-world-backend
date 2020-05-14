import os
from flask import Flask, jsonify, g
from resources.dogs import dogs
from resources.users import users
from resources.parks import parks
from resources.user_prefs import user_prefs
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = "Super Secret Pizza Party."
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  try:
    print("Loading the following USER: ")
    user = models.User.get_by_id(user_id)
    return user
  except models.DoesNotExist:
    return None

@login_manager.unauthorized_handler
def unauthorized():
  return jsonify(
    data={
      'error': 'User is NOT LOGGED IN'
    },
    message="You must be LOGGED IN to access",
    status=401
  ), 401

CORS(dogs, origins=['http://localhost:3000', 'https://its-a-doggy-dog-world.herokuapp.com'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000', 'https://its-a-doggy-dog-world.herokuapp.com'], supports_credentials=True)
CORS(parks, origins=['http://localhost:3000', 'https://its-a-doggy-dog-world.herokuapp.com'], supports_credentials=True)
CORS(user_prefs, origins=['http://localhost:3000', 'https://its-a-doggy-dog-world.herokuapp.com'], supports_credentials=True)

app.register_blueprint(dogs, url_prefix='/api/v1/dogs')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(parks, url_prefix='/api/v1/parks')
app.register_blueprint(user_prefs, url_prefix='/api/v1/user_prefs')

@app.before_request
def before_request():
  print("you should see this before each request")
  g.db = models.DATABASE
  g.db.connect()


@app.after_request
def after_request(response):
  print("you should see this after each request")
  g.db.close()
  return response

@app.route('/')
def hello():
  return 'Hello, world!'

@app.route('/test_json')
def get_json():
  return jsonify(['hello', 'hi', 'hey'])

@app.route('/say_hello/<username>')
def say_hello(username):
  return "Hello {}".format(username)


if 'ON_HEROKU' in os.environ: 
  print('\non heroku!')
  models.initialize()


if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)

  