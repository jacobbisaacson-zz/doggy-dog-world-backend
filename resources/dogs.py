import models
from flask import Blueprint

dogs = Blueprint('dogs', 'dogs')

# INDEX
@dogs.route('/', methods=['GET'])
def dogs_index():
	return "dogs resource working"

# CREATE
@dogs.route('/', methods=['POST'])
def create_dog():
	return "hitting create_dog route"