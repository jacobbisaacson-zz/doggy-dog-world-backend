import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

dogs = Blueprint('dogs', 'dogs')

# INDEX -- /api/v1/dogs (SHOW MY DOGS)
@dogs.route('/', methods=['GET'])
@login_required
def dogs_index():
  current_user_dog_dicts = [model_to_dict(dog) for dog in current_user.dogs]
  print(current_user_dog_dicts)
  for dog_dict in current_user_dog_dicts:
    dog_dict['owner'].pop('password')
  print(current_user_dog_dicts)

  return jsonify({
    'data': current_user_dog_dicts,
    'message': f"Successfully FOUND {len(current_user_dog_dicts)} (YOUR) dogs",
    'status': 200
  }), 200

# INDEX -- SHOW ALL DOGS
@dogs.route('/all', methods=['GET'])
def get_all_dogs():
  dogs = models.Dog.select()
  dog_dicts = [model_to_dict(dog) for dog in dogs] 
  for dog_dict in dog_dicts:
    dog_dict['owner'].pop('password')
    if not current_user.is_authenticated: 
      dog_dict.pop('owner')
  return jsonify({
    'data': dog_dicts,
    'message': f"Successfully FOUND {len(dog_dicts)} (ALL) dogs",
    'status': 200
  })
  

# CREATE
@dogs.route('/', methods=['POST'])
@login_required
def create_dog():
  payload = request.get_json()
  print(payload)
  new_dog = models.Dog.create(
    name=payload['name'], 
    owner=current_user.id, 
    breed=payload['breed'],
    image=payload['image']
  )
  print(dir(new_dog))
  dog_dict = model_to_dict(new_dog)
  print(dog_dict)
  dog_dict['owner'].pop('password')

  return jsonify(
    data=dog_dict, 
    message='Successfully CREATED dog',
    status=201
  ), 201


# DESTROY
@dogs.route('/<id>', methods=['DELETE']) 
@login_required
def delete_dog(id):
  try: 
    dog_to_delete = models.Dog.get_by_id(id)
    if dog_to_delete.owner.id == current_user.id:
      dog_to_delete.delete_instance()
      return jsonify(
        data={},
        message=f"Successfully DELETED dog with id {id}",
        status=200
      ), 200
    else:
      return jsonify(
        data={
          'error': '403 Forbidden'
        },
        message="Dog owner's id DOES NOT MATCH dog's id. User can only DELETE their own dogs",
        status=403
      ), 403
  except models.DoesNotExist:
    return jsonify(
      data={
        'error': '404 Not found'
      },
      message="There is NO DOG with that ID.",
      status=404
    ), 404  


# UPDATE
@dogs.route('/<id>', methods=['PUT'])
@login_required
def update_dog(id):
  payload = request.get_json()
  dog_to_update = models.Dog.get_by_id(id)
  if dog_to_update.owner.id == current_user.id:
    if 'name' in payload:
      dog_to_update.name = payload['name']
    if 'breed' in payload:
      dog_to_update.breed = payload['breed']
    if 'image' in payload:
      dog_to_update.image = payload['image']
    dog_to_update.save()
    updated_dog_dict = model_to_dict(dog_to_update)
    updated_dog_dict['owner'].pop('password')

    return jsonify(
        data=updated_dog_dict,
        message=f"Successfully UPDATED dog with id {id}",
        status=200
      ), 200
  else:
    return jsonify(
      data={ 'error': '403 Forbidden'},
      message="Dog owner's id DOES NOT MATCH dog's id. User can only UPDATE their own dogs",
      status=403
    ), 403

# SHOW DOG
@dogs.route('/<id>', methods=['GET'])
def show_dog(id):
  dog = models.Dog.get_by_id(id)
  if not current_user.is_authenticated:
    return jsonify(
      data={
        'name': dog.name,
        'breed': dog.breed,
        'image': dog.image
      },
      message="ONLY REGISTERED USERS can see more info about this dog",
      status=200
    ), 200
  else: 
    dog_dict = model_to_dict(dog)
    dog_dict['owner'].pop('password')
    if dog.owner.id != current_user.id:
      dog_dict.pop('created_at')
    return jsonify(
      data=dog_dict,
      message=f"FOUND DOG with id {id}",
      status=200
    ), 200









