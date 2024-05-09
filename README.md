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


FLASK RESTful Web Application

This is a simple Flask web application with a RESTful API, utilizing Flask-RESTful for creating, updating, deleting, and retrieving items. The application also includes web pages to consume the API, allowing users to perform CRUD operations on the data.

Installation
Clone the repository:



git clone https://github.com/Kemeh-30/Data-Representation-Project.git
Navigate to the project directory:


cd Representation-Project.git
Install the required dependencies:

pip install -r requirements.txt



Usage
Run the Flask application:


python app.py
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

Use the web pages to interact with the API:

Visit http: to view a list of items.
Access the RESTful API endpoints:
Individual item: http://127.0.0.1:5000/api/item/<item_id>
Collection of items: http://127.0.0.1:5000/api/items
Perform CRUD operations using the web pages or a tool like curl or Postman for the API.

API Endpoints


GET /api/item/<item_id>: Retrieve details of a specific item.
PUT /api/item/<item_id>: Update information for a specific item.
DELETE /api/item/<item_id>: Delete a specific item.
GET /api/items: Retrieve a list of all items.
POST /api/items: Create a new item.


Dependencies

Flask
Flask-WTF
Flask-SQLAlchemy
Flask-RESTful


