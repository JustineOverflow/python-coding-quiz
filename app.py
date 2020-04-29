import random

from flask import Flask, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

hashquestions = {}


@app.route('/home')
def home():
    return "Welcome to this coding quiz!"


questions = {
    1: {
        "key": 1,
        "name": "Which of the following is not a programming language?",
        "answer": "Cobra",
        "choices": ["Cobra", "Python", "Swift"]
    },
    2: {
        "key": 2,
        "name": "Which company created the library React?",
        "answer": "Facebook",
        "choices": ["Apple", "Microsoft", "Facebook"]
    },
    3: {
        "key": 3,
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
    4: {
        "key": 4,
        "name": "Which of the following is a non relational database?",
        "answer": "MongoDB",
        "choices": ["SQL", "MongoDB", "Sequelize"]
    },
    5: {
        "key": 5,
        "name": "which function aims at adding an element to a hashmap?",
        "answer": "put",
        "choices": ["add", "push", "put"]
    },
    6: {
        "key": 6,
        "name": "Which computational complexity is the most time performant?",
        "answer": "o(logN)",
        "choices": ["o(n)", "o(nlogN)", "o(logN)"]
    },
    7: {
        "key": 7,
        "name": "You want to access the last element added to a list, you prefer to use:",
        "answer": "stack",
        "choices": ["Stack", "Queues", "LastIn"]
    },
    8: {
        "key": 8,
        "name": "Which of the following algorithms does not exist?",
        "answer": "fast sort",
        "choices": ["bubble sort", "fast sort", "selection sort"]
    },
    9: {
        "key": 9,
        "name": "in React, I can share data between different components using:",
        "answer": "props",
        "choices": ["route", "useState", "props"]
    },
    10: {
        "key": 10,
        "name": "Which of the following is a principle in clean code?",
        "answer": "DRY",
        "choices": ["DOY", "DRY", "DPY"]
    },

    11: {
        "key": 11,
        "name": "Which of the following is not a HTTP request?",
        "answer": "PUSH",
        "choices": ["PUT", "PUSH", "DELETE"]
    }
}


@app.route('/quiz')
def get_quiz():
    seenQuestions = map(int, request.args.get('seenQuestions').split(','))
    return random.choice([value for key, value in questions.items() if key not in seenQuestions])

@app.route('/check-answer')
def check_answer():
    guess = request.values['guess']
    key = int(request.values['key'])
    return str(questions[key]['answer'].lower() == guess.lower()).lower()



if __name__ == '__main__':
    app.run(debug=True, port=5000)
