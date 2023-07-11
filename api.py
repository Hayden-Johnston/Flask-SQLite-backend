# author: Hayden Johnston
# github: hgjohn
# date: 07/11/2023
# description: API routes for Flask backend.

from flask import request, jsonify
from flask_restful import Api
from app import app, get_db, delete_db, insert_db

api = Api(app)

@app.route('/api/db/add/', methods=['POST'])
def add_db():
    med = request.get_json()
    print(med)
    return jsonify(insert_db(med))

@app.route('/api/db/', methods=['GET'])
def get_all_meds():
    return jsonify(get_db())

@app.route('/api/db/<name>', methods=['GET'])
def get_db_by_name(name):
    return jsonify(get_db_by_name(name))

@app.route('/api/db/update/', methods=['PUT'])
def update_med():
    med = request.get_json()
    return jsonify(update_med(med))

@app.route('/api/db/delete/', methods=['DELETE'])
def delete_meds(name):
    return jsonify(delete_db(name))
