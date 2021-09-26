from producer import publish
from flask import Flask, jsonify, abort
from dataclasses import dataclass
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/ms_main'
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@dataclass
class Product(db.Model):
    id : int
    title : str
    image : str  
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id : int
    user_id : int
    product_id : int 
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route("/api/products/")
def index():
    return jsonify(Product.query.all())


@app.route("/api/products/<int:id>/like/", methods=['GET'])
def like(id):
    req = requests.get('http://172.17.0.1:8000/api/user/')
    json = req.json()

    productUser = ProductUser(user_id=json['id'], product_id=id)
    db.session.add(productUser)
    db.session.commit()

    publish('product_liked', id)

    return jsonify({
        'message' : 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')