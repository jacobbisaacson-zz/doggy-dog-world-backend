import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

parks = Blueprint('parks', 'parks')

# INDEX -- /api/v1/parks (show parks)
# @parks.route('/all', methods=['GET'])
# def get_all_parks():
#   parks = models.Park.select()
#   park_dicts = [model_to_dict(park) for park in parks] 
#   for park_dict in park_dicts:
#     park_dict['owner'].pop('password')
#     if not current_user.is_authenticated: 
#       park_dict.pop('owner')
#   return jsonify({
#     'data': park_dicts,
#     'message': f"Successfully FOUND {len(park_dicts)} (ALL) parks",
#     'status': 200
#   })

# TEST
@parks.route('/')
def parks_index():
  return "parks resource working"