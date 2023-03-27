#----------------------------------------------------------------------------#
# File: Annotations Controller
# Description: Manages all the routes and data for the Annotations table
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
import application.models.Annotation as Annotation


#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all annotations
# ----------------------------------------------------------
@app.route('/annotations', methods=['GET'])
def select_annotations_data():

    # try to find all annotations, except error.
    try:

        # use the function in Annotation model
        response = Annotation.select_annotations()

        # return the documents as the response
        return jsonify({"result":response})
    except:
        
        # error message as the result
        return jsonify({"result":"no data available"})



# Route to insert data in annotations table
# ----------------------------------------------------------------------
@app.route('/annotations', methods=['POST'])
def insert_annotations_data():
    try:
        # Get data in json format
        ann_id = request.json["ann_id"]
        corpus_id = request.json["corpus_id"]
        text_id = request.json["text_id"]
        ann_text = request.json["ann_text"]
        start_span = request.json["start_span"]
        end_span = request.json["end_span"]
        norm_id = request.json["norm_id"]
        attributes = request.json["attributes"]
        mark = request.json["mark"]

        # Use the function in model
        result = Annotation.insert_ann_data(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"insert okey", "response":result})
    except:
        
        return jsonify({"result":"error inserting data"})

# Tests
# URL: http://127.0.0.1:5000/annotations
# Method: POST

# JSON:
# {"ann_id":7,
# "corpus_id":1,
# "text_id":2,
# "ann_text":"ann43",
# "start_span":1,
# "end_span":3,
# "norm_id":2,
# "attributes":"attr1",
# "mark":"fefe"
# }


# Route to insert data in annotations table
# ----------------------------------------------------------------------
@app.route('/annotations/<string:id>', methods=['PUT'])
def update_annotations_data(id):

    try:
        # Get data in json format
        corpus_id = request.json["corpus_id"]
        text_id = request.json["text_id"]
        ann_text = request.json["ann_text"]
        start_span = request.json["start_span"]
        end_span = request.json["end_span"]
        norm_id = request.json["norm_id"]
        attributes = request.json["attributes"]
        mark = request.json["mark"]


        # Use the function in model
        result = Annotation.update_ann_data(id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data", "response":result})
    except:
        return  jsonify({"result":"no update"})

# Tests
# URL: http://127.0.0.1:5000/annotations/7

# JSON:
# {
# "corpus_id":1,
# "text_id":2,
# "ann_text":"ann7",
# "start_span":1,
# "end_span":3,
# "norm_id":2,
# "attributes":"attr1",
# "mark":"fefe"
# }


# Delete a document by id
# --------------------------------------------------------------------
@app.route("/annotations/<string:id>", methods=['DELETE'])
def delete_annotation_data(id):
    try:
        result = Annotation.delete_ann_data(id)
        
        # If the document was deleted, return succes message, else error message
        return jsonify({"result":"okey deleted"})
    except:
        return jsonify({"result":"error deleting"})

# Test
# http://127.0.0.1:5000/annotations/7