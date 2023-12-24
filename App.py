from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

# Create a Flask web application
app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initialize SQLAlchemy for database operations
db = SQLAlchemy(app)

# Define a model for the 'Item' table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Remove db.create_all() from here

# Define a form using Flask-WTF for handling item input
class ItemForm(FlaskForm):
    name = StringField('Name')
    quantity = IntegerField('Quantity')
    submit = SubmitField('Submit')

# Define a route for the home page
@app.route('/')
def index():
    # Query all items from the 'Item' table
    items = Item.query.all()

    # Render the 'index.html' template, passing the items to display
    return render_template('index.html', items=items)

# ... (rest of the code remains the same)

# Run the application if this script is executed
if __name__ == '__main__':
    # Move db.create_all() inside the if block
    with app.app_context():
        # Create the 'Item' table in the database
        db.create_all()

    # Run the application in debug mode
    app.run(debug=True)
