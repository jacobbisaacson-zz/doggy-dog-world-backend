import models
from flask import Blueprint

dogs = Blueprint('dogs', 'dogs')

@dogs.route('/')
def dogs_index():
	return "dogs resource working"