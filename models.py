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

class Dog(Model):
  name=CharField()
  owner=ForeignKeyField(User, backref='dogs')
  breed=CharField()
  created_at=DateTimeField(default=datetime.datetime.now)
  # image=CharField()
  # have user type in img url (so string)

  class Meta: 
    database = DATABASE

class Park(Model):
  name=CharField()
  owner=ForeignKeyField(User, backref='parks')
  # park_creator=ForeignKeyField(User, backref='parks')
  # location=CharField() ********

  isClean=BooleanField(null = False)
  isBig=BooleanField(null = False)
  isFenced=BooleanField(null = False)
  isBusy=BooleanField(null = False)

  # current_time=DateTimeField(default=datetime.datetime.now)

  class Meta: 
    database = DATABASE


def initialize():
  DATABASE.connect()

  DATABASE.create_tables([User, Dog, Park], safe=True)
  print("CONNECTED to DB and CREATED (User and Dog and Park) TABLES if they weren't already there")

  DATABASE.close()


