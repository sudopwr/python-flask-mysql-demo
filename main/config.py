import os

class ProductionConfigs:
    DEBUG = False
    APP_ORIGINS = os.getenv("APP_ORIGINS")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

class DevelopmentConfigs:
    DEBUG = True
    APP_ORIGINS = os.getenv("APP_ORIGINS")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    
config = {
    "production": ProductionConfigs,
    "development": DevelopmentConfigs
}
