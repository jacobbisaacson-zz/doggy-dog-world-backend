import models
from flask import Blueprint, request

dogs = Blueprint('dogs', 'dogs')

# INDEX
@dogs.route('/', methods=['GET'])
def dogs_index():
	return "dogs resource working"

# CREATE
@dogs.route('/', methods=['POST'])
def create_dog():
  payload = request.get_json()
  print(payload)
  return "you hit dog create route -- check terminal"
