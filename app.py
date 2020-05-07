from flask import Flask, jsonify

DEBUG=True
PORT=8000

app = Flask(__name__)

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
	app.run(debug=DEBUG, port=PORT)

  