from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#everything is stored here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#initializes the database
db = SQLAlchemy(app)

class Todo(db.Model):
    #columns in the database
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    #automatically sets
    date_created = db.Column(db.Datetime, default= (datetime.timezone.utc))
    
    def __repre__(self):
        #returns task and id when new element is created
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)