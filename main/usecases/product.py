from flask import Blueprint, request
from uuid import uuid4

product_blp = Blueprint("Product", __name__)


blogs = [{
    "id": "12234",
    "title": "HTML Tutorial",
    "content": "This is good tutorials"
}, {
    "id": "3445435trt45",
    "title": "CSS Tutorial",
    "content": "This is good CSS tutorials"
}]

@product_blp.route('/products', methods = ["get"])
def get_products():
    return blogs

@product_blp.route('/products/<id>', methods = ["get"])
def get_by_id_products(id):
    temp = [blog for blog in blogs if blog["id"] == id][0]
    return temp, 200

@product_blp.route('/products', methods = ["post"])
def add_products():
    request_data = request.get_json()
    blog = {
        "id": str(uuid4()),
        "title": request_data["title"],
        "content": request_data["content"]
    }
    print(blog)
    blogs.append(blog)
    return blog, 201

@product_blp.route('/products/<id>', methods = ["put"])
def update_products(id):
    request_data = request.get_json()
    temp = [blog for blog in blogs if blog["id"] == id][0]
    print(temp)
    temp["title"] = request_data["title"]
    temp["content"] = request_data["content"]
    return { "msg": "success" }, 200

@product_blp.route('/products/<id>', methods = ["delete"])
def delete_products(id):
    temp = [blog for blog in blogs if blog["id"] != id]
    print(temp)
    blogs.clear()
    blogs.extend(temp)
    return { "msg": "success" }, 200


