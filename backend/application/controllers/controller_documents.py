#----------------------------------------------------------------------------#
# File: Documents Controller
# Description: Manages all the routes and data for the Documents table
# Author : Siddique Muhammad
# Date: 13/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

# Import Flask modules
from application import app
from flask import Flask,jsonify,request

# Import Model for documents, annotations, specialties
import application.models.Document as Document
import application.models.Annotation as Annotation
import application.models.Specialty as Specialty

# Os module
import os

# Zip File Extraction
from io import BytesIO
import zipfile
import tarfile
import rarfile


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
        text_id = request.json["text_id"]
        date = request.json["date"]
        author = request.json["author"]
        source = request.json["source"]
        collection = request.json["collection"]
        language = request.json["language"]

        # Use the function in model
        result = Document.insert_doc_data(text_id, date, author, source, collection, language)
    
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
# -----------------------------------------------------------------------
def extract_files(archive_file):
    # print(archive_file.namelist())

    # For files in a directory
    for file_name in archive_file.namelist():
        # print(file_name)

        # Check if the file is a directory or not
        if os.path.isdir(file_name):

            # Get the names and insert in database
            manage_directory(file_name)
            
        # If it not a directory, get data from this files and insert:
        elif os.path.isfile(file_name):

            # Manage files. Annotations and txt
            manage_file(file_name, archive_file)




# Function to get data of the directoires and store in the database
# ---------------------------------------------------------------
def manage_directory(file_name):
    print('The file is a directory')

    # Get specialty names
    names = os.path.split(file_name)

    # Use the function in specialty_model to insert the specialty name in the database
    # result = Specialty.insert_speczip_data(names)

    # return ('result')

    # print(name[0])


# Function to get data from the directories
# -------------------------------------------------------------------------------------
def manage_file(file_name, archive_file):

    print(' ')
    print('This is a file')

    file = file_name.split("/")


    # Check if the file is a txt or ann:
    # If the file is a txt:
    if file_name.endswith('.txt'):
        print('-The file is a txt file')

        # Get data from txt files
        txt_data = manage_text(archive_file, file_name)
        # print(txt_data)

        # Insert the documents names in the database
        res = Document.insert_doczip_data(file[1])

    # If the file is an annotation file:
    elif file_name.endswith('.ann'):
        print('-The file is an annotation file')

        # Get annotation data and insert
        ann_data = manage_annotations(archive_file, file_name)
        result = Annotation.insert_annzip_data(ann_data)

        # To check
        # print(ann_data[0:5])

        # Insert the documents names in the database
        res = Document.insert_doczip_data(file[1])

    else:
        print('-The file is not valid for this action')



# Function to parse the txt files data
# --------------------------------------------------------------------------------------
def manage_text(archive_file, file_name):
    '''
    Manages the txt files, extract the data in these files
    - Input parameters: archive file is the file received
                        file name is the name of all the files in the folder received
    - Output parameters: data extracted from txt files.
    '''
    
    # Open the archive file
    with archive_file.open(file_name) as file:

        # Read file data
        file_data = file.read()

        # Return the file data
        return file_data


# Function to parse the txt files data
# --------------------------------------------------------------------------------------
def manage_annotations(archive_file, file_name):
    '''
    Manages the annotation files, extract the data in these files
    - Input parameters: archive file is the file received
                        file name is the name of all the files in the folder received
    - Output parameters: data extracted from annotation files.
    '''

    file = file_name.split("/")
    
    # Get the text_id of the document
    document_id = Document.select_documentid(file[1])

    # print(document_id)

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
                text_id = document_id

                # Append the data in a list
                # data = mark, ann_text, start_span, end_span, attributes
                data = mark, ann_text, start_span, end_span, attributes, text_id

                result.append(data)

                # To check
                # print(result)
            
            return result

# ------------------------- For testing zip file -------------------------
# Test in terminal
# curl -i -X POST -F name=prueba -F file=@file.zip "localhost:5000/upload"