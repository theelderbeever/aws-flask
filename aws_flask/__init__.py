from flask import Flask


def create_app():
    application = Flask(__name__, instance_relative_config=True,)

    @application.route("/")
    def index():
        return "Hello factory __init__ relative and git"

    return application
