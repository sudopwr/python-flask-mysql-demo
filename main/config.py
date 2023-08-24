import os

class ProductionConfigs:
    DEBUG = False
    APP_ORIGINS = os.getenv("APP_ORIGINS")

class DevelopmentConfigs:
    DEBUG = True
    APP_ORIGINS = os.getenv("APP_ORIGINS")

    
config = {
    "production": ProductionConfigs,
    "development": DevelopmentConfigs
}
