import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

user_prefs = Blueprint('user_prefs', 'user_prefs')

# TEST
@user_prefs.route('/')
def user_prefs_index():
  return "user_prefs resource working"

# INDEX
@user_prefs.route('/show', methods=['GET'])
@login_required
def user_prefs_show():
  current_user_user_pref_dicts = [model_to_dict(user_pref) for user_pref in current_user.user_prefs]
  print(current_user_user_pref_dicts)
  for user_pref_dict in current_user_user_pref_dicts:
    user_pref_dict['owner'].pop('password')
  print(current_user_user_pref_dicts)

  # might want to pop passwords

  return jsonify({
    'data': current_user_user_pref_dicts,
    'message': f"Successfully FOUND {len(current_user_user_pref_dicts)} (YOUR) USER PREFERENCES",
    'status': 200
  }), 200

# CREATE
@user_prefs.route('/', methods=['POST'])
@login_required
def create_user_prefs():
  payload = request.get_json()
  print(payload)
  new_user_prefs = models.User_pref.create(
    name=payload['name'], 
    owner=current_user.id, 
    clean_pref=payload['clean_pref'],
    big_pref=payload['big_pref'],
    fenced_pref=payload['fenced_pref'],
    busy_pref=payload['busy_pref'],
    note=payload['note'],
  )
  print(dir(new_user_prefs))
  user_prefs_dict = model_to_dict(new_user_prefs)
  print(user_prefs_dict)
  user_prefs_dict['owner'].pop('password')

  return jsonify(
    data=user_prefs_dict, 
    message='Successfully CREATED USER PREFERENCES',
    status=201
  ), 201






