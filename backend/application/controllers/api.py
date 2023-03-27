# ########################################################################
# ##################### CRUD APP WITH MYSQL DATABASE #####################
# ########################################################################

# ########################################################################
# # Author : Siddique
# # Date : 16/02/2023
# ########################################################################

# # Import Flask modules
# from application import app
# from flask import Flask,jsonify,request

# # import model
# import application.models.model as model
# # from application.models.model import *

# # app Flask, initialize
# # app = Flask(__name__)

# # model = Control()

# try:
#     # Proves
#     # ---------------------------------------------
#     @app.route('/hello')  # Method Get
#     def hello():
#         return jsonify("Hello, world!")


#     # Route to insert data in documents table
#     # ----------------------------------------------------------------------
#     @app.route('/insert_documents_data', methods=['POST'])
#     def insert_documents_data():

#         # Get data in json format
#         text_id = request.json["text_id"]
#         date = request.json["date"]
#         author = request.json["author"]
#         source = request.json["source"]
#         collection = request.json["collection"]
#         language = request.json["language"]

#         # Use the function in model
#         c = model.insert_doc_data(text_id, date, author, source, collection, language)
        
#         # If the insert was successful, return the okey msg
#         # if c:
#             # return jsonify({"result":"insert okey"})
#         # else:
#             # 
#             # return jsonify({"result":"error inserting data"})
#         return jsonify({"result":"okey inserting data"})


#     @app.route('/documents', methods=['POST'])
#     def insert_documents_data():

#         # Get data in json format
#         text_id = request.json["text_id"]
#         date = request.json["date"]
#         author = request.json["author"]
#         source = request.json["source"]
#         collection = request.json["collection"]
#         language = request.json["language"]

#         # Use the function in model
#         c = model.insert_doc_data(text_id, date, author, source, collection, language)
        
#         # If the insert was successful, return the okey msg
#         # if c:
#             # return jsonify({"result":"insert okey"})
#         # else:
#             # 
#             # return jsonify({"result":"error inserting data"})
#         return jsonify({"result":"okey inserting data"})

#     # Delete a document by id
#     # --------------------------------------------------------------------
#     @app.route("/documents", methods=["DELETE"])
#     def delete_doc_data():
#         text_id = request.json["text_id"]
#         c = model.delete_doc_data(text_id)
#         return jsonify("okey deleted")



#     # Route to insert data in corpus table
#     # ----------------------------------------------------------------------
#     @app.route('/insert_corpus_data', methods=['POST'])
#     def insert_corpus_data():

#         # Get data in json format
#         corpus_id = request.json["corpus_id"]
#         corpus_name = request.json["corpus_name"]
#         labels = request.json["labels"]
#         description = request.json["description"]
#         version = request.json["version"]
#         n_docs = request.json["n_docs"]

#         # Use the function in model
#         c = model.insert_cor_data(corpus_id, corpus_name, labels, description, version, n_docs)
        
#         # If the insert was successful, return the okey msg
#         # if c:
#         #     return jsonify({"result":"insert okey"})
#         # else:
#         #     return jsonify({"result":"error inserting data"})
#         return jsonify({"result":"okey inserting data"})

#     # Delete a document by id
#     # --------------------------------------------------------
#     # @app.route("/delete_doc_data", methods=["POST"])
#     # def delete_doc_data():
#     #     text_id = request.json["text_id"]
#     #     c = model.delete_doc_data(text_id)
#     #     return jsonify("okey deleted")

# except:
#     msg = 'Error'
#     print(msg)


# # To check insert_documents_data route in postman or thunder client. 
# # Specify the route and add the following data in json 

# {
#   "text_id":"2",
#   "date":"02",
#   "author":"bsc",
#   "source":"web",
#   "collection":"col2",
#   "language":"es"
# }