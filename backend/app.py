# -- coding utf-8 --
# ----------------------------------------------------------------------
# Author : Siddique Muhammad
# Date : 15/03/2023
# Copyright (c) 2023 Barcelona Supercomputing Center
# ----------------------------------------------------------------------


'''
This module contains the BioTextMiner API.
'''

# Import
# ----------------------------------------------------------------------
from flask import Flask
from application import app
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

# Configparser settings
# ----------------------------------------------------------------------
import configparser

parameters = config = configparser.ConfigParser()
parameters.read('./configuration.cfg')


# Main
# ----------------------------------------------------------------------
if __name__=="__main__": 

    app.config['JWT_SECRET_KEY'] = 'secretkey'
    jwt = JWTManager(app)   
    
    CORS(app)                  
    app.run(debug=True) 
