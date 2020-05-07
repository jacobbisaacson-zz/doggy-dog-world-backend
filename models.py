from peewee import *
import datetime
# from flask_login import UserMixin

DATABASE = SqliteDatabase('dogs.sqlite') 

class Dog(Model):
  name = CharField()
  owner = CharField()
  breed = CharField()
  created_at: DateTimeField(default=datetime.datetime.now)

  class Meta: 
    database = DATABASE 

def initialize():
  DATABASE.connect()

  DATABASE.create_tables([Dog], safe=True)
  print("CONNECTED to DB and CREATED TABLES if they weren't already there")

  DATABASE.close()