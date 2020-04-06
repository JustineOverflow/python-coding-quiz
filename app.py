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
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
    6: {
        "key": 6,
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
    7: {
        "key": 7,
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
    8: {
        "key": 8,
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
    9: {
        "key": 9,
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
    10: {
        "key": 10,
        "name": "Which library could replace Express?",
        "answer": "Koa",
        "choices": ["Koa", "NPM", "NodeJS"]
    },
}


@app.route('/quiz')
def get_quiz():
    random_key = random.choice(questions.keys())

    while random_key in hashquestions.keys():
        random_key = random.choice(questions.keys())

    question = questions[random_key]
    hashquestions[random_key] = questions

    return question


@app.route('/check-answer')
def check_answer():
    guess = request.values['guess']
    key = int(request.values['key'])
    return str(questions[key]['answer'].lower() == guess.lower()).lower()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
