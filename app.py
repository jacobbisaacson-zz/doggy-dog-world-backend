from flask import Flask, jsonify
from resources.dogs import dogs
from resources.users import users
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = "Super Secret Pizza Party."
login_manager = LoginManager()
login_manager.init_app(app)

CORS(dogs, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(dogs, url_prefix='/api/v1/dogs')
app.register_blueprint(users, url_prefix='/api/v1/users')


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
      'error': 'USER is not LOGGED IN'
    },
    message="You must be LOGGED IN to access that resource",
    status=401
  ), 401


@app.route('/')
def hello():
  return 'Hello, world!'

@app.route('/test_json')
def get_json():
  return jsonify(['hello', 'hi', 'hey'])

@app.route('/say_hello/<username>')
def say_hello(username):
  return "Hello {}".format(username)



if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)

  