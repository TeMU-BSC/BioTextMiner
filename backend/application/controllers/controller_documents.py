#----------------------------------------------------------------------------#
# File: Documents Controller
# Description: Manages all the routes and data for the Documents table
# Author : Siddique Muhammad
# Date: 08/05/2023
# Version: 1.9.
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

# Import modules
from ast import List
from collections import deque
from typing import Optional
from application import app
from flask import Flask,jsonify,request

# Import Model for documents, annotations, specialties
import application.models.Document as Document
import application.models.Annotation as Annotation
import application.models.Specialty as Specialty

# Os module
import os
import glob

# Zip File Extraction
from io import BytesIO
import zipfile
import tarfile
import rarfile

# Import ElasticSearch
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionTimeout

# Spacy
import spacy
from spacy import displacy

# Configparser settings
import configparser
parameters = config = configparser.ConfigParser()
parameters.read('./configuration.cfg')


#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to select all documents
# -------------------------------------------------------------
@app.route('/documents', methods=['GET'])
def select_documents_data():

    # try to find all documents, except error.
    try:

        # use the function in Document model
        response = Document.select_documents()

        # return the documents as the response
        return jsonify({"result": "ok finding documents", "response":response})
    
    except:

        # error message as the result
        return jsonify({"result":"no data available"})


# Route to select documents with optional search parameter
# -------------------------------------------------------------
@app.route('/api/documents', methods=['GET'])
def select_documents_dataa():
    search_term = request.args.get('search')
    try:
        # use the function in Document model with search term
        response = Document.select_document_byname(search_term)

        # return the documents as the response
        return jsonify({"result": "ok finding documents", "response": response})
    except:
        # error message as the result
        return jsonify({"result": "no data available"})



# Route to select a document by id
# -------------------------------------------------------------
@app.route('/documents/<string:id>', methods=['GET'])
def select_document_by_id(id):
    '''
    Input parameters: id of the document to find
    '''

    # try to select a document by id except error
    try:
        document = Document.select_where(id)

        # If the document data is available, return them
        return jsonify({"result": "ok finding documents","response":document})
    
    except:
        return jsonify({"result":"no data"})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/documents', methods=['POST'])
def insert_documents_data():

    # try to insert a document data, if not possible return an error message as a result
    try:
        # Get data in json format
        # text_id = request.json["text_id"] # id no hace falta en el form
        date = request.json["date"] # fecha de insertado, actual
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]
        text = request.json["text"] # en elastic search

        # Use the function in model
        result = Document.insert_doc_data(date, author, source, collection, language, text)

        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})
    
    except:
        return jsonify({"result":"error inserting data"})

# -------- For testing this route: -------
# URL: http://127.0.0.1:5000/documents
# Method: POST

# JSON example data:
# {
#   "text_id":5,
#   "date":"02",
#   "author":"bscsss",
#   "source":"web",
#   "collection":"cosssl2",
#   "language":"es"
# }
# -----------------------------------------


# Route to update data in documents table
# ----------------------------------------------------------------------
@app.route('/documents/<string:id>', methods=['PUT'])
def update_documents_data(id):
    '''
    Input parameters: id of the document to update
    '''

    # try to update a document's data except error
    try:

        # Get data in json format
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]

        # Use the function in model
        response = Document.update_doc_data(id, date, author, source, collection, language)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey updating data","response":response})
    
    except:
        return  jsonify({"result":"no update"})

# -------- For testing this route: -------
# URL: http://127.0.0.1:5000/documents/5
# Method: PUT

# JSON data:
# {
#   "date":"02",
#   "author":"bscsss",
#   "source":"web",
#   "collection":"cosssl2",
#   "language":"es"
# }
# -----------------------------------------


# Route to delete data in documents table
# --------------------------------------------------------------------
@app.route("/documents/<string:id>", methods=['DELETE'])
def delete_document_data(id):
    '''
    Input parameters: id of the document to delete
    '''

    # If the document was deleted, return succes message, else error message
    try:
        # Use the function in model
        result = Document.delete_doc_data(id)
        return jsonify({"result":"okey deleted"})
    
    except:
        return jsonify({"result":"no document deleted"})

# -------- For testing this route: -------
# Test with URL: http://127.0.0.1:5000/documents/5
# Method: PUT
# -----------------------------------------


# Route to select documents in corpus
# Return documents
# -----------------------------------------------------------------------
@app.route("/documents-by-corpus/<string:corpusid>", methods=['GET'])
def select_documents_corpus(corpusid):
    '''
    Input parameters: corpus id to search the documents of a specific corpus
    '''

    # Try to find all the documents of a specific corpus, except error.
    try:

        # Use the function in Document Model
        result = Document.select_documents_by_corpus(corpusid)

        # Return success message and the data found
        return jsonify({"result": "okey finding documents", "response":result})

    except:

        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/documents-by-corpus/13
