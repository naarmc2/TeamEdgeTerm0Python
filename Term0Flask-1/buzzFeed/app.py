from flask import Flask, render_template, request
from flask_wtf import FlaskForm
app = Flask(__name__)

QandA = {
    "Q1":{"ID": 1, "Question": "Which fruit is debatable?", "Options": ["apple","tomato","banana"], "answer":"tomato"},
    "Q2":{"ID": 2, "Question": "Which of these fruit has the largest seed? ", "Options": ["avocado","blueberry","cherry"], "Answer":"avocado"},
    "Q3":{"ID": 3, "Question": "Which fruit is poisonous when eaten raw? ", "Options": ["ackee","naseberry","starfruit"], "Answer":"ackee"},
    "Q4":{"ID": 4, "Question": "Which fruit is NOT used in a pina cola?", "Options": ["coconut","pineapple","papaya"], "Answer":"papaya"},
    "Q5":{"ID": 5, "Question": "Which fruit of these fruits is green on the inside?", "Options": ["dragonfruit","kiwi","banana"], "Answer":"kiwi"}, 
}

@app.route('/')
def index():
    return render_template ('index.html', QandA=QandA)

@app.route('/index', methods=['POST'])

def generateQuiz():
    user_answers = {key: value for key, value in request.form.items()}
    score, total_questions = calculate_score(user_answers)
    return render_template('results.html', title='Quiz Result', score=score, total_questions=total_questions)

def calculate_score(user_answers):
    score = 0
    total_questions = len(QandA['Question'])

    for question in QandA['questions']:
        question_id = question['id']
        user_answer = user_answers.get(str(question_id))  # Convert question_id to string
        if user_answer and user_answer == question['Answer']:
            score += 1

    return score, total_questions


if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = 3000)