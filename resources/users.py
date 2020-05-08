import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', 'users')

# INDEX
@users.route('/', methods=['GET'])
def user_show():
  user_dict = model_to_dict(current_user)
  user_dict.pop('password')
  return jsonify({
    'data': user_dict,
    'message': "Successfully FOUND you, the USER",
    'status': 200
  }), 200

# # CREATE USER PROFILE
# @users.route('/', methods=['POST'])
# def create_user_profile():
#   dropdown_list = ['Name', 'Clean', 'Fenced', 'Busy', 'Big']
#   return 


# INDEX (single user - logged in) /api/v1/users
# @users.route('/', methods=['GET'])
# @login_required
# def user_index(): 
#   payload

  # return jsonify({
  #   'data': current_user_dicts,
  #   'message': f"Successfully FOUND {current_user_user_dicts} you, the USER",
  #   'status': 200
  # }), 200


# REGISTER
@users.route('/register', methods=['POST'])
def register():
  payload = request.get_json()
  # payload['email'] = payload['email'].lower()
  payload['username'] = payload['username'].lower()
  print(payload)

  try:
    models.User.get(models.User.username == payload['username'])
    return jsonify(
      data={},
      message=f"A user with the username {payload['username']} ALREADY EXISTS",
      status=401
    ), 401

  except models.DoesNotExist:
    pw_hash = generate_password_hash(payload['password'])
    created_user = models.User.create(
      username=payload['username'],
      # email=payload['email'],
      password=pw_hash
    )
    print(created_user)
    login_user(created_user)
    created_user_dict = model_to_dict(created_user)
    print(created_user_dict)   
    print(type(created_user_dict['password']))
    created_user_dict.pop('password')
    return jsonify(
      data=created_user_dict,
      message=f"Sucessfully REGISTERED user {created_user_dict['username']}",
      status=201
    ), 201


# LOGIN
@users.route('/login', methods=['POST'])
def login():
  payload = request.get_json()
  # payload['email'] = payload['email'].lower()
  payload['username'] = payload['username'].lower()
  try: 
    user = models.User.get(models.User.username == payload['username'])
    user_dict = model_to_dict(user)
    password_is_good = check_password_hash(user_dict['password'], payload['password'])
    if(password_is_good):
      login_user(user)
      print(model_to_dict(user))
      user_dict.pop('password')
      return jsonify(
        data=user_dict,
        message=f"Successfully LOGGED IN {user_dict['username']}",
        status=200
      ), 200

    else: 
      print('pw is no good')
      return jsonify(
        data={},
        message="Username or password is INCORRECT",
        status=401
      ), 401

  except models.DoesNotExist: 
    print('username is no good')
    return jsonify(
      data={},
      message="Username or password is INCORRECT",
      status=401
    ), 401

# ALL USERS
@users.route('/all', methods=['GET'])
def user_index():
  users = models.User.select()
  user_dicts = [ model_to_dict(user) for user in users ]
  for user_dict in user_dicts:
    user_dict.pop('password')
  print(user_dicts)
  return jsonify(user_dicts), 200


# LOGGED IN USER
@users.route('/logged_in_user', methods=['GET'])
def get_logged_in_user():
  print(current_user)
  print(type(current_user))
  if not current_user.is_authenticated: 
    return jsonify(
      data={},
      message="NO user is CURRENTLY LOGGED IN",
      status=401,
    ), 401

  else:
    user_dict = model_to_dict(current_user)
    user_dict.pop('password')
    return jsonify(
      data=user_dict,
      message=f"CURRENTLY LOGGED IN as {user_dict['username']}.",
      status=200
    ), 200


# LOG OUT
@users.route('/logout', methods=['GET'])
def logout(): 
  logout_user()
  return jsonify(
    data={},
    message="Successfully LOGGED OUT.",
    status=200
  ), 200



