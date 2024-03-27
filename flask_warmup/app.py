#! /usr/bin/python

from flask import Flask, jsonify

app = Flask(__name__)

def evaluate(op, num1, num2):
    num1, num2 = int(num1), int(num2)
    if op == 'plus':
        return num1 + num2
    elif op == 'minus':
        return num1 - num2
    elif op == 'times':
        return num1 * num2
    return num1/num2

@app.route('/<op>/<num1>/<num2>/')
def operation(op, num1, num2):
    data = {
        'question': op,
        'inputs': [num1, num2],
        'answer': evaluate(op, num1, num2)
    }
    return(jsonify(data))

app.run(host = '0.0.0.0', port = 5127)