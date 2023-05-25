#----------------------------------------------------------------------------#
# File: Users Controller
# Description: Manages all the routes and data for the Users table
# Author : Siddique Muhammad
# Date: 15/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from application import app
from flask import Flask,jsonify,request
from application.models import User

# CORS
from flask_cors import CORS
CORS(app)
#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#

# Route to do login
# ---------------------------------------------------------------------------
@app.route('/login', methods=['POST']) 
def login():

    # Try to do login, excepts error
    try:

        # Receive data from the client
        data = request.get_json()
        username = request.json['username']
        password = request.json['password']

        # Check if the username and password are correct
        # if username == 'admin' and password == '123':
        response = User.get_user(username, password)
        print(response)

        if response:
            # access_token = create_access_token(identity=username)
            # print(access_token)
            # If correct, return success message
            return jsonify({"message": "Login successfull", "err":"false", "data":response})
        
        else:

            # Else, return incorrect credentials error
            return jsonify({"message": "Username or password incorrects", "err":"true", "data":response})
    
    except:
        return jsonify({"message": "An error happened", "err":"true", "data":response})


# Route to insert data in documents table
# ----------------------------------------------------------------------
@app.route('/register', methods=['POST'])
def insert_user_data():

    # try to insert a document data, if not possible return an error message as a result
    try:
        # Get data in json format
        name = request.json["name"]
        surname = request.json["surname"]
        email = request.json["email"]
        username = request.json["username"]
        password = request.json["password"]

        print(name, surname, email, username, password)
        # Use the function in model
        result = User.insert_user(name, surname, email, username, password)
    
        # If the insert was successful, return the okey msg
        return jsonify({"result":"okey inserting data","response":result})
    
    except:
        return jsonify({"result":"error inserting data"})

# For testing
# 127.0.0.1:5000/register
# { "name":"marta", 
#   "surname":"fernandez", 
#   "email":"marta@gmail.com", 
#   "username":"marta56", 
#   "password":"mypass56"
# }
