from _init_ import db
from crud.model import Events
import random


# this is method called by frontend, it has been randomized between Alchemy and Native SQL for fun
def users_all():
    if random.randint(0, 1) == 0:
        table = users_all_alc()
    else:
        table = users_all_alc()
    return table


# SQLAlchemy extract all users from database
def users_all_alc():
    table = Events.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready


# Native SQL extract all users from database
def users_all_sql():
    table = db.session.execute('select * from Events')
    json_ready = sqlquery_2_list(table)
    return json_ready


# SQLAlchemy extract users from database matching term
def users_ilike(term):
    """filter Users table by term into JSON list (ordered by User.type)"""
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Events.query.order_by(Events.type).filter((Events.type.ilike(term)) | (Events.rating.ilike(term)))
    return [peep.read() for peep in table]


# SQLAlchemy extract single user from database matching ID
def user_by_id(eventID):
    """finds User in table matching userid """
    return Events.query.filter_by(eventID=eventID).first()


# SQLAlchemy extract single user from database matching rating
def user_by_rating(rating):
    """finds User in table matching rating """
    return Events.query.filter_by(rating=rating).first()


# ALGORITHM to convert the results of an SQL Query to a JSON ready format in Python
def sqlquery_2_list(rows):
    out_list = []
    keys = rows.keys()  # "Keys" are the columns of the sql query
    for values in rows:  # "Values" are rows within the SQL database
        dictionary = {}
        for i in range(len(keys)):  # This loop lines up K, V pairs, same as JSON style
            dictionary[keys[i]] = values[i]
        dictionary["query"] = "by_sql"  # This is for fun a little watermark
        out_list.append(dictionary)  # Finally we have a out_list row
    return out_list


# Test queries
if __name__ == "__main__":
    for i in range(10):
        print(users_all())