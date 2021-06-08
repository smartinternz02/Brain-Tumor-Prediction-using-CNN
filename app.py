from flask import Flask ,render_template,request
from flask.helpers import flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired
from wtforms.fields import FileField
from flask_wtf.file import FileAllowed, FileRequired
from prediction import prediction
from PIL import Image
import secrets
import os


class MRIFileForm(FlaskForm):
    file = FileField("MRI image",validators=[FileRequired(),FileAllowed(["jpg","jpeg","png"])])

app = Flask(__name__) 
app.config['SECRET_KEY'] = '123456789'
# app is routed 
def save_picture(file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(file.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('static\TI',picture_fn)
    i = Image.open(file)
    i.save(picture_path)
    return picture_fn

@app.route('/',methods=["GET","POST"])
def display():
    form = MRIFileForm()
    if request.method == "GET":
        return render_template("index.html",form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            file = form.file.data
            saved_picture = save_picture(file)
            result = prediction(saved_picture)
            if result == "no":
                alert = "success"
                flash('No tumor has been Detected!!',alert)
            elif result == "yes":
                alert="danger"
                flash('Tumor has been Detected!!',alert)
            return render_template('index.html',form=form)


if __name__ == '__main__':
    app.run(debug = True) 






