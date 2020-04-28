from flask import Flask

app = Flask(__name__, instance_relative_config=True,)


@app.route("/")
def index():
    return "Hello World"


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.

    app.debug = True
    app.run()
