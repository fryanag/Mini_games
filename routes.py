from flask import Blueprint

# Define a Blueprint for the routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello from routes!"

@main.route('/about')
def about():
    return "About page"