# 127.0.0.1:5000/documents-by-corpus/14
# 127.0.0.1:5000/documents-by-corpus/222

# Method GET


# Route to select documents in specialty
# Return documents
# -----------------------------------------------------------------------
@app.route("/documents-by-specialty/<string:specialityid>", methods=['GET'])
def select_documents_specility(specialityid):
    '''
    Input parameters: specility id to search the documents of a specific specility
    '''

    # Try to find all the documents of a specific specility, except error.
    try:

        # Use the function in Document Model
        result = Document.select_documents_by_specialty(specialityid)

        # Return success message and the data found
        return jsonify({"result": "okey finding documents", "response":result})

    except:
    
        # If error, return error message
        return jsonify({"result":"no data found"})

# To test
# 127.0.0.1:5000/documents-by-specility/1
# 127.0.0.1:5000/documents-by-specility/2
# 127.0.0.1:5000/documents-by-specility/3

# Method GET


# -----------------------------------------------------------------------
# ZIP FILES MANAGEMENTS
# -----------------------------------------------------------------------
# Route to upload a zip file in the server
# -----------------------------------------------------------------------
@app.route('/upload', methods=['POST'])
def upload():

    # Get the file and read it
    file = request.files['file']
    file_data = file.read()

    # Determine the file type based on the file extension
    file_extension = file.filename.split('.')[-1].lower()
    
    # Extract the files based on the file type
    if file_extension == 'zip':
        with zipfile.ZipFile(BytesIO(file_data)) as zip_file:
            extract_files(zip_file)

    elif file_extension == 'tar':
        with tarfile.open(fileobj=BytesIO(file_data)) as tar_file:
            extract_files(tar_file)

    elif file_extension == 'rar':
        with rarfile.RarFile(BytesIO(file_data)) as rar_file:
            extract_files(rar_file)

    else:
        return 'Invalid file type'

    return 'Success!'


# Function to extract the file data and store in the database
# This function divides the files depending they are directories or files
# -----------------------------------------------------------------------
def extract_files(archive_file):



    # For each files in the files list
    for file_name in archive_file.namelist():

        # Testing filename
        if file_name.endswith('/'):
            manage_directory(file_name)

        else:
            manage_file(file_name, archive_file)



        # # If it is a directoy, manage the directory with a the "manage_directory" function.
        # if os.path.isdir(file_name):
        #     print('jjbjbjk')
        #     # Get the names and insert in database
        #     manage_directory(file_name)
            
        # # If it not a directory, manage with the "manage_file" function:
        # elif os.path.isfile(file_name):
        #     print('jjbjbjk')

        #     # Manage files. Annotations and txt
        #     manage_file(file_name, archive_file)


# Function to get data of the directories names and store in the database
# ---------------------------------------------------------------
def manage_directory(file_name):
    '''
    Input Parameters: The directory filename
    '''
    # Get specialty names
    names = os.path.split(file_name)

    # Use the function in specialty_model to insert the specialty name in the database
    # result = Specialty.insert_speczip_data(names)

    # return ('result')

    # print(name[0])


# Function to get data from the files
# -------------------------------------------------------------------------------------
def manage_file(file_name, archive_file):
    '''
    Input parameters: - The file name
                      - The archive file contains all the files (directory and subdirectories)
    '''



    # Split file name, 0 position is the directory and -1 position the file
    file = file_name.split("/")

    # Manage file depending on the file extension (txt or ann)
    if file_name.endswith('.txt'):
       
        # Insert data in Documents table and get id of the last insert
        txt_id = Document.insert_doc_name(file[-1])

        if len(txt_id)==0:
            message = 'Required already satisfied'

        else:
            # TXT ID
            # Convert id to str
            txt_id_str = "".join(str(x) for x in txt_id[0])

            # TXT DATA
            # Get data from txt files
            txt_data = manage_text(archive_file, file_name)

            # Convert to str
            txt_data2 = str(txt_data, 'UTF-8')

            # TXT NAME
            # Get document name
            txt_name = file[1]

            # INSERT DATA IN ELASTIC SEARCH
            result = manage_elastic(txt_id_str, txt_name, txt_data2, "yes")
    
        # Insert the documents names in the database
        # res = Document.insert_doczip_data(file[1])


    # If the file is an annotation file:
    if file_name.endswith('.ann'):
        file_name_only = (os.path.splitext(file_name)[0])
        new = (file_name_only + '.txt')

        isFile = os.path.isfile(new)

        not_included = []

        if(isFile)==False:
            not_included.append(file_name)



        # verificar, coger el nombre i verificar si 
        # print('-The file is an annotation file')

        # Get annotation data and insert
        ann_data = manage_annotations(archive_file, file_name)
        result = Annotation.insert_annzip_data(ann_data)

        # Insert the documents names in the database
        # res = Document.insert_doczip_data(file[1])

    # else:
    #     print('-The file is not valid for this action')



