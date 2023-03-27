#----------------------------------------------------------------------------#
# File: Specialties Controller
# Description: Manages all the routes and data for the Specialties table
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
import application.models.Specialty as Specialty



#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all ontologies
# ----------------------------------------------------------
@app.route('/specialties', methods=['GET'])
def select_specialties_data():

    try:
        response = Specialty.select_specialties()

        # If the specialties are available, show them. Otherwise error message
        return jsonify({"result": "ok finding specialties", "response":response})
    
    except:

        return jsonify({"result":"no data available"})


# Route to select a specialty by id
# -------------------------------------------------------------
@app.route('/specialties/<string:id>', methods=['GET'])
def select_specialty_by_id(id):

    try:
        response = Specialty.select_where(id)

        # If the document data is available, return them
        return jsonify({"result": response})
    
    except:

        return jsonify({"result":"no data"})


# Route to insert data in specialties table
# ----------------------------------------------------------------------
@app.route('/specialties', methods=['POST'])
def insert_specialties_data():

    try:
        # Get data in json format
        specialty_id = request.json["specialty_id"]
        name = request.json["name"]
        description = request.json["description"]

        # Use the function in model
        result = Specialty.insert_spec_data(specialty_id, name, description)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})
    
    except:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/specialties
# Method: POST

# JSON:
# {
#   "specialty_id":6,
#   "name":"medicina_familiar",
#   "description":"about familiar medicine"
# }


# Route to insert data in specialties table
# ----------------------------------------------------------------------
@app.route('/specialties/<string:specialty_id>', methods=['PUT'])
def update_specialties_data(specialty_id):

    try:
        # Get data in json format
        name = request.json["name"]
        description = request.json["description"]

        # Use the function in model
        response = Specialty.update_spec_data(specialty_id,name, description)
    
        # If the update was successful, return the okey msg
        return jsonify({"result":"okey updating data","response":response})
    
    except:
        return  jsonify({"result":"no update"})

# Tests
# URL: 127.0.0.1:5000/specialties/6
# Method : POST

# JSON:
# {
#   "name":"medicina_externa",
#   "description":"about extern medicine"
# }


# Delete a specialty by id
# --------------------------------------------------------------------
@app.route("/specialties/<string:specialty_id>", methods=['DELETE'])
def delete_specialty_data(specialty_id):

    try:
        result = Specialty.delete_spec_data(specialty_id)
        
        # If the document was deleted, return succes message, else error message
        return jsonify({"result":"okey deleted"})
    
    except:
        return jsonify({"result":"error deleting"})

# Test with URL: http://127.0.0.1:5000/specialties/5


# Route to select specialties in document
# Return specialties.
# -----------------------------------------------------------------------
@app.route("/specialties-by-document/<string:textid>", methods=['GET'])
def select_specialties_documents(textid):
    '''
    Input parameters: text id to search the specialties of a specific document
    '''

    # Try to find all the specialties of a specific document, except error.
    try:

        # Use the function in Specialty Model
        result = Specialty.select_specialties_by_document(textid)

        # Return success message and the data found
        return jsonify({"result": "okey", "response":result})

    except:

        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/specialties-by-document/1
# 127.0.0.1:5000/specialties-by-document/5
# 127.0.0.1:5000/specialties-by-document/10

# Method GET