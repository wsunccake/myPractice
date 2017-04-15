import json
from flask import Flask, request, jsonify
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def home():
    return 'Hello Flask'


@app.route('/say/<string:user>')
def say(user):
    return 'Hello {}'.format(user)


@app.route('/ask', methods=['GET'])
def ask():
    user = request.args.get('user')
    return 'Hello {}'.format(user) 


@app.route('/tell', methods=['POST'])
def tell():
    # print('request.header:\n{}\n'.format(request.headers))
    # print('request.form:\n{}\n'.format(request.form))
    # print('request.data:\n{}\n'.format(request.data))
    # print('request.json:\n{}\n'.format(request.json))

    if request.headers['Content-Type'] == 'text/plain':
        result = request.data
    elif request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        # user = request.form['user']
        result = 'Hello {}'.format(request.form['user'])
    elif request.headers['Content-Type'] == 'application/json':
        # user = json.loads(json.dumps(request.json))['user']
        result = jsonify({'user': request.json['user']})
    else:
        result = 'Hello Flask'
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

