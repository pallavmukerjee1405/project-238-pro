#Importing all required libraries
import os
from flask import Flask, jsonify
from flask_cors import CORS#To develop cross-origins in the applications
from flask_sqlalchemy import SQLAlchemy#To work with all SQL queries
from flask_migrate import Migrate#To migrate the new data into the database
from dotenv import load_dotenv#To load the environment under below function load_dotenv()
load_dotenv()


# instantiate the extensions
db = SQLAlchemy()

migrate = Migrate()

def create_app(script_info=None):#To start the application

    # instantiate the app
    app = Flask(__name__)
    cors = CORS(app)


    # set configz
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # set up extensions
    db.init_app(app)


    migrate.init_app(app, db)

    # register blueprints
    from .views.views import views
    from .api.api import api

    app.register_blueprint(views)#To reveal the blueprint for the frontend code
    app.register_blueprint(api)#To reveal the blueprint for the backend code

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({
            "status":"error",
            "error":e.description
        }), 400

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({
            "status":"error",
            "error":e.description
        }), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({
            "status":"error",
            "error":"this wasn't suppose to happen"
        })

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    return app
