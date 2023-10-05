import os

class ProductionConfigs:
    DEBUG = False
    APP_ORIGINS = os.getenv("APP_ORIGINS")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    JWT_SECRET = os.getenv("JWT_SECRET")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

class DevelopmentConfigs:
    DEBUG = True
    APP_ORIGINS = os.getenv("APP_ORIGINS")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    JWT_SECRET = os.getenv("JWT_SECRET")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

    
config = {
    "production": ProductionConfigs,
    "development": DevelopmentConfigs
}
