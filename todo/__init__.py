from flask import Flask




def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = 1
    from .views.routes import api

    app.register_blueprint(api)
    return app
