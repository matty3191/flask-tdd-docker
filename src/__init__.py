import os

from flask import Flask
# from flask import Flask, jsonify
# from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# #instantiate the app
# app = Flask (__name__)
# api = Api(app)

# #set config
# app_settings = os.getenv('APP_SETTINGS')
# app.config.from_object(app_settings)
# # app.config.from_object('src.config.DevelopmentConfig') - old

#instantiate the db
db = SQLAlchemy()

# #model
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), nullable=False)
#     active = db.Column(db.Boolean(), default=True, nullable=False)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# class Ping(Resource):
#     def get(self):
#         return {
#             'status':'success',
#             'message':'pong!'
#         }

# api.add_resource(Ping, '/ping')

#application factory pattern
def create_app(script_info=None):
    
    #instantiate the app
    app = Flask(__name__)

    #set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    #set up extensions
    db.init_app(app)

    #register blueprints
    from src.api.ping import ping_blueprint
    app.register_blueprint(ping_blueprint)

    from src.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    #shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app

    ##Take note of the shell_context_processor. This is used to register the app and db to the shell. 
    # Now we can work with the application context and the database without having to import them directly into the shell
