import requests
from flask import Blueprint
from flask import render_template, request

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_neha = Blueprint('neha', __name__,
                     url_prefix='/team',
                     template_folder='templates/teamhtml',
                     static_folder='static',
                     static_url_path='static')

@app_neha.route("/neha/",methods=['GET', 'POST'])
def neha():
    output = [{'number':2,'text':'is a prime number'}]
    if request.form:
        num1 = request.form.get('num1')

        if len(num1)>0:  # input field has content
            url = "https://numbersapi.p.rapidapi.com/"+num1+"/math"

            querystring = {"fragment":"true","json":"true", "number":"num"}
            headers = {
                'x-rapidapi-host': "numbersapi.p.rapidapi.com",
                'x-rapidapi-key': "2f4fb94902msh2ed8a6c271d64d9p1535e1jsn91c7cb7b9d1c",
                'x-numbers-api-number': "num"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)

            return render_template("teamhtml/neha.html", x=response.json())
    return render_template("teamhtml/neha.html", x=output)