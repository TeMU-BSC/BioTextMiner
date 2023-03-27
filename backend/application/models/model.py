# # ------------------------ Model -----------------------------
# # Manages all the petitions from the server

# # Imports
# from pathlib import Path
# from application.config.database import get_connection # Import the database connection



# # Function to insert data in documents table
# # ---------------------------------------------------------------------------------
# def insert_doc_data(textid, date, author, source, collection, language):
#     '''Input parameters: data to insert in the table'''

#     # get connection
#     conexion = get_connection()

#     # cursor
#     with conexion.cursor() as cursor:

#         # execute command
#         cursor.execute("INSERT INTO documents(text_id, date, author, source, collection, language) VALUES (%s, %s, %s, %s, %s, %s)",
#                     (textid, date, author, source, collection, language))

#     # commit and close the connection
#     conexion.commit()
#     conexion.close()


# # Function to insert data in corpus table
# # ---------------------------------------------------------------------------------
# def insert_cor_data(corpus_id, corpus_name, labels, description, version, n_docs):
#     '''Input parameters: data to insert in the table'''

#     # get connection
#     conexion = get_connection()

#     # cursor
#     with conexion.cursor() as cursor:

#         # execute query
#         cursor.execute("INSERT INTO corpus(corpus_id, corpus_name, labels, description, version, n_docs) VALUES (%s, %s, %s, %s, %s, %s)",
#                     (corpus_id, corpus_name, labels, description, version, n_docs))
    
#     # commit and close the connection
#     conexion.commit()
#     conexion.close()


# # To delete data in documents table
# # ---------------------------------------------------------------------------------
# def delete_doc_data(textid):
#     '''Input parameter: the id of the document to delete'''

#     # get connection
#     connexion = get_connection()
    
#     # cursor
#     with connexion.cursor() as cursor:

#         # execute command
#         cursor.execute("DELETE FROM documents WHERE text_id = %s", textid)

#     # commit and close
#     connexion.commit()
#     connexion.close


# # To delete data in corpus table
# # ---------------------------------------------------------------------------------
# def delete_cor_data(corpusid):
#     '''Input parameter: the id of the document to delete'''

#     # get connection
#     connexion = get_connection()
    
#     # cursor
#     with connexion.cursor() as cursor:

#         # execute command
#         cursor.execute("DELETE FROM corpus WHERE corpus_id = %s", corpusid)

#     # commit and close
#     connexion.commit()
#     connexion.close


# # Tests
# # insert_doc_data('2', '2', 'bsc', 'web', 'col2', 'en')
# # delete_doc_data('1')