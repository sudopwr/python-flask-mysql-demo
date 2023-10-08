from flask import Blueprint, request, jsonify, g
from uuid import uuid4
from main.models import Order, User, Product
from main.db import db
from main.usecases.login import login_required

order_blp = Blueprint("Order", __name__)


@order_blp.route('/orders', methods=["get"])
@login_required
def get_orders():
    orders = None
    if g.user["role"] == "admin":
        orders = Order.query\
            .join(User, Order.user_id == User.id)\
            .join(Product, Order.product_id == Product.id)\
            .add_columns(User.name, Product.name)\
            .all()
    else:
        orders = Order.query\
            .join(User, Order.user_id == User.id)\
            .join(Product, Order.product_id == Product.id)\
            .add_columns(User.name, Product.name)\
            .filter(Order.user_id == g.user["uid"])\
            .all()

    print(orders)
    result = []
    for order in orders:
        _order = order[0]
        username = order[1]
        productname = order[2]

        final = {
            "id": _order.id,
            "product_id": _order.product_id,
            "user_id": _order.user_id,
            "quantity": _order.quantity,
            "status": _order.status,
            "order_date": _order.order_date,
            "user_name": username,
            "product_name": productname,
        }
        result.append(final)

    print(result)
    return jsonify(result)


@order_blp.route('/orders', methods=["post"])
@login_required
def add_orders():
    try:
        request_data = request.get_json()
        order = Order(
            product_id=request_data["product_id"],
            quantity=request_data["quantity"],
            user_id=g.user["uid"],
            status="order_placed"
        )
        db.session.add(order)
        db.session.commit()
        return {"msg": "success"}, 201
    except Exception as e:
        print(e)
        return {"msg": "Failed"}, 500
