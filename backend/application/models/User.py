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
        cursor.execute ('SELECT * FROM users WHERE username=%s AND password=%s',username, password)        
        
        #fetch data and return
        data = cursor.fetchone()
        return data