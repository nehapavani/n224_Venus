from flask import Blueprint
from flask import render_template
import json

app_allison = Blueprint('allison', __name__,
                     url_prefix='/team',
                     template_folder='templates/teamhtml',
                     static_folder='static',
                     static_url_path='static')

@app_allison.route("/allison/")
def allison():
    import requests

    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "6a027693demsh0874e4210688c19p170b79jsn0d9c4cb261b8"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("teamhtml/allison.html", Z=output)
