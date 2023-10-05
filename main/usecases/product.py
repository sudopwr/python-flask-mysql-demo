from flask import Blueprint, request, jsonify
from uuid import uuid4
from main.models import Product
from main.db import db
from main.usecases.login import login_required, should_be_admin

product_blp = Blueprint("Product", __name__)


@product_blp.route('/products', methods=["get"])
def get_product():
    products = Product.query.all()
    return jsonify(products)


@product_blp.route('/products/<id>', methods=["get"])
def get_by_id_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product), 200


@product_blp.route('/products', methods=["post"])
@login_required
@should_be_admin
def add_product():
    request_data = request.get_json()
    product = Product(
        name=request_data["name"],
        description=request_data["description"],
        price=request_data["price"],
        quantity=request_data["quantity"],
        image=request_data["image"],
    )
    db.session.add(product)
    db.session.commit()
    return {"msg": "success"}, 201


@product_blp.route('/products/<id>', methods=["put"])
@login_required
@should_be_admin
def update_product(id):
    request_data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = request_data["name"]
    product.description = request_data["description"]
    product.price = request_data["price"]
    product.quantity = request_data["quantity"]
    if "image" in request_data:
        product.image = request_data["image"]
        
    db.session.commit()
    return {"msg": "success"}, 200


@product_blp.route('/products/<id>', methods=["delete"])
@login_required
@should_be_admin
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return {"msg": "success"}, 200
