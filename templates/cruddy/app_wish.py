"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_login import login_required

from templates.cruddy.query import *

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_wish = Blueprint('wish', __name__,
                     url_prefix='/wish',
                     template_folder='templates/wishy/',
                     static_folder='static',
                     static_url_path='static')

""" Blueprint is established to isolate Application control code for CRUD operations, key features:
    1.) 'Users' table control methods, controls relationship between User Actions and Database Model
    2.) Control methods are achieved using app routes for each CRUD operations
    3.) login required to restrict CRUD operations to identified users
"""


# Default URL for Blueprint
@app_wish.route('/')
@login_required  # Flask-Login uses this decorator to restrict acess to logged in users
def wish():
    """obtains all Users from table and loads Admin Form"""
    return render_template("cruddy/templates/wish.html", table=wishlist_all())


# Flask-Login directs unauthorised users to this unauthorized_handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('wish.wish_login'))


# if login url, show phones table only
@app_wish.route('/login/', methods=["GET", "POST"])
def wish_login():
    # obtains form inputs and fulfills login requirements
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):       # zero index [0] used as email is a tuple
            return redirect(url_for('wish.wish'))

    # if not logged in, show the login page
    return render_template("cruddy/templates/wlogin.html")


@app_wish.route('/authorize/', methods=["GET", "POST"])
def wish_authorize():
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password1 = request.form.get("password1")
        password2 = request.form.get("password1")         # password should be verified
        if authorize(user_name, email, password1):    # zero index [0] used as user_name and email are type tuple
            return redirect(url_for('wish.wish_login'))
    # show the auth user page if the above fails for some reason
    return render_template("cruddy/templates/wauthorize.html")


# CRUD create/add
@app_wish.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = WishList(
            request.form.get("name"),
            request.form.get("quantity")
        )
        po.create()
    return redirect(url_for('wish.wish'))


# CRUD read
@app_wish.route('/read/', methods=["POST"])
def read():
    """gets Item Number from form and obtains corresponding data from WishList table"""
    table = []
    if request.form:
        num = request.form.get("num")
        po = wishlist_by_id(num)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("cruddy/templates/wish.html", table=table)


# CRUD update
@app_wish.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        num = request.form.get("num")
        name = request.form.get("name")
        po = wishlist_by_id(num)
        if po is not None:
            po.update(name)
    return redirect(url_for('wish.wish'))


# CRUD delete
@app_wish.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        num = request.form.get("num")
        po = wishlist_by_id(num)
        if po is not None:
            po.delete()
    return redirect(url_for('wish.wish'))


# Search Form
@app_wish.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("cruddy/templates/wsearch.html")


# Search request and response
@app_wish.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    return response