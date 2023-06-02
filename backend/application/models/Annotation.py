#----------------------------------------------------------------------------#
# File: Annotations Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 10/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from pathlib import Path
from application.config.database import get_connection # Import the database connection



# Function to select all annotations from the database
# --------------------------------------------------------------------------------
def select_annotations():
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from annotations")

    # fetchall and return the data
        data = cursor.fetchall()
        return data
    

# Function to select all annotations from the database of a specific document
# --------------------------------------------------------------------------------
def select_annotations_by_document(text_id):
    '''
    Input parameters: text_id id of the document
    '''
    # get connection    
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("select * from annotations where text_id = %s", text_id)

    # fetchall and return the data
        data = cursor.fetchall()
        return data


# Function to insert data in annotations table
# ---------------------------------------------------------------------------------
def insert_ann_data(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute query
        cursor.execute("INSERT INTO annotations(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark))
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")



# Function to update data in annotations table
# ---------------------------------------------------------------------------------
def update_ann_data(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark):
    '''Input parameters: data to insert in the table'''

    # get connection
    conexion = get_connection()

    data = ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark
    print(ann_id)

    # cursor
    with conexion.cursor() as cursor:

        # execute query
        cursor.execute("UPDATE annotations SET corpus_id = %s, text_id = %s, ann_text = %s, start_span = %s, end_span = %s, norm_id = %s, attributes = %s, mark = %s WHERE ann_id = %s",
                    (corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark, ann_id))
    
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) inserted")


# To delete data in annotations table
# ---------------------------------------------------------------------------------
def delete_ann_data(annid):
    '''Input parameter: the id of the corpus to delete'''

    # get connection
    connexion = get_connection()
    
    # cursor
    with connexion.cursor() as cursor:

        # execute command
        cursor.execute("DELETE FROM annotations WHERE ann_id = %s", annid)

    # commit and close
    connexion.commit()
    connexion.close



# Function to insert data in annotations table
# ---------------------------------------------------------------------------------
def insert_annzip_data(ann_data):
    '''Input parameters: data to insert in the table'''
    # for line in ann_data:
    #     print(line)

    # get connection
    conexion = get_connection()
    # cursor
    with conexion.cursor() as cursor:

        # execute query
        for line in ann_data:
            print(line)
            # print('ok')
            cursor.execute("INSERT INTO annotations(text_id, ann_text, start_span, end_span, attributes, mark) VALUES (%s, %s, %s, %s, %s, %s)",
            (line[5], line[1], line[2], line[3], line[4], line[0]))
            
                
    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")