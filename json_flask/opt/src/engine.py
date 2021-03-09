#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, session
import json
from flask_socketio import SocketIO
import sys
from flask_cors import CORS
import wave
from datetime import datetime
import requests
import waitress

async_mode = None
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode = async_mode)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route("/", methods=['POST'])
def json_flask():
    result = {}
    if request.method == "POST":
        data = request.data.decode('utf-8')
        data = json.loads(data)
    print(data)

    name = data['name']
    password = data['pass']

    if name == 'rirma' and password == 'rirmadesu':
        result['authentication_result'] = 'successful'
        print('authentication_successful')
    else:
        result['authentication_result'] = 'failure'
        print('authentication_failure')

    return json.dumps(result)


if __name__ == "__main__":
    waitress.serve(app, host='0.0.0.0', port=10033)