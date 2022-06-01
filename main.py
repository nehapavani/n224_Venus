# from flask import Flask
from flask import render_template
from templates.cruddy.app_crud import app_crud
from templates.cruddy.app_crud_api import app_crud_api
from templates.cruddy.app_wish import app_wish
from templates.cruddy.app_wish_api import app_wish_api
from __init__ import app

# app = Flask(__name__)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_wish)
app.register_blueprint(app_wish_api)


@app.route('/')
# map URL route for function below
def index():
    return render_template("index.html")


@app.route('/shopnow', methods=['GET','POST'])
def shopnow():
    return render_template("shopnow.html")


@app.route('/feedback', methods=['GET','POST'])
def feedback():
    return render_template("feedback.html")


@app.route('/blog', methods=['GET','POST'])
def blog():
    return render_template("blog.html")


@app.route('/size', methods=['GET','POST'])
def size():
    return render_template("size.html")


@app.route('/quiz', methods=['GET','POST'])
def quiz():
    return render_template("quiz.html")


if __name__ == "__main__":
    app.run(debug=True)
