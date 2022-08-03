from flask_mongoengine import MongoEngine
from mongoengine import *

class Toy(Document):
    name = StringField()
