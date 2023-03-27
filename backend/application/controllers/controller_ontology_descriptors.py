#----------------------------------------------------------------------------#
# File: Ontology Descriptor Controller
# Description: Manages all the routes and data for the Ontology Descriptors table
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
import application.models.OntologyDescriptors as OntologyDescriptors

#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all ontology descriptors
# ----------------------------------------------------------
@app.route('/descriptors', methods=['GET'])
def select_descriptors_data():

    try:
        response = OntologyDescriptors.select_ontology_descriptors()

        # If the ontology codes are available, show them. Otherwise error message
        return jsonify({"result": "ok finding ontology desciptors", "response":response})
    
    except:
        return jsonify({"result":"no data available"})
    # return jsonify({"result":c})


# Route to select a ontology descriptor by id
# -------------------------------------------------------------
@app.route('/descriptors/<string:ontology_id>', methods=['GET'])
def select_descriptor_by_id(ontology_id):

    try:
        result = OntologyDescriptors.select_where(ontology_id)

        # If the document data is available, return them
        return jsonify({"result": result})

    except:
        
        return jsonify({"result":"no data"})


# Route to insert data in ontology descriptors table
# ----------------------------------------------------------------------
@app.route('/descriptors', methods=['POST'])
def insert_descriptors_data():

    try:
        # Get data in json format
        code_id = request.json["code_id"]
        descriptor_id = request.json["descriptor_id"]
        ontology_id = request.json["ontology_id"]
        descriptor = request.json["descriptor"]
        semantic_label = request.json["semantic_label"]
        language = request.json["language"]
        term_type = request.json["term_type"]
        
        data = code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type

        print(data)

        # Use the function in model
        result = OntologyDescriptors.insert_ont_desc_data(code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})

    except:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/descriptors
# Method: POST

# JSON:
# {
#   "code_id":"6",
#   "descriptor_id":"6",
#   "ontology_id":"6",
#   "descriptor": "desc006",
#   "semantic_label":"label06",
#   "language":"es",
#   "term_type":"type06"
# }


# Route to insert data in ontologies table 
# ----------------------------------------------------------------------
@app.route('/descriptors/<string:code_id>', methods=['PUT'])
def update_descriptor_data(code_id):

    try:
        # Get data in json format
        descriptor_id = request.json["descriptor_id"]
        ontology_id = request.json["ontology_id"]
        descriptor = request.json["descriptor"]
        semantic_label = request.json["semantic_label"]
        language = request.json["language"]
        term_type = request.json["term_type"]

        # Use the function in model
        response = OntologyDescriptors.update_ont_desc_data(code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data","response":response})
    
    except:
        return  jsonify({"result":"no update"})

# Tests
# URL: http://127.0.0.1:5000/descriptors/6
# Method : PUT

# JSON:
# {
#   "descriptor_id":"6",
#   "ontology_id":"6",
#   "descriptor": "desc06",
#   "semantic_label":"label06",
#   "language":"es",
#   "term_type":"type06"
# }


# Delete a ontology descriptor by id
# --------------------------------------------------------------------
@app.route("/descriptors/<string:code_id>", methods=['DELETE'])
def delete_descriptor_data(code_id):

    try:
        result = OntologyDescriptors.delete_ont_desc_data(code_id)
    
        # If the ontology was deleted, return succes message, else error message
        return jsonify({"result":"okey deleted"})

    except:
        return jsonify({"result":"error deleting"})

# Test with URL: http://127.0.0.1:5000/descriptors/6
# Method : DELETE


# Route to select ontologies in ontology_descriptors
# Return ontologies
# -----------------------------------------------------------------------
@app.route("/descriptors-by-ontology/<string:ontologyid>", methods=['GET'])
def select_descriptors_ontology(ontologyid):
    '''
    Input parameters: ontology_id to search the ontology descriptors of a specific ontology
    code_id is the identifier of a ontology
    '''

    # Try to find all the ontologies of a specific descriptor, except error.
    try:

        # Use the function in Ontology Model
        result = OntologyDescriptors.select_descriptors_by_ontology(ontologyid)

        # Return success message and the data found
        return jsonify({"result": "okey finding ontology_descriptors", "response":result})

    except:

        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/descriptors-by-ontology/1
# 127.0.0.1:5000/descriptors-by-ontology/2
# 127.0.0.1:5000/descriptors-by-ontology/4

# Method GET