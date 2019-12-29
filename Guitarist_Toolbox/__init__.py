import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Guitarist_Toolbox.config import DevelopmentConfig

db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    from Guitarist_Toolbox.api.routes import api
    app.register_blueprint(api)

    return app