# Function to parse the txt files data
# --------------------------------------------------------------------------------------
def manage_text(archive_file, file_name):
    '''
    Manages the txt files, extract the data in these files
    - Input parameters: archive file is the file received
                        file name is the name of each file in the received folder 
    - Output parameters: data extracted from txt files.
    '''
    print('testtxt')
    # Open the archive file
    with archive_file.open(file_name) as file:

        # Read file data
        file_data = file.read()

        # Return the file data
        return file_data


# Function to parse the annotation files data
# --------------------------------------------------------------------------------------
def manage_annotations(archive_file, file_name):
    '''
    Manages the annotation files, extract the data in these files
    - Input parameters: archive file is the file received
                        file name is the name of all the files in the folder received
    - Output parameters: data extracted from annotation files.
    '''
    print(file_name)
    # Result: covid/32583150B_ES.ann
    file = file_name.split("/")
    print(file[1])
    # Result: 32583150B_ES.ann

    # Result that I want to pass: 32583150B_ES.txt

    file_name_without_extension = file[1].replace(".ann", ".txt")
    print(file_name_without_extension)
    # Result: 32583150B_ES.txt

    # Get the text_id of the document
    document_id = Document.select_documentid(file_name_without_extension)

    # corpus = {"labels":[]}
    print(document_id)

    # Open the archive file
    with archive_file.open(file_name) as file:
            
            # Readlines in the file
            file_data = file.readlines()
            result = []

            # For each line, split and save
            for lines in file_data:

                # Split lines with \t
                line = (lines.split(b'\t'))

                mark = line[0]

                text_span = line[1].split()
                ann_text = text_span[0]
                start_span = text_span[1]
                end_span = text_span[2]

                attributes = line[2]

                # Append the data in a list
                # data = mark, ann_text, start_span, end_span, attributes
                data = mark, ann_text, start_span, end_span, attributes, document_id

                result.append(data)
                # if ann_text not in corpus.labels:
                #     corpus.labels.append(ann_text)


            
            return result

# ------------------------- For testing zip file -------------------------
# Test in terminal
# curl -i -X POST -F name=prueba -F file=@file.zip "localhost:5000/upload"
# -----------------------------------------------------------------------


# -----------------------------------------------------------------------
# ELASTIC SEARCH 
# -----------------------------------------------------------------------
# Define the Elastic Search Client class
# -----------------------------------------------------------------------
def elastic():

    class ElasticsearchClient:
        def __init__(self) -> None:
            self._client: Optional[Elasticsearch] = None
            self.indices: List[str] = []

        @property
        def client(self) -> Elasticsearch:
            if self._client is None:
                self._client = Elasticsearch(parameters['elastic']['url'],basic_auth=(parameters['elastic']['user'], parameters['elastic']['password']))
            return self._client

        # def parallel_bulk(self, *args, **kwargs):
        #     """
        #     See https://elasticsearch-py.readthedocs.io/en/master/helpers.html#elasticsearch.helpers.parallel_bulk
        #     for details, this is just a wrapper method to unify the helper method and client.
        #     `parallel_bulk` returns a generator, need to `deque` it to consume.
        #     """
            
            # deque(_parallel_bulk(self.client, *args, **kwargs), maxlen=0)

    ec = ElasticsearchClient()

    return ec

# Function to insert data in ElasticSearch
# -----------------------------------------------------------------------
def manage_elastic(id, name, data, printed):

    # Define var
    ec = elastic()

    # Create index, with name "documents" if not exists
    # if ec.indices.exists("documents"):
    #     pass
    # else:
    #     ec.client.indices.create(index="documents", ignore=400)
    # ec.client.indices.create(index="documents", ignore=400)

    # Create dict
    mydict = {}

    # Add data to the dict
    mydict["id"] = id
    mydict["name"] = name
    mydict["data"] = data

    # Add data to index
    ec.client.index(index="documents",id=mydict["id"],document=mydict,)

    # print data, if required
    if printed == "yes":
        results = ec.client.search(index="documents", query={'match_all' : {}})
        print(results)   
    else:
        pass 


# ---------------------------- TODO -------------------------------------
# Route to search documents in ElasticSearch
# -----------------------------------------------------------------------
@app.route('/search-elastic', methods=['POST'])
def search():

    # keyword to search
    keyword = request.json['keyword']

    # If keyword is null, return error message. Else, search in elastic
    if keyword =='':
        return jsonify({'error': "No data received"}), 400
    else:
        result = search_in_elastic(keyword)
        return jsonify(result)


