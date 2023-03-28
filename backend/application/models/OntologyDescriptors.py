#----------------------------------------------------------------------------#
# File: Ontology Descriptor Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 16/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from pathlib import Path
from application.config.database import get_connection # Import the database connection


# Function to select all ontology_descriptors from the database
# --------------------------------------------------------------------------------
def select_ontology_descriptors():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from ontology_descriptors")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select a ontology descriptor by id
# --------------------------------------------------------------------------------
def select_where(descriptor_id):
    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("SELECT * FROM ontology_descriptors WHERE descriptor_id = %s", descriptor_id)

    # commit and close the connection
        data = cursor.fetchall()
        return data


# Function to insert data in ontology descriptors table
# ---------------------------------------------------------------------------------
def insert_ont_desc_data(code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO ontology_descriptors(code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")


# Function to update data in ontology descriptors table
# ---------------------------------------------------------------------------------
def update_ont_desc_data(code_id, descriptor_id, ontology_id, descriptor, semantic_label, language, term_type):

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("UPDATE ontology_descriptors SET descriptor_id = %s, ontology_id=%s, descriptor=%s, semantic_label=%s, language=%s, term_type=%s WHERE code_id=%s",
                    (descriptor_id, ontology_id, descriptor, semantic_label, language, term_type, code_id))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")


# To delete data in ontology_descriptors table
# ---------------------------------------------------------------------------------
def delete_ont_desc_data(code_id):
    '''Input parameter: the id of the ontology descriptor to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM ontology_descriptors WHERE code_id = %s", code_id)

    # commit and close
    connexion.commit()
    connexion.close


# To select ontology_descriptors data by ontology_id
# ---------------------------------------------------------------------------------
def select_descriptors_by_ontology(ontologyid):
    '''
    Input parameters: ontology id (identifier of ontology) to search the descriptors of a specific ontology
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from ontology_descriptors JOIN ontology_ontology_descriptors ON ontology_descriptors.code_id =  ontology_ontology_descriptors.code_id WHERE ontology_ontology_descriptors.ontology_id=%s", ontologyid)

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to insert data in ontology descriptors table
# ---------------------------------------------------------------------------------
def insert_tsv_data(data):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # For each row:
        for line in data:

        # execute command inserting data
            cursor.execute("INSERT INTO ontology_descriptors(descriptor_id, ontology_id, descriptor, semantic_label, language, term_type) VALUES (%s, %s, %s, %s, %s, %s)", (line[0], line[1], line[2], line[3], line[4], line[5]))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")