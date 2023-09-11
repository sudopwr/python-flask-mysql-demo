from flask import Blueprint, request, jsonify, g
import jwt

login_blp = Blueprint("Login", __name__)


@login_blp.route('/login', methods=["post"])
def login():
    request_data = request.get_json()
    username = request_data["username"]

    payload = {
        "uid": username
    }

    token = jwt.encode(payload, "dsfdf5654tgfdg5546", algorithm = "HS256")

    return { "token": token }

@login_blp.route('/orders', methods=["get"])
def get_orders():
    # verify
    token = get_token_auth_header()
    print(token)
    data = jwt.decode(token, "dsfdf5654tgfdg5546", algorithms = ["HS256"])
    g.user = data
    print(g.user)
    return { "orders" : "success" }


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
    return token
