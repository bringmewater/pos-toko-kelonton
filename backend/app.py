from flask import Flask


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    from .blueprints.example import example_bp
    app.register_blueprint(example_bp)

    return app
