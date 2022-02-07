""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from _init_ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and type and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Events (db.Model):
    # define the Users schema
    eventID = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), unique=False, nullable=False)
    rating = db.Column(db.String(255), unique=False, nullable=False)
    location = db.Column(db.String(255), unique=False, nullable=False)
    date = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, type, rating, location, date):
        self.type = type
        self.rating = rating
        self.location = location
        self.date = date


    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "eventID": self.eventID,
            "type": self.type,
            "rating": self.rating,
            "location": self.location,
            "date": self.date
        }

    # CRUD update: updates users type, location, date
    # returns self
    def update(self, type):
        """only updates values with length"""
        if len(type) > 0:
            self.type = type
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: events")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""

    u1 = Events(type='Flood', rating='4', location='New York', date="2003-03-02")


    table = [u1]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate rating, or error: {row.rating}")


def model_printer():
    print("------------")
    print("Table: events with SQL query")
    print("------------")
    result = db.session.execute('select * from Events')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()