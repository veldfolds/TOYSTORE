from http.client import CREATED, NO_CONTENT, OK
from flask import Flask
from cataloguerepo.models import Toy

app = Flask(__name__)


@app.route("/catalogue", methods=["GET"])
def getcatalogue():
    """get all toys listed in the catalogue"""
    return OK

@app.route("/catalogue", methods=["POST"])
def addtocatalogue():
    """add a toy to the catalogue"""
    return CREATED

@app.route("/catalogue/<id>", methods=["DELETE"])
def removefromcatalogue(id):
    """remove toys from the catalogue"""
    return NO_CONTENT

@app.route("/catalogue", methods=["PUT"])
def updatecatalogue():
    """update a toy listed in the catalogue"""
    return NO_CONTENT



