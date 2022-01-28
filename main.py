from flask import render_template, request
from _init_ import app


from crud.app_crud import app_crud
from earthquakerating.app_earthquakerating import app_earthquakerating

from team.neha import app_neha
app.register_blueprint(app_neha)

from team.gigi import app_gigi
app.register_blueprint(app_gigi)

from team.christina import app_christina
app.register_blueprint(app_christina)

from team.anika import app_anika
app.register_blueprint(app_anika)

from team.allison import app_allison
app.register_blueprint(app_allison)

app.register_blueprint(app_crud)
app.register_blueprint(app_earthquakerating)

# create an instance of flask object


# home page accessed with http://127.0.0.1:5000/
@app.route("/",methods=['GET', 'POST'])
# map URL route for function below
def index():
    return render_template("index.html")

@app.route("/journal/")
def journal():
    return render_template("journals/journal.html")

@app.route("/staticsite/")
def staticsite():
    return render_template("layouts/staticsite.html")

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
    return render_template("pbl/week4/recent_updates.html")

@app.route("/disastermap/" , methods=['GET', 'POST'])
def disastermap():
    return render_template("pbl/week4/disastermap.html")

@app.route('/greet_disastermap', methods=['GET', 'POST'])
def greet_disastermap():
    # submit button has been pushed
    if request.form:
        comment = request.form.get("comment")
        if comment.__len__() != 0:  # input field has content
            return render_template("pbl/week4/disastermap.html", comment=comment)
        else:
            # starting and empty input default
            return render_template("pbl/week4/disastermap.html", comment="World")
            return render_template("pbl/week4/disastermap.html", comment="Bad input")
    else:
        return render_template("pbl/week4/disastermap.html")


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
    return render_template("pbl/week4/impacts.html")

@app.route("/world/")
def world():
    return render_template("pbl/week4/world.html")

@app.route("/weather_fun/")
def weather_fun():
    return render_template("pbl/week5/weather_fun.html")

@app.route("/animal/")
def animal():
    return render_template("pbl/week4/animal.html")

@app.route("/political/")
def political():
    return render_template("pbl/week4/political.html")

@app.route("/about/")
def about():
    return render_template("layouts/about.html")

@app.route("/Tornado/")
def Tornado():
    return render_template("Natural Disaster Info Pages/Tornado.html")

# from image import hide_msg
# @app.route("/rgbhide")
# def hidemsg():
#    hide_msg()

if __name__ == "__main__":
    app.run(debug=True,port=8000)