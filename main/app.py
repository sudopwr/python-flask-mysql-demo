"""Flask App main module"""
from flask import Flask, request, render_template
from flask_cors import CORS
from uuid import uuid4
import os
from main.config import config
from main.utils import testing

app = Flask(__name__)
app_mode = os.getenv("APP_MODE")
config_props = config.get(app_mode)
app.config.from_object(config_props)

CORS(app, origins=[app.config["DEBUG"]])
print('App origins : %s' % app.config["APP_ORIGINS"])
print('DEBUG : %s' % app.config["DEBUG"])

blogs = [{
    "id": "12234",
    "title": "HTML Tutorial",
    "content": "This is good tutorials"
}, {
    "id": "3445435trt45",
    "title": "CSS Tutorial",
    "content": "This is good CSS tutorials"
}]

@app.route('/blogs', methods = ["get"])
def get_blogs():
    return blogs

@app.route('/blogs/<id>', methods = ["get"])
def get_by_id_blogs(id):
    temp = [blog for blog in blogs if blog["id"] == id][0]
    return temp, 200

@app.route('/blogs', methods = ["post"])
def add_blogs():
    request_data = request.get_json()
    blog = {
        "id": str(uuid4()),
        "title": request_data["title"],
        "content": request_data["content"]
    }
    print(blog)
    blogs.append(blog)
    return blog, 201

@app.route('/blogs/<id>', methods = ["put"])
def update_blogs(id):
    request_data = request.get_json()
    temp = [blog for blog in blogs if blog["id"] == id][0]
    print(temp)
    temp["title"] = request_data["title"]
    temp["content"] = request_data["content"]
    return { "msg": "success" }, 200

@app.route('/blogs/<id>', methods = ["delete"])
def delete_blogs(id):
    temp = [blog for blog in blogs if blog["id"] != id]
    print(temp)
    blogs.clear()
    blogs.extend(temp)
    return { "msg": "success" }, 200

    
with app.app_context():
    testing()
    