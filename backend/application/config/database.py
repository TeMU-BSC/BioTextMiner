#----------------------------------------------------------------------------#
# File: database
# Description: This file is used to get the connection with database
# Author : Siddique Muhammad
# Date: 21/02/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import pymysql

# Configparser settings
import configparser
parameters = config = configparser.ConfigParser()
parameters.read('./configuration.cfg')



# Function to get the connection with database
# -----------------------------------------------------------------------------------------
def get_connection():
        return pymysql.connect( host=parameters['database']['host'], 
                                user= parameters['database']['user'], 
                                passwd= parameters['database']['password'], 
                                db=parameters['database']['database'])




# For testing here
# -----------------------------------------------------------------------------------------
conn = pymysql.connect( host=parameters['database']['host'], 
                        user= parameters['database']['user'], 
                        passwd= parameters['database']['password'], 
                        db=parameters['database']['database'])

# Cursor        
cursor = conn.cursor()

# Select
# print(cursor.execute('SELECT author FROM documents'))
# conn.commit()

# Insert values
# cursor.execute("INSERT INTO documents VALUES ('1', '2023-02-16', 'bsc', 'web', 'col1', 'es');")
# conn.commit()

# cursor.execute('describe documents')
# cursor.execute('INSERT INTO games VALUES(1, uno, ')

