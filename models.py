from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('users.sqlite')

class User(UserMixin, Model):
	username=CharField(unique=True)
	email=CharField(unique=True)
	password=CharField()

	class Meta:
		database = DATABASE

def initialize():
	DATABASE.connect()

	DATABASE.create_tables([User], safe=True)
	print("CONNECTED TO DB AND CREATED TABLES IF THEY WEREN'T ALREADY THERE")

	DATABSE.close()