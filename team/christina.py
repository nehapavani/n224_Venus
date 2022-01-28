import requests
from flask import Blueprint
from flask import render_template, request
import json

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_christina = Blueprint('christina', __name__,
                     url_prefix='/team',
                     template_folder='templates/teamhtml',
                     static_folder='static',
                     static_url_path='static')


@app_christina.route("/christina/", methods=['GET', 'POST'])
def christina():
    place="Atlanta"
    if request.method == 'POST':
        place = request.form['place']
    querystring = {"q":place}

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "35c993f134msh6fbb5b79c410a17p11f3f7jsn6ad7e30cfe36"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    print(response.text)
    return render_template("teamhtml/christina.html", detail=output)
