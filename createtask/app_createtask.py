from flask import Blueprint, render_template
import requests, json

app_createtask = Blueprint('createtask', __name__,
                         url_prefix='/createtask',
                         template_folder='templates/createtask/',
                         static_folder='static',
                         static_url_path='static/assets')


@app_createtask.route('/earthquakegraph')
def earthquakegraph():
    return render_template("earthquakegraph.html")

@app_createtask.route("/earthquake_monitor/")
def earthquake_monitor():
    url = "https://earthquake-monitor.p.rapidapi.com/recent"

    headers = {
        'x-rapidapi-host': "earthquake-monitor.p.rapidapi.com",
        'x-rapidapi-key': "4ab4681ba9mshf17197c9d59be44p17d1edjsnabe7ccc22eb5"
    }

    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    print(response.text)
    return render_template("earthquakem.html", Z=output)