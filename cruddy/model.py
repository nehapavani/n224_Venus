# model.py
# The class that you use to represent users needs to implement these properties and methods:  
# is_authenticated, is_active, is_anonymous, get_id()
# To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations  
# for all of these properties and methods.

from flask_login import UserMixin
# Users DB is a collection Data Structure
class Users(UserMixin, db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes instance variables within object
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.set_password(password) #encrypt password
        self.phone = phone

# required for login_user, overrides id (login_user default) to implemented userID
# The method get_id() must return a str that uniquely identifies this user, and can be used to load the user  
# from the user_loader callback.
def get_id(self):
    return self.userID
