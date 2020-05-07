import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

dogs = Blueprint('dogs', 'dogs')

# INDEX
@dogs.route('/', methods=['GET'])
def dogs_index():
  result = models.Dog.select()
  print(result)
  dog_dicts = [model_to_dict(dog) for dog in result]
  print(dog_dicts)

  return jsonify({
    'data': dog_dicts,
    'message': f"Successfully found {len(dog_dicts)} dogs",
    'status': 200
  }), 200

# CREATE
@dogs.route('/', methods=['POST'])
def create_dog():
  payload = request.get_json()
  print(payload)
  new_dog = models.Dog.create(name=payload['name'], owner=payload['owner'], breed=payload['breed'])
  print(dir(new_dog))
  dog_dict = model_to_dict(new_dog)

  return jsonify(
    data=dog_dict, 
    message='Successfully created dog!',
    status=201
  ), 201


# DESTROY
@dogs.route('/<id>', methods=['DELETE']) 
def delete_dog(id):
  delete_query = models.Dog.delete().where(models.Dog.id == id)
  num_of_rows_deleted = delete_query.execute()
  print(num_of_rows_deleted)

  return jsonify(
    data={},
    message="Successfully DELETED {} dog with id {}".format(num_of_rows_deleted, id),
    status=200
  ), 200


# UPDATE
@dogs.route('/<id>', methods=['PUT'])
def update_dog(id):
  payload = request.get_json()
  update_query = models.Dog.update(
    name=payload['name'],
    breed=payload['breed'],
    owner=payload['owner']
  ).where(models.Dog.id == id)
  num_of_rows_modified = update_query.execute()
  updated_dog = models.Dog.get_by_id(id) 
  updated_dog_dict = model_to_dict(updated_dog)

  return jsonify(
      data=updated_dog_dict,
      message=f"Successfully UPDATE dog with id {id}",
      status=200
    ), 200








