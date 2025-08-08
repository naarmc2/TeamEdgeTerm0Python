import datetime 
import random
from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/")

def home():
   return "Hello Nathania"

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/greet/<name>')

def greet_user(name):
    return render_template('greeting.html', name = name)

@app.route('/isPalindrome/<word>')

def isPalindrome(word):
    isPalindrome = False
    if word == word[ ::-1]:
        isPalindrome = True
    return render_template('isPalindrome.html', isPalindrome = isPalindrome, word = word)

@app.route('/diceStimulation')
 
def randomNumber():
    dice1= random.randint(1,6)
    dice2 = random.randint(1,6)
    
    double = False
    if dice1 == dice2:
        double = True
        
    return render_template("diceStimulation.html", dice1 = dice1, dice2 = dice2, double = double)

@app.route('/birthYear.html/yearBorn')

def calculateBirthYear(yearBorn):
    currentYear = 2025
    age = currentYear - yearBorn
    
    return render_template("age.html", yearBorn= yearBorn)
