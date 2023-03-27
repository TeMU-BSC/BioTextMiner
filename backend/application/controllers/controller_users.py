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
        if username == 'admin' and password == '123':

            # If correct, return success message
            return jsonify({"message": "Login successfull"})
        
        else:

            # Else, return incorrect credentials error
            return jsonify({"message": "Username or password incorrects"})
    
    except:
        return jsonify({"message": "An error happened"})
