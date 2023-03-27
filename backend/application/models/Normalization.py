#----------------------------------------------------------------------------#
# File: Normalization Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 10/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from pathlib import Path
from application.config.database import get_connection # Import the database connection


# Function to select all documents from the database
# --------------------------------------------------------------------------------
def select_normalizations():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from normalizations")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select a normalization by id
# --------------------------------------------------------------------------------
def select_where(norm_id):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM normalizations WHERE norm_id = %s", norm_id)

    # commit and close the connection
        data = cursor.fetchall()
        return data


# Function to insert data in documents table
# ---------------------------------------------------------------------------------
def insert_norm_data(norm_id, ontology_id, code_id, semantic_relation):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO normalizations(norm_id, ontology_id, code_id, semantic_relation) VALUES (%s, %s, %s, %s)",
                    (norm_id, ontology_id, code_id, semantic_relation))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")


def update_norm_data(norm_id, ontology_id, code_id, semantic_relation):

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE normalizations SET ontology_id=%s, code_id=%s, semantic_relation=%s WHERE norm_id=%s",
                    (ontology_id, code_id, semantic_relation, norm_id))

    # commit and close the connection
    conexion.commit()
    print(cursor.rowcount, "record(s) updated")
    return cursor.rowcount
    # conexion.close()


# To delete data in documents table
# ---------------------------------------------------------------------------------
def delete_norm_data(norm_id):
    '''Input parameter: the id of the normalization to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM normalizations WHERE norm_id = %s", norm_id)

    # commit and close
    connexion.commit()
    connexion.close