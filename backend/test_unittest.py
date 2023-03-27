#----------------------------------------------------------------------------#
# File: test_unittest.py
# Description: This file is used for testing the endpoints and other functionalities with the library Unittest
# Author : Siddique Muhammad
# Date: 07/03/2023
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
# Try to import modules with exeptions
try:
    from application import app
    import unittest

except Exception as e:
    print("Exception module not found ".format(e))


#----------------------------------------------------------------------------#
# Class: Flask Test 
# Description: This class includes different testing methods
# Author : Siddique Muhammad
# Date: 07/03/2023
#----------------------------------------------------------------------------#
class FlaskTest(unittest.TestCase):
    # Check for the response 
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/documents")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    # Check if content return is json
    # def test_index(self):
    #     tester = app.test_client(self)
    
    #     response = tester.get("/documents")
    #     self.assertEqual(response.content_type, "application/json")

        # Return ok!


    # Check for Data returned
    # def test_index_data(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/documents")
    #     self.assertTrue(b'bsc' in response.data) 

    #     # Return ok!

    # def test_index_data(self):
    #     tester = app.test_client(self)
    #     response = tester.delete("/documents/2")
    #     self.assertEqual(response.content_type, "application/json")
        # self.assertTrue(b'okey' in response.data) 

        # Return ok!

    # def test_index_data(self):
    #     tester = app.test_client(self)
    #     response = tester.delete("/corpus/2")
    #     self.assertEqual(response.content_type, "application/json")
        # self.assertTrue(b'okey' in response.data) 

        # Return ok!

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/specialties-by-document/10")
        self.assertEqual(response.content_type, "application/json")
        # self.assertTrue(b'okey' in response.data) 

        # Return ok!


#----------------------------------------------------------------------------#
# Main
#----------------------------------------------------------------------------#
if __name__ == "__main__":
    
    # Run the Test Program
    unittest.main()
