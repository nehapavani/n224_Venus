"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response

from crud.sql import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_earthquakerating = Blueprint('earthquakerating', __name__,
                                 url_prefix='/earthquakerating',
                                 template_folder='templates/earthquakerating/',
                                 static_folder='static',
                                 static_url_path='static')

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes for CRUD (Blueprint)
"""


# Default URL
@app_earthquakerating.route('/')
def earthquakerating():
    """obtains all Users from table and loads Admin Form"""
    return render_template("earthquakerating.html", table=users_all())


# CRUD create/add
@app_earthquakerating.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("type"),
            request.form.get("address"),
            request.form.get("city"),
            request.form.get("date")
        )
        po.create()
    return redirect(url_for('earthquakerating.earthquakerating'))


# CRUD read
@app_earthquakerating.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("earthquakerating.html", table=table)


# CRUD update
@app_earthquakerating.route('/update/', methods=["POST"])
def update():
    """gets userid and type from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("type")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('earthquakerating.earthquakerating'))


# CRUD delete
@app_earthquakerating.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('earthquakerating.earthquakerating'))


# Search Form
@app_earthquakerating.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("earthquakerating.html")


# Search request and response
@app_earthquakerating.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    return response