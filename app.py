#!/usr/bin/env python
import json
from flask import Flask, jsonify, abort, make_response
APP = Flask(__name__)

MASCOTS = json.load(open('data.json', 'r'))
@APP.route('/', methods=['GET'])
def get_mascots():
    return jsonify(MASCOTS)

@APP.route(guid):
    for mascot in MASCOTS:
        if guid == mascot['guid']:
            return jsonify(mascot)

    abort(404)
    return None

@APP.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)

if __name == "__main__":
    APP.run("0.0.0.0", debug=True)