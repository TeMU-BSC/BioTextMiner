#----------------------------------------------------------------------------#
# File: Normalizations Controller
# Description: Manages all the routes and data for the Normalizations table
# Author : Siddique Muhammad
# Date: 13/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import documents model
from application.models import Normalization


#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all normalizations
# -------------------------------------------------------------
@app.route('/normalizations', methods=['GET'])
def select_normalizations_data():

    # try to find all normalizations, except error.
    try:
        response = Normalization.select_normalizations()

        # If the normalizations are available, show them. Otherwise error message
        return jsonify({"result": "ok finding normalizations", "response":response})
    
    except:
        return jsonify({"result":"no data available"})


# Route to select a normalization by id
# -------------------------------------------------------------
@app.route('/normalizations/<string:id>', methods=['GET'])
def select_normalization_by_id(id):

    try:
        result = Normalization.select_where(id)

    # If the normalization data is available, return them
        return jsonify({"result":"okey finding data", "response":result})
    
    except:

        return jsonify({"result":"no data"})


# Route to insert data in normalizations table
# ----------------------------------------------------------------------
@app.route('/normalizations', methods=['POST'])
def insert_normalizations_data():

    try:
        # Get data in json format
        norm_id = request.json["norm_id"]
        ontology_id = request.json["ontology_id"]
        code_id = request.json["code_id"]
        semantic_relation = request.json["semantic_relation"]

        # Use the function in model
        result = Normalization.insert_norm_data(norm_id, ontology_id, code_id, semantic_relation)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})
    
    except:

        return jsonify({"result":"okey"})

# Tests
# URL: http://127.0.0.1:5000/normalizations
# Method: POST

# JSON:
# {
#    "norm_id":7,
#    "ontology_id":5,
#    "code_id":"1",
#    "semantic_relation":"ceevklen"
#  }


# Route to update data in normalizations table 
# ----------------------------------------------------------------------
@app.route('/normalizations/<string:norm_id>', methods=['PUT'])
def update_normalizations_data(norm_id):

    try:
        # Get data in json format
        ontology_id = request.json["ontology_id"]
        code_id = request.json["code_id"]
        semantic_relation = request.json["semantic_relation"]

    # Use the function in model
        result = Normalization.update_norm_data(norm_id, ontology_id, code_id, semantic_relation)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data"})
    
    except:
        return  jsonify({"result":"no update"})

# Tests
# URL: http://127.0.0.1:5000/normalizations/7

# JSON:
# {
#    "ontology_id":6,
#    "code_id":"1",
#    "semantic_relation":"ceevklen"
#  }


# Delete a normalization by id
# --------------------------------------------------------------------
@app.route("/normalizations/<string:norm_id>", methods=['DELETE'])
def delete_normalization_data(norm_id):

    try:
        result = Normalization.delete_norm_data(norm_id)
    
        # If the normalization was deleted, return succes message, else error message
        return jsonify({"result":"okey deleting data"})
    except:
        return  jsonify({"result":"no normalization deleted"})

# Test with URL: http://127.0.0.1:5000/normalization/7
# Method : DELETE