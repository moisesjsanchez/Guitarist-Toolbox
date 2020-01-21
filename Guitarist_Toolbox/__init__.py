from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from Guitarist_Toolbox.config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    from Guitarist_Toolbox.api.routes import api
    app.register_blueprint(api)

    return app
