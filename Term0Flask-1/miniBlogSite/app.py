from flask import Flask, render_template, redirect, url_for, request

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    task = StringField('Task Description', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Submit')
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/add", methods = ["GET","POST"])

def add_task():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = form.task.data
            
            return render_template("home.html", message = "Task added successfully", form = form)
        else:
            return render_template("home.html", form=form)
        
        
            
if __name__ == '__main__':
    app.run(debug=True)