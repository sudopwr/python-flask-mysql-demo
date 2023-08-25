from main.usecases.blog import blog_blp
from main.usecases.product import product_blp

def register_routes(app):
    app.register_blueprint(blog_blp)
    app.register_blueprint(product_blp)