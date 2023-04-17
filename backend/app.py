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

# Configparser settings
# ----------------------------------------------------------------------
import configparser

parameters = config = configparser.ConfigParser()
parameters.read('./configuration.cfg')


# Main
# ----------------------------------------------------------------------
if __name__=="__main__":    
    CORS(app)                  
    app.run(debug=True) 
