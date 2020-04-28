from flask import Flask


def create_app():
    application = Flask(__name__, instance_relative_config=True,)

    @application.route("/")
    def index():
        return "Hello dev"

    return application


if __name__ == "__main__":
    application = create_app()
    application.debug = True
    application.run()
