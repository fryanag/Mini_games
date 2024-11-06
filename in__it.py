from flask import Flask

from .routes import main

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask!"
app.register_blueprint(main)