from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('dogs.sqlite') 

class User(UserMixin, Model):
  username=CharField(unique=True)
  password=CharField()
  name=CharField()
  clean_pref=IntegerField()
  big_pref=IntegerField()
  fenced_pref=IntegerField()
  busy_pref=IntegerField()
  note=CharField()

  # email=CharField(unique=True)

  class Meta:
    database = DATABASE

class Dog(Model):
  name=CharField()
  owner=ForeignKeyField(User, backref='dogs')
  breed=CharField()
  created_at=DateTimeField(default=datetime.datetime.now)
  # image?

  class Meta: 
    database = DATABASE

class Park(Model):
  name=CharField()

  # location=CharField() ********
  isClean=BooleanField(default=False, required=True)
  isBig=BooleanField(default=False, required=True)
  isFenced=BooleanField(default=False, required=True)
  isBusy=BooleanField(default=False, required=True)
  current_time=DateTimeField(default=datetime.datetime.now)


  # do i give these integers?  and then the drop down selection refers to a number?


def initialize():
  DATABASE.connect()

  DATABASE.create_tables([User, Dog], safe=True)
  print("CONNECTED to DB and CREATED (User and Dog) TABLES if they weren't already there")

  DATABASE.close()


