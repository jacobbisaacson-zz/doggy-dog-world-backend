from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('dogs.sqlite') 

class User(UserMixin, Model):
  username=CharField(unique=True)
  password=CharField()

  # name=CharField()
  # clean_pref=IntegerField()
  # big_pref=IntegerField()
  # fenced_pref=IntegerField()
  # busy_pref=IntegerField()
  # note=CharField()

  # NEED TO UPDATE THIS IN THE USER STUFF!!!!

  # email=CharField(unique=True)

  class Meta:
    database = DATABASE

class User_pref(Model):
  name=CharField()
  owner=ForeignKeyField(User, backref='user_prefs')
  clean_pref=IntegerField()
  big_pref=IntegerField()
  fenced_pref=IntegerField()
  busy_pref=IntegerField()
  note=CharField()

  class Meta:
    database = DATABASE

class Dog(Model):
  name=CharField()
  owner=ForeignKeyField(User, backref='dogs')
  breed=CharField()
  created_at=DateTimeField(default=datetime.datetime.now)
  image=CharField()
  # image=CharField()
  # have user type in img url (so string)

  class Meta: 
    database = DATABASE

class Park(Model):
  name=CharField()
  owner=ForeignKeyField(User, backref='parks')
  # park_creator=ForeignKeyField(User, backref='parks')
  location=CharField()
  clean=IntegerField()
  big=IntegerField()
  fenced=IntegerField()
  busy=IntegerField()
  # current_time=DateTimeField(default=datetime.datetime.now)

  class Meta: 
    database = DATABASE


def initialize():
  DATABASE.connect()

  DATABASE.create_tables([User, User_pref, Dog, Park], safe=True)
  print("CONNECTED to DB and CREATED (User, User_pref, Dog, Park) TABLES if they weren't already there")

  DATABASE.close()


