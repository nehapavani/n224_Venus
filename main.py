from flask import render_template, request
from _init_ import app
import requests
import json

from crud.app_crud import app_crud
app.register_blueprint(app_crud)

# create an instance of flask object



# home page accessed with http://127.0.0.1:5000/
@app.route("/",methods=['GET', 'POST'])
# map URL route for function below
def index():
    return render_template("index.html")

@app.route("/journal/")
def journal():
    return render_template("journals/journal.html")

@app.route("/earthquakerating/")
def earthquakerating():
    return render_template("earthquakerating/earthquakerating.html")

@app.route('/greet_earthquakerating', methods=['GET', 'POST'])
def greet_earthquakerating():
    # submit button has been pushed
    if request.form:
        rating = request.form.get("rating")
        if rating.__len__() != 0:  # input field has content
            return render_template("earthquakerating/earthquakerating.html", rating=rating)
        else:
            # starting and empty input default
            return render_template("earthquakerating/earthquakerating.html", rating="World")
    else:
        return render_template("earthquakerating/earthquakerating.html")

@app.route("/recent_updates/")
def recent_updates():
    return render_template("pblweek4/recent_updates.html")

@app.route("/disastermap/" , methods=['GET', 'POST'])
def disastermap():
    return render_template("pblweek4/disastermap.html")

@app.route('/greet_disastermap', methods=['GET', 'POST'])
def greet_disastermap():
    # submit button has been pushed
    if request.form:
        comment = request.form.get("comment")
        if comment.__len__() != 0:  # input field has content
            return render_template("pblweek4/disastermap.html", comment=comment)
        else:
            # starting and empty input default
            return render_template("pblweek4/disastermap.html", comment="World")
            return render_template("pblweek4/disastermap.html", comment="Bad input")
    else:
        return render_template("pblweek4/disastermap.html")


# @app.route("/disasterNews/")
# def disasterNews():

@app.route("/tracy_jarman/")
def tracy_jarman():
    return render_template("women_disasters/tracy_jarman.html")

@app.route("/anna_mani/")
def anna_mani():
    return render_template("women_disasters/anna_mani.html")

@app.route("/lydia_sijp/")
def lydia_sijp():
    return render_template("women_disasters/lydia_sijp.html")

@app.route("/impacts/")
def impacts():
    return render_template("pblweek4/impacts.html")

@app.route("/world/")
def world():
    return render_template("pblweek4/world.html")

@app.route("/animal/")
def animal():
    return render_template("pblweek4/animal.html")

@app.route("/political/")
def political():
    return render_template("pblweek4/political.html")

@app.route("/about/")
def about():
    return render_template("layouts/about.html")

@app.route("/christina/", methods=['GET', 'POST'])
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
    return render_template("team/christina.html", detail=output)

@app.route("/gigi/")
def gigi():
    url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

    headers = {
        'x-rapidapi-host': "random-words-with-pronunciation.p.rapidapi.com",
        'x-rapidapi-key': "4ab4681ba9mshf17197c9d59be44p17d1edjsnabe7ccc22eb5"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("team/gigi.html", Y=output)

@app.route("/anika/")
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
    return render_template("team/anika.html", A=output, B=output)


    return render_template("team/anika.html")

@app.route("/allison/")
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
    return render_template("team/allison.html", Z=output)

@app.route("/neha/",methods=['GET', 'POST'])
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

            return render_template("team/neha.html", x=response.json())
    return render_template("team/neha.html", x=output)

@app.route("/Tornado/")
def Tornado():
    return render_template("Natural Disaster Info Pages/Tornado.html")

# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    app.run(debug=True,port=8000)