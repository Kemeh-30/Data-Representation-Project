# Data-Representation-Project

QUESTION

Write a program that demonstrates that you understand creating and consuming
RESTful APIs.Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data. use the below to do the above question tell me what the topic is 
level 1.A rehash of the sample project lab I.e.:
1. A basic Flask server that has a
2. REST API, (to perform CRUD operations)
3. One database table and
4. Accompanying web interface, using AJAX
calls, to perform these CRUD operations


# Flask CRUD Application

This is a simple Flask application demonstrating CRUD (Create, Read, Update, Delete) operations with a SQLite database.

## Prerequisites

- Python (version 3.6 or higher)
- pip (Python package installer)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Kemeh-30/Data-Representation-Project.git
   cd Data-Representaion-Project.git


Install dependencies:

pip install -r requirements.txt



Configuration
The SQLite database is used by default. No additional configuration is required for local development.
Update the app.config['SQLALCHEMY_DATABASE_URI'] in App.py if you want to use a different database.


Running the Application

python App.py



Visit http://127.0.0.1:5000/ in your web browser to access the application.

API Endpoints
/api/items (GET and POST): Retrieve a list of items or add a new item.
/api/items/<int:item_id> (GET, PUT, DELETE): Retrieve, update, or delete a specific item.
Adding a New Item
Visit http://127.0.0.1:5000/add_item to use the web interface for adding a new item.




This README provides clear instructions on how to set up and run the project, and it specifies the use of the `requirements.txt` file for installing dependencies.
