from flask import flask

app = flask(__name__)

@app.route('/')
def index():
    return "<h1>hello Flask</h1>"


if __name__ == "__main__":
    app.run()
