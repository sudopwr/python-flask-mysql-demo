from flask import Blueprint, request, jsonify
from uuid import uuid4
from main.models.blog import Blog
from main.db import db

blog_blp = Blueprint("Blog", __name__)

@blog_blp.route('/blogs', methods = ["get"])
def get_blogs():
    blogs = Blog.query.all()
    return jsonify(blogs)

@blog_blp.route('/blogs/<id>', methods = ["get"])
def get_by_id_blogs(id):
    blog = Blog.query.get_or_404(id)
    return jsonify(blog), 200

@blog_blp.route('/blogs', methods = ["post"])
def add_blogs():
    request_data = request.get_json()
    blog = Blog(title = request_data["title"], content =  request_data["content"])
    db.session.add(blog)
    db.session.commit()
    return { "msg": "success" }, 201

@blog_blp.route('/blogs/<id>', methods = ["put"])
def update_blogs(id):
    request_data = request.get_json()
    blog = Blog.query.get_or_404(id)
    blog.title = request_data["title"]
    blog.content = request_data["content"]
    db.session.commit()
    return { "msg": "success" }, 200

@blog_blp.route('/blogs/<id>', methods = ["delete"])
def delete_blogs(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return { "msg": "success" }, 200


