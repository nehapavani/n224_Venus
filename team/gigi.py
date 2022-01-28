import requests
from flask import Blueprint
from flask import render_template
import json

app_gigi = Blueprint('gigi', __name__,
                                url_prefix='/team',
                                template_folder='templates/teamhtml',
                                static_folder='static',
                                static_url_path='static')

@app_gigi.route("/gigi/")
def gigi():
    url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

    headers = {
        'x-rapidapi-host': "random-words-with-pronunciation.p.rapidapi.com",
        'x-rapidapi-key': "4ab4681ba9mshf17197c9d59be44p17d1edjsnabe7ccc22eb5"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("teamhtml/gigi.html", Y=output)
