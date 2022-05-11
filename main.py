from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")


@app.route('/shopnow', methods=['GET','POST'])
def shopnow():
    return render_template("shopnow.html")


@app.route('/feedback', methods=['GET','POST'])
def feedback():
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
