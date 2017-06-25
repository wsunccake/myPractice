from flask import Flask, request

import math
import json


app = Flask(__name__)


def calculate_output(method, inputs, outputs):
    payload = json.dumps({'function': method,
                          'input': inputs,
                          'output': outputs})
    return payload


@app.route('/')
def home():
    return 'Hello Flask'


@app.route('/sqrt/<string:input>', methods=['GET'])
def sqrt(input):
    number = float(input) if input.isdigit() else None
    output = math.sqrt(number) if number > 0 else 'NaN'

    return calculate_output('sqrt', [input], [str(output)])


@app.route('/power')
def power():
    input1 = request.args.get('base')
    input2 = request.args.get('exponent')
    base = float(input1) if input1.isdigit() else 0
    exponent = float(input2) if input2.isdigit() else 0
    output = math.pow(base, exponent)

    return calculate_output('power', [input1, input2], [str(output)])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