# Route to get document data by id
# -----------------------------------------------------------------------
@app.route('/search-document/<string:id>', methods=['GET'])
def search_document(id):
    try:
        document = get_document_from_elasticsearch(id)
        if document is not None:
            return jsonify(document)
        else:
            return jsonify({'error': 'Document not found'}), 404
    except Exception as e:
        error_message = "Error searching document in Elasticsearch: {}".format(str(e))
        return jsonify({'error': error_message}), 500



# Function to get document data in elasticsearch
# ------------------------------------------------------------------------
def get_document_from_elasticsearch(document_id):

    try:
        # Create Elasticsearch client
        ec = elastic()

        # Define the search query
        body = {
            "query": {
                "term": {
                "id": {
                    "value": document_id
                }
                }
            }
        }

        # Search for the document by ID
        res = ec.client.search(index="documents", body=body)


        # Get result
        hits = res['hits']['hits']
        result = [{'id': hit['_id'], 'data': hit['_source']['data'], 'name': hit['_source']['name']} for hit in hits]

        # Return the result in json format
        return (result)


    except Exception as e:
        # Handle any exceptions that occur during the search
        error_message = "Error retrieving document from Elasticsearch: {}".format(str(e))
        return None



# ---------------------------- TODO -------------------------------------
def search_in_elastic(keyword):

    try:

        # Define var for elasticsearch client
        ec = elastic()

        # body for the query
        # - start in the 45, skip the ones before that number
        # - picks the follwing 10
        # - query, with fuzzy (picks all the words that are similar)
        body = {
                "from": 45, 
                "size": 10,
                "query": {
                    "fuzzy": {
                    "data": {
                        "value": keyword
                    }
                    }
                }
                }

        # Response
        res = ec.client.search(index="documents", body=body)

        # To obtain all fields of hits
        # Return the result in json format
        # return jsonify(res['hits']['hits'])

        # To obtain only the id and the data
        hits = res['hits']['hits']
        result = [{'id': hit['_id'], 'data': hit['_source']['data'], 'name': hit['_source']['name']} for hit in hits]

        # Return the result in json format
        return (result)
        
    except ConnectionTimeout as e:
        # Send an error response to the frontend
        error_message = "Connection timeout to ElasticSearch: {}".format(str(e))
        return jsonify({'error': error_message}), 500


# ------------------------- TODO --------------------------------
# Function to obtain annotations of a document
@app.route('/annotations-by-document/<string:textid>', methods=['GET'])
def obtain_annotation(textid):
    '''
    Input parameters  : text_id the id of the documents
    Output parameters : annotations of that document
    '''
    result = Annotation.select_annotations_by_document(textid)

    return jsonify(result)

# 
def get_annotations(ids):
    pass

# Obtain annotations by doc
def annotations_by_doc(textid):
    result = Annotation.select_annotations_by_document(textid)

    return jsonify(result)


# ---------------------------- Functional -------------------------------------
# Search Route
# -----------------------------------------------------------------------------
@app.route('/search', methods=['POST'])
def searching():

    # Get the query
    query = request.json['query']

    # Data to pass
    results = ['caso_ontologia_45.txt', 'caso_clinico_20.txt', 'caso_ontologia_20.txt']

    # perform search operation using the query parameter
    filtered_results = [result for result in results if query in result]

    # Return filtered results according the searchin, json format
    return jsonify(filtered_results)



# -------------------------- SPACY / DISPLACY -----------------------------
# STEPS
# 1. Obtener el texto en elasticsearch a partir del textid 
# 2. Obtener anotaciones en la base de datos, a partir de la textid
# 3. Generar las anotaciones en el textoo

# Load model
nlp = spacy.load("es_core_news_sm")


# Route to display text with annotations.
# --------------------------------------------------------------
@app.route('/search-annotations/<string:id>', methods=['GET'])
def my_annotations(id):
    # Get data from elastic search
    data_elastic = get_document_from_elasticsearch(id)

    # Get text
    text = data_elastic[0]['data']


    # Get annotations of text
    result = Annotation.select_annotations_by_document(id)

    # Convert to entities
    entities = [(start_span, end_span, ann_text) for (_, _, _, ann_text, start_span, end_span, _, _, _) in result]

    annot = {
        "entities": entities
    }


    # Create doc object from text
    doc = nlp.make_doc(text) 
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")

        if span is not None:
            # span.style["background"] = "#aa9cfc"
            ents.append(span)
    
    # Label the text with the ents
    doc.spans["sc"] = ents 

    html = displacy.render([doc], style="span", options={"compact": True}) # Note the change here, passing a list with one document
    return html
    

    # To test: http://localhost:5000/anns