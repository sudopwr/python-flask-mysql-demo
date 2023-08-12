"""Flask App main module"""
from flask import Flask

app = Flask(__name__)

@app.route('/products')
def index():
    return { "name": "sudo power" }
