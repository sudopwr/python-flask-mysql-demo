"""Flask App main module"""
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5501"])

@app.route('/products', methods = ["get"])
def get_products():
    return { "message": "get api called" }

@app.route('/products/<id>', methods = ["get"])
def get_by_id_products(id):
    return { "message": "get by id api called " + id }

@app.route('/products', methods = ["post"])
def add_products():
    request_data = request.get_json()
    request_data["msg"] = "product added!"
    return request_data, 201

@app.route('/products', methods = ["put"])
def update_products():
    return { "message": "put api called" }

@app.route('/products/<id>', methods = ["delete"])
def delete_products(id):
    return { "message": "delete api called " + id }
