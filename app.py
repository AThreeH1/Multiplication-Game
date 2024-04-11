from flask import Flask, render_template, request, jsonify
import random
import json
import time

app = Flask(__name__)

@app.route('/')
def index():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return render_template('index.html', num1=num1, num2=num2)

@app.route('/submit', methods=['POST'])
def submit():
    answer = int(request.form['answer'])
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    is_correct = answer == num1 * num2

    return jsonify({'correct': is_correct})

if __name__ == '__main__':
    app.run(debug=True)
