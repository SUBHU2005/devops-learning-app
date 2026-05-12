from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

PORT = os.getenv("PORT")
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["devopsdb"]

collection = db["names"]

@app.route('/save', methods=['POST'])
def save_name():

    data = request.json

    name = data.get('name')

    collection.insert_one({"name": name})

    return jsonify({"message": "Name saved successfully"})


@app.route('/names', methods=['GET'])
def get_names():

    names = collection.find()

    result = []

    for item in names:
        result.append(item["name"])

    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(PORT))