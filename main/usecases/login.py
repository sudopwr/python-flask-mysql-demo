from flask import Blueprint, request, jsonify, g
import jwt
from functools import wraps

login_blp = Blueprint("Login", __name__)


@login_blp.route('/login', methods=["post"])
def login():
    request_data = request.get_json()
    username = request_data["username"]

    payload = {
        "uid": username
    }

    if username == "sudopower":
        payload["role"] = "admin"

    token = jwt.encode(payload, "dsfdf5654tgfdg5546", algorithm = "HS256")

    return { "token": token }

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token, msg = get_token_auth_header()

        if token == False:
            return { "error": msg }, 401
        try:
            g.user = jwt.decode(token, "dsfdf5654tgfdg5546", algorithms = ["HS256"])
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

@login_blp.route('/products', methods=["get"])
def get_products():
    return { "products" : "product data" }

@login_blp.route('/orders', methods=["post"])
@login_required
def add_orders():
    return { "msg" : "order has been placed successfully" }

@login_blp.route('/products', methods=["post"])
@login_required
@should_be_admin
def add_products():
    return { "msg" : "product has been added successfully" }


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
