from flask import Flask, Blueprint, render_template


def create_app():
	# instantiate the app
    app = Flask(__name__)

    # register the blueprints
    from .views import views
    app.register_blueprint(views)

    return app
