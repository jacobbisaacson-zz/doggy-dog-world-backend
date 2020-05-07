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























if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)

  