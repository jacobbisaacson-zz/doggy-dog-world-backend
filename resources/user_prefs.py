import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

user_prefs = Blueprint('user_prefs', 'user_prefs')

# TEST
@user_prefs.route('/')
def user_prefs_index():
  return "user_prefs resource working"