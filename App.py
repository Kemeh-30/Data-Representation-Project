from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Remove db.create_all() from here

class ItemForm(FlaskForm):
    name = StringField('Name')
    quantity = IntegerField('Quantity')
    submit = SubmitField('Submit')

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

# ... (rest of the code remains the same)

if __name__ == '__main__':
    # Move db.create_all() inside the if block
    with app.app_context():
        db.create_all()
    app.run(debug=True)

