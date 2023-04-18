#----------------------------------------------------------------------------#
# File: User Model
# Description: Manages all the petitions from the server
# Author : Siddique Muhammad
# Date: 10/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from pathlib import Path
from application.config.database import get_connection # Import the database connection

# Get user from the database
def get_user(username, password):
    '''
    Input parameters: - username: the username of the user to search
                      - password: the password of the user to search
    '''

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute ('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))        

        #fetch data and return
        data = cursor.fetchone()
        return data
    
# Function to register a user
# ---------------------------------------------------------------------------------
def insert_user(name, surname, email, username, password):
    '''
    Input parameters: 
                    user's data
    '''

    # Guest role by default
    role = 'guest'

    # get connection
    conexion = get_connection()

    # cursor
    with conexion.cursor() as cursor:

        # execute command
        cursor.execute("INSERT INTO users(username, password, name, surname, email, role) VALUES (%s, %s, %s, %s, %s, %s)",
                    (username, password, name, surname, email, role))

    # commit and return message
    conexion.commit()
    return(str(cursor.rowcount)+ " record(s) updated")