from flask_mongoengine import MongoEngine
from mongoengine import *

db = MongoEngine()
#represents a specific toy on the shelf
class Toy(Document):
    name = StringField(max_length=20, min_length=1),
    company = StringField(),
    price = DecimalField(min_value=1),
    image_url = StringField(),
    year = DateField(),
    stock = IntField()
