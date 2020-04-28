from flask import Flask

application = Flask(__name__, instance_relative_config=True,)


@application.route("/")
def index():
    return "Hello World"


# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()
