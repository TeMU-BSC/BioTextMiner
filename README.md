# BioTextMiner
BioTextMiner is a web application developed by the NLP4BIA  that provides a user-friendly interface for corpus control of biomedical corpora. With BioTextMiner, researchers can easily manage and manipulate large-scale biomedical text data by organizing and curating it in a centralized database


# Code
The code is structured as follows:
- Backend : Manages the backend endpoint and access to database
- Frontend : User interface of the application

# Technologies
- Flask : Python framework, used to write the endpoints in the backend
- React (NextJs) : JavaScript library, used in the frontend
- MySql : Relation Database
- ElasticSearch : Searching server

# Prerequisites
- Mysql server
- ElasticSearch server
- Node v.18
- python 3

# Usage
## Start Flask application
flask --debug run

This will start the flask app in debug mode

## Start NextJs application
npm run dev

By default, it is started in port 8005. To change the port, modify it in package.json.

