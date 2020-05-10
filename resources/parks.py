import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

parks = Blueprint('parks', 'parks')

# INDEX -- /api/v1/parks (show parks)
@parks.route('/all', methods=['GET'])
def get_all_parks():
  parks = models.Park.select()
  park_dicts = [model_to_dict(park) for park in parks] 
  for park_dict in park_dicts:
    park_dict['owner'].pop('password')
    if not current_user.is_authenticated: 
      park_dict.pop('owner')
  return jsonify({
    'data': park_dicts,
    'message': f"Successfully FOUND {len(park_dicts)} (ALL) parks",
    'status': 200
  })

# TEST
@parks.route('/')
def parks_index():
  return "parks resource working"

# CREATE
@parks.route('/', methods=['POST'])
@login_required
def create_park():
  payload = request.get_json()
  print(payload)
  new_park = models.Park.create(
    name=payload['name'],
    isClean=payload['isClean'],
    isBig=payload['isBig'],
    isFenced=payload['isFenced'],
    isBusy=payload['isBusy'],
    owner=current_user.id
  )
  print(dir(new_park))
  park_dict = model_to_dict(new_park)
  print(park_dict)

  return jsonify(
    data=park_dict, 
    message='Successfully CREATED PARK',
    status=201
  ), 201

# DESTROY
@parks.route('/<id>', methods=['DELETE']) 
@login_required
def delete_park(id):
  try: 
    park_to_delete = models.Park.get_by_id(id)
    if park_to_delete.owner.id == current_user.id:
      park_to_delete.delete_instance()
      return jsonify(
        data={},
        message=f"Successfully DELETED PARK with id {id}",
        status=200
      ), 200
    else:
      return jsonify(
        data={
          'error': '403 Forbidden'
        },
        message="Park Creator owner's id DOES NOT MATCH dog's id. User can only DELETE their own dogs",
        status=403
      ), 403

  except models.DoesNotExist:
    return jsonify(
      data={
        'error': '404 Not found'
      },
      message="There is NO PARK with that ID.",
      status=404
    ), 404


# EDIT/UPDATE 
@parks.route('/<id>', methods=['PUT'])
# @login_required
def update_park(id):
  payload = request.get_json()
  park_to_update = models.Park.get_by_id(id)
  if park_to_update.owner.id == current_user.id:
    if 'name' in payload:
      park_to_update.name = payload['name']
    if 'isClean' in payload:
      park_to_update.isClean = payload['isClean']
    if 'isBig' in payload:
      park_to_update.isBig = payload['isBig']
    if 'isFenced' in payload:
      park_to_update.isFenced = payload['isFenced']
    if 'isBusy' in payload:
      park_to_update.isBusy = payload['isBusy']
    # if 'owner' in payload:
    #   park_to_update.owner = payload['owner']
    park_to_update.save()
    updated_park_dict = model_to_dict(park_to_update)
    updated_park_dict['owner'].pop('password')

    return jsonify(
        data=updated_park_dict,
        message=f"Successfully UPDATED PARK with id {id}",
        status=200
      ), 200
  # else:
  #   return jsonify(
  #     data={ 'error': '403 Forbidden'},
  #     message="Park's creator's id DOES NOT MATCH parks's id. User can only UPDATE their own dogs",
  #     status=403
  #   ), 403



























