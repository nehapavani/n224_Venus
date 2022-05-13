from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template, request
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
import requests
import json

app = Flask(__name__)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


@app.route('/')
# map URL route for function below
def index():
    return render_template("index.html")


@app.route('/shopnow', methods=['GET','POST'])
def shopnow():
    return render_template("shopnow.html")


@app.route('/feedback', methods=['GET','POST'])
def feedback():
    return render_template("feedback.html")


@app.route('/size', methods=['GET','POST'])
def size():
    return render_template("size.html")


if __name__ == "__main__":
    app.run(debug=True)
