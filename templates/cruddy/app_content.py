import os
from __init__ import app
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from cruddy.query import user2_by_id

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_content = Blueprint('content', __name__,
                        url_prefix='/content',
                        template_folder='templates/contenty/',
                        static_folder='static',
                        static_url_path='static')


# A global variable is used to provide feedback for session to users, but is considered short term solution
files_uploaded = []


# Page to upload content page
@app_content.route('/')
@login_required
def content():
    # grab user2 object (uo) based on current login
    uo = user_by_id(current_user.userID)
    user = uo.read()  # extract user record (Dictionary)
    # load content page
    return render_template('content.html', user=user, files=files_uploaded)


# Notes create/add
@app_content.route('/upload/', methods=["POST"])
@login_required
def upload():
    try:
        # grab file object (fo) from user input
        # The fo variable holds the submitted file object. This is an instance of class FileStorage, which Flask imports from Werkzeug.
        fo = request.files['filename']
        # save file to location defined in __init__.py
        # ... os.path uses os specific pathing for web server
        # ... secure_filename checks for integrity of name for operating system. Pass it a filename and it will return a secure version of it.

        fo.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(fo.filename)))
        # ... add to files_uploaded to give feedback of success on HTML page
        files_uploaded.insert(0, url_for('static', filename='uploads/' + fo.filename))
    except:
        # errors handled, but specific errors are not messaged to user
        pass
    # reload content page
    return redirect(url_for('content.content'))