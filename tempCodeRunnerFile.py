from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_restful import Api, Resource

# Create a Flask web application
app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initialize SQLAlchemy for database operations
db = SQLAlchemy(app)

# Create a RESTful API using Flask-RESTful
api = Api(app)

# Define a model for the 'Item' table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Define a form using Flask-WTF for handling item input
class ItemForm(FlaskForm):
    name = StringField('Name')
    quantity = IntegerField('Quantity')
    submit = SubmitField('Submit')

# Define a resource for individual items (RESTful API endpoint)
class ItemResource(Resource):
    def get(self, item_id):
        item = Item.query.get(item_id)
        if item:
            return jsonify({'id': item.id, 'name': item.name, 'quantity': item.quantity})
        else:
            return jsonify({'message': 'Item not found'}), 404

    def put(self, item_id):
        item = Item.query.get(item_id)
        if item:
            # Update item information based on JSON data in the request
            item.name = request.json['name']
            item.quantity = request.json['quantity']
            db.session.commit()
            return jsonify({'message': 'Item updated successfully'})
        else:
            return jsonify({'message': 'Item not found'}), 404

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            # Delete the item from the database
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item deleted successfully'})
        else:
            return jsonify({'message': 'Item not found'}), 404

# Define a resource for a collection of items (RESTful API endpoint)
class ItemsResource(Resource):
    def get(self):
        # Retrieve all items from the 'Item' table
        items = Item.query.all()
        # Convert items to a list of dictionaries for JSON response
        items_list = [{'id': item.id, 'name': item.name, 'quantity': item.quantity} for item in items]
        return jsonify({'items': items_list})

    def post(self):
        # Create a new item based on JSON data in the request
        new_item = Item(name=request.json['name'], quantity=request.json['quantity'])
        # Add the new item to the database
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item created successfully', 'id': new_item.id})

# Add the item and items resources to the API with their respective endpoints
api.add_resource(ItemResource, '/api/item/<int:item_id>')
api.add_resource(ItemsResource, '/api/items')

# Define a route for the home page
@app.route('/')
def index():
    # Retrieve all items from the 'Item' table
    items = Item.query.all()
    # Render the 'index.html' template, passing the items to display
    return render_template('index.html', items=items)

# Run the application if this script is executed
if __name__ == '__main__':
    # Create the 'Item' table in the database
    with app.app_context():
        db.create_all()

    # Run the application in debug mode
    app.run(debug=True)
