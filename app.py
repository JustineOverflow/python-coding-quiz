from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the coding quiz!"


class Question:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers


@app.route('/questions')
def getQuestions():
    questionsList = [
        {"name": "Which of the following is not a programming language?",
         "answer": "Cobra",
         "choices": ["Python", "Swift"]}]
    return json.dumps(questionsList)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
