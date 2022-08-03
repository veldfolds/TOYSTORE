from flask_mongoengine import MongoEngine
from mongoengine import *

#represents a specific toy on the shelf
class Toy(Document):
    name = StringField(),
    price = DecimalField(),
    image_url = StringField,
    year = DateField(),
    stock = IntField()
