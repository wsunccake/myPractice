from flask import Blueprint, request

import math
import json


base_blueprint = Blueprint(
        'base',
        __name__,
        # url_prefix='/base'
)


def calculate_output(method, inputs, outputs):
    payload = json.dumps({'function': method,
                          'input': inputs,
                          'output': outputs})
    return payload


@base_blueprint.route('/sqrt/<string:input>', methods=['GET'])
def sqrt(input):
    number = float(input) if input.isdigit() else None
    output = math.sqrt(number) if number > 0 else 'NaN'

    return calculate_output('sqrt', [input], [str(output)])


@base_blueprint.route('/power')
def power():
    input1 = request.args.get('base')
    input2 = request.args.get('exponent')
    base = float(input1) if input1.isdigit() else 0
    exponent = float(input2) if input2.isdigit() else 0
    output = math.pow(base, exponent)

    return calculate_output('power', [input1, input2], [str(output)])

