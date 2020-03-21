import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the coding quiz!"


questionsList = [
    {
        "id": 1,
        "name": "Which of the following is not a programming language?",
        "answer": "Cobra",
        "choices": ["Cobra", "Python", "Swift"]
    }
]


@app.route('/quiz')
def get_quiz():
    question = random.choice(questionsList)
    return jsonify(question)

    # question =
    # question_id = request.args.get('question_id')
    # return '{}'.format(question)

    # score = 0
    #
    # for qItem in questionsList:
    #     print(qItem.question)
    #     print("Here are the possible answers:")
    #     possible = qItem.otherAnswers + [qItem.correctAnswer]
    #     random.shuffle(possible)
    #     count = 0
    #     while count < len(possible):
    #         print(str(count + 1) + ": " + possible[count])
    #         count += 1
    #     print("Please enter the number of your answer:")
    #     userAnswer = raw_input()
    #     while not userAnswer.isdigit() or not 0 < int(userAnswer) <= len(possible):
    #         print("Try again - please enter a valid number:")
    #         userAnswer = raw_input()
    #     userAnswer = int(userAnswer)
    #     if possible[userAnswer - 1] == qItem.correctAnswer:
    #         print("Correct answer!")
    #         score += 1
    #     else:
    #         print("Wrong answer")
    #         print("Correct answer was: " + qItem.correctAnswer)
    #         print("")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
