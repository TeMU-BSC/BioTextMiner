#----------------------------------------------------------------------------#
# File: Corpus Controller
# Description: Manages all the routes and data for the Corpus table
# Author : Siddique Muhammad
# Date: 13/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import Model for corpus
import application.models.Corpus as Corpus
import application.models.Document as Document


#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all corpus
# -------------------------------------------------------------
@app.route('/corpus', methods=['GET'])
def select_corpus_data():

    # try to find all corpus, except error.
    try:

        # use the function in Corpus model
        response = Corpus.select_corpus()

        # return the corpus as the response
        return jsonify({"result": "ok finding corpus", "response":response})
    
    except:
        
        # error message as the result
        return jsonify({"result":"no data available"})


# Route to select top coprus by id
# -------------------------------------------------------------
@app.route('/corpus_top', methods=['GET'])
def select_corpus_top():

    # try to find all corpus, except error.
    try:

        # use the function in Corpus model
        response = Corpus.select_corpus_top()

        # return the corpus as the response
        return jsonify({"result": "ok finding corpus", "response":response})
    
    except:
        
        # error message as the result
        return jsonify({"result":"no data available"})
        


# Route to select a coprus by id
# -------------------------------------------------------------
@app.route('/corpus/<string:id>', methods=['GET'])
def select_corpus_by_id(id):
    # text_id = request.json["text_id"]

    c = Corpus.select_where(id)

    # If the document data is available, return them
    if c!=None:
        return jsonify({"result": c})
    else:
        
        return jsonify({"result":"no data"})



# Route to insert data in corpus table
# ----------------------------------------------------------------------
@app.route('/corpus', methods=['POST'])
def insert_corpus_data():

    # try to insert a corpus data, if not possible return an error message as a result

    try:
        # Get data in json format
        corpus_name = request.json["corpus_name"]
        labels = request.json["labels"]
        description = request.json["description"]
        version = request.json["version"]

        # Use the function in model
        result = Corpus.insert_cor_data(corpus_name, labels, description, version)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})
    
    except:
        
        return jsonify({"result":"error inserting data"})


# -------- For testing this route: -------
# URL: http://127.0.0.1:5000/corpus
# Method: POST

# {
#   "corpus_name":"corpus_dishf",
#   "labels":"label11",
#   "description":"Corpus description",
#   "version":"2.0"
# }
# -----------------------------------------


# Route to update data in corpus table. 
# ----------------------------------------------------------------------
@app.route('/corpus/<string:corpus_id>', methods=['PUT'])
def update_corpus_data(corpus_id):
    '''
    Input parameters: id of the corpus to update
    '''

    try:
        # Get data in json format
        corpus_name = request.json["corpus_name"]
        labels = request.json["labels"]
        description = request.json["description"]
        version = request.json["version"]
        n_docs = request.json["n_docs"]

        # Use the function in model
        response = Corpus.update_cor_data(corpus_id, corpus_name, labels, description, version, n_docs)
        
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data","response":response})
    
    except:
        return  jsonify({"result":"no update"})
    

# -------- For testing this route: -------
# URL: http://127.0.0.1:5000/corpus/12
# Method = PUT

# {
#   "corpus_name":"deede",
#   "labels":"label11",
#   "description":"Corpus description",
#   "version":"2.0",
#   "n_docs":"2"
# }
# -----------------------------------------


# Route to delete data in corpus table
# --------------------------------------------------------------------
@app.route("/corpus/<string:corpusid>", methods=['DELETE'])
def delete_corpus_data(corpusid):
    '''
    Input parameters: id of the corpus to delete
    '''

    # If the corpus was deleted, return succes message, else error message
    try:
        # Use the function in model
        result = Corpus.delete_cor_data(corpusid)
        return jsonify({"result":"okey deleted"})
    
    except:
        return jsonify({"result":"no document deleted"})
    


# Route to select corpus in document
# Return corpus.
# -----------------------------------------------------------------------
@app.route("/corpus-by-document/<string:textid>", methods=['GET'])
def select_corpus_documents(textid):
    '''
    Input parameters: text id to search the corpus of a specific document
    '''

    # Try to find all the documents of a specific corpus, except error.
    try:

        # Use the function in Corpus Model
        result = Corpus.select_corpus_by_document(textid)

        # Return success message and the data found
        return jsonify({"result": "okey finding corpus", "response":result})

    except:

        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/corpus-by-document/1
# 127.0.0.1:5000/corpus-by-document/10
# 127.0.0.1:5000/corpus-by-document/2

# Method 






# Route to select a coprus by id
# -------------------------------------------------------------
@app.route('/corpus_data/<string:id>', methods=['GET'])
def corpus_data(id):
    # text_id = request.json["text_id"]

    corpus_data = Corpus.select_where(id)

    documents_data = Document.select_txt_by_corpus(id)

    # If the document data is available, return themm
    if corpus_data!=None:
        return jsonify({"result": corpus_data, "resultdoc" : documents_data})
    else:
        
        return jsonify({"result":"no data"})