from flask import Blueprint
from flask import render_template
import json

app_anika = Blueprint('anika', __name__,
                     url_prefix='/team',
                     template_folder='templates/teamhtml',
                     static_folder='static',
                     static_url_path='static')

@app_anika.route("/anika/")
def anika():
    import requests
    url = "https://random-palette-generator.p.rapidapi.com/palette/10/3"

    headers = {
        'x-rapidapi-host': "random-palette-generator.p.rapidapi.com",
        'x-rapidapi-key': "919ce4f3a5msh7c957a7d94f60dfp124405jsnb6d1a6618168"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    output = json.loads(response.text)
    print(response.text)
    return render_template("teamhtml/anika.html", A=output, B=output)


    return render_template("teamhtml/anika.html")
