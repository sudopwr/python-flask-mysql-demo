from flask import Blueprint, request, jsonify, g, current_app
import jwt
from functools import wraps
from google.oauth2 import id_token
from google.auth.transport import requests
from main.models import User
from main.db import db

login_blp = Blueprint("Login", __name__)

@login_blp.route('/login', methods=["post"])
def login():
    try:
        request_data = request.get_json()
        google_id_token = request_data["jwt"]
        idinfo = id_token.verify_oauth2_token(google_id_token, requests.Request(), current_app.config["GOOGLE_CLIENT_ID"])

        google_user_id = idinfo["sub"]

        user = User.query.get(google_user_id)

        if user is None:
            user = User(
                id = google_user_id,
                name = idinfo["name"],
                email = idinfo["email"],
                image = idinfo["picture"],
            )
            db.session.add(user)
            db.session.commit()

        payload = {
            "uid": google_user_id
        }

        if idinfo["email"] == current_app.config["ADMIN_EMAIL"]:
            payload["role"] = "admin"
        else:
            payload["role"] = "user"

        jwtToken = jwt.encode(payload, current_app.config["JWT_SECRET"], algorithm = "HS256")

        return { "token": jwtToken }
    except Exception as e:
        return { "error": "Login Failed" }, 401

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token, msg = get_token_auth_header()

        if token == False:
            return { "error": msg }, 401
        try:
            g.user = jwt.decode(token, current_app.config["JWT_SECRET"], algorithms = ["HS256"])
        except Exception as e:
            return { "error": "Invalid Token" }, 401
        
        return f(*args, **kwargs)

    return decorator

def should_be_admin(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            if g.user["role"] != "admin":
                return { "error": "Invalid request" }, 403
        except Exception as e:
            return { "error": "Invalid request" }, 403
        
        return f(*args, **kwargs)

    return decorator

def get_token_auth_header():
    auth = request.headers.get("Authorization", None)
    if not auth:
        return False, "Authorization header is expected"

    parts = auth.split()

    if parts[0].lower() != "bearer":
        return False, "Authorization header must start with Bearer"
    elif len(parts) == 1:
        return False, "Token not found"
    elif len(parts) > 2:
        return False, "Authorization header must be Bearer token"

    token = parts[1]
    return token, ''
