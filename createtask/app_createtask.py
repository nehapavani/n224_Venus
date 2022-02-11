from flask import Blueprint, render_template

app_createtask = Blueprint('createtask', __name__,
                         url_prefix='/createtask',
                         template_folder='templates/createtask/',
                         static_folder='static',
                         static_url_path='static/assets')


@app_createtask.route('/earthquakegraph')
def earthquakegraph():
    return render_template("earthquakegraph.html")