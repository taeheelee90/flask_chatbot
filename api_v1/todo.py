from flask import jsonify
from flask import request
from flask import Blueprint
import requests

from . import api

@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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', json ={
            'text': 'Hello members in slack!'
        }, headers={'Content-Type': 'application/json'})
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)

# Separate test method for Slash command
@api.route('/test', methods=['POST'])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)
        