"""Flask App main module"""
import os
from flask import Flask, request, render_template
from flask_cors import CORS
from uuid import uuid4
from main.config import config
from main.usecases import register_routes
from main.db import db
from main.models import *

app = Flask(__name__)
app.config.from_object(config.get(os.getenv("APP_MODE")))

CORS(app, origins=[app.config["APP_ORIGINS"]])
register_routes(app)
db.init_app(app)
    
with app.app_context():
    db.create_all()
    