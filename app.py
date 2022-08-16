import json
from flask import make_response
from flask import Flask, request
import flask
from flask_pymongo import PyMongo
from cataloguerepo.models import toys_list


app = Flask(__name__)
#substite you own connection string
mongo_client = PyMongo(app, "https://localhost:<port>")

db = mongo_client.db

@app.route("/toys", methods=["GET"])
def getcatalogue():
    """get all toys listed in the catalogue"""
    catalogue = db.toys.find()

    #seed the db if nothing exists so all you need to do
    #is to ensure your database has a toys collection and the rest
    #will be taken care of
    if catalogue == "":
        db.toys.insert_many(toys_list)

    return flask.jsonify([toy for toy in catalogue])

@app.route("/toys", methods=["POST"])
def addtocatalogue():
    """add a toy to the catalogue"""
    body = request.json()
    toys = json.loads(body)
    created_ids = db.catalogue.insert_many(toys).inserted_ids()

    return make_response(json.dumps(created_ids), 201)

@app.route("/toys/<id>", methods=["DELETE"])
def removefromcatalogue(id):
    """remove toys from the catalogue"""
    deleted = db.catalogue.delete_one('{_id:')

    return make_response(json.dumps(deleted), 204)

#not yet implemented
@app.route("/toys/<id>", methods=["PUT"])
def updatecatalogue(id):
    """update a toy listed in the catalogue"""

    return 204
