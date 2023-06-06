#----------------------------------------------------------------------------#
# File: Document Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 21/02/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from pathlib import Path

# Import the database connection configuration
from application.config.database import get_connection 


# Function to select all documents from the database
# --------------------------------------------------------------------------------
def select_documents():

    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from documents")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select documents from the database with optional search term
# --------------------------------------------------------------------------------
def select_document_byname(search_term=None):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:
        if search_term:
            # execute command with search term
            cursor.execute("SELECT * FROM documents WHERE name LIKE %s", (f"%{search_term}%",))
        else:
            # execute command without search term
            cursor.execute("SELECT * FROM documents")

        # fetchall and return the data
        data = cursor.fetchall()
        return data


# Function to select a document by id
# --------------------------------------------------------------------------------
def select_where(textid:str):
    '''
    Input parameters: 
                    textid: id of the document to find
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM documents WHERE text_id = %s", textid)

    # commit and close the connection
        data = cursor.fetchall()
        return data


# Function to insert data in documents table
# ---------------------------------------------------------------------------------
def insert_doc_data(textid:str, date:str, author:str, source:str, collection:str, language:str):
    '''
    Input parameters: 
                    text id: id of the document to insert
                    date: date of the document
                    author : the author
                    source: source of the document
                    collection: collection of the document
                    langauge: in which language the document is
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO documents(text_id, date, author, source, collection, language) VALUES (%s, %s, %s, %s, %s, %s)",
                    (textid, date, author, source, collection, language))


    #gestionar elastic search. obtener id del ultimo insert
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")


# Function to update data in documents table
# ---------------------------------------------------------------------------------
def update_doc_data(textid:str, date:str, author:str, source:str, collection:str, language:str):
    '''
    Input parameters: 
                    text id: id of the document to update
                    date: date of the document
                    author : the author
                    source: source of the document
                    collection: collection of the document
                    langauge: in which language the document is
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE documents SET date=%s, author=%s, source=%s, collection=%s, language=%s WHERE text_id=%s",
                    (date, author, source, collection, language, textid))

    # commit and return a message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")



# To delete data in documents table
# ---------------------------------------------------------------------------------
def delete_doc_data(textid):
    '''Input parameter: the id of the document to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM documents WHERE text_id = %s", textid)

    # commit and close connection
    connexion.commit()
    connexion.close

# To select documents data by corpus id
# ---------------------------------------------------------------------------------
def select_documents_by_corpus(corpusid):
    '''
    Input parameters: corpus id to search the documents of a specific corpus
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from documents JOIN document_corpus ON documents.text_id =  document_corpus.text_id WHERE document_corpus.corpus_id=%s", corpusid)

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# To select documents data by specility id
# ---------------------------------------------------------------------------------
def select_documents_by_specialty(specialityid):
    '''
    Input parameters: speciality id to search the documents of a specific specility
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from documents JOIN document_specialties ON documents.text_id =  document_specialties.text_id WHERE document_specialties.specialty_id=%s", specialityid)

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to insert data in documents table
# ---------------------------------------------------------------------------------
def insert_doczip_data(name:str):
    '''
    Input parameters: 
        name: name of the document
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command

        # Check if the document exists in the database
        cursor.execute("SELECT text_id FROM documents WHERE name = %s", name)
        resultado = cursor.fetchone()

        # If the result is None, means that there is no document with this name stored in the database.
        if resultado is None:
            message = "Database messsage : The document does not exist in the database"

            # Execute insert command to insert the document if not exists
            if name.endswith('txt') or name.endswith('ann'):
                cursor.execute("INSERT INTO documents(name) VALUES (%s)",(name))
            else:
                message = 'Database message : The file extension is not txt or ann.'

        else:
            message = "Database messsage : The document already exists in the database"
            

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated", message)




# Function to select document id by name
# --------------------------------------------------------------------------------
def select_documentid(name:str):
    '''
    Input parameters: 
        name: name of the document to find
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT text_id FROM documents WHERE name = %s", name)
        
    # commit and close the connection
        data = cursor.fetchall()
        return data




# Function to insert data in documents table
# ---------------------------------------------------------------------------------
def insert_doc_name(name:str):
    '''
    Input parameters: 
        name: name of the document
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        # Check if the document exists in the database
        cursor.execute("SELECT text_id FROM documents WHERE name = %s", name)
        result = cursor.fetchone()

        # If the result is None, means that there is no document with this name stored in the database.
        if result is None:
            # print("Database messsage : The document does not exist in the database")

            # Execute insert command to insert the document if not exists
            if name.endswith('txt'):
                cursor.execute("INSERT INTO documents(name) VALUES (%s)",(name))

                # Get the id of the last insert.
                cursor.execute("SELECT LAST_INSERT_ID()")

            else:
                message = 'Database message : The file extension is not txt.'
                
        else:
            message = "Database messsage : The document already exists in the database"
            

    # commit and return message
    conexion.commit()
    data = cursor.fetchall()

    # if len(data) == 0:
    #     print("No se encontraron filas.")
    # else:
    #     print("Se encontraron filas.")

    return data
    #return(str(cursor.rowcount)+ " record(s) updated")



# Documents by corpus:
# Get documents by a specific corpus
# Dashboard table
# --------------------------------------------------------------------
def select_txt_by_corpus(corpusid):
    '''
    Input parameters: corpus id to search the documents of a specific corpus
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT d.* FROM documents AS d JOIN document_corpus AS dc ON d.text_id = dc.text_id WHERE dc.corpus_id=%s", corpusid)

    # fetchall and return the data
        data = cursor.fetchall()
        return data