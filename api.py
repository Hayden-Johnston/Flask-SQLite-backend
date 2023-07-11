# author: Hayden Johnston
# github: hgjohn
# date: 07/11/2023
# description: API routes for Flask backend.

from flask import request, jsonify
from flask_restful import Api
from app import app, get_db, delete_db, insert_db, get_by_name, update_db

api = Api(app)

@app.route('/api/db/add/', methods=['POST'])
def add_entry():
    item = request.get_json()
    # print(item)
    return jsonify(insert_db(item))

@app.route('/api/db/', methods=['GET'])
def get_all():
    return jsonify(get_db())

@app.route('/api/db/<name>', methods=['GET'])
def get_entry_by_name(name):
    return jsonify(get_by_name(name))

@app.route('/api/db/update/', methods=['PUT'])
def update_entry():
    item = request.get_json()
    return jsonify(update_db(item))

@app.route('/api/db/delete/<name>', methods=['DELETE'])
def delete_entry(name):
    return jsonify(delete_db(name))