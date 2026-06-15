existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define the home page route
@app.route("/")
def home():
    return "Welcome to Flatiron Cars"

@app.route("/<model>")
def show_model(model):
    if model in existing_models:
        print (f"Flatiron {model} is in our fleet!")
    else:
        print (f"No models called {model} exists in our catalog.")

