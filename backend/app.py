from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FILE_NAME = "names.txt"

@app.route('/save', methods=['POST'])
def save_name():
    data = request.json
    name = data.get('name')

    with open(FILE_NAME, 'a') as file:
        file.write(name + '\n')

    return jsonify({"message": "Name saved successfully"})


@app.route('/names', methods=['GET'])
def get_names():
    try:
        with open(FILE_NAME, 'r') as file:
            names = file.readlines()

        names = [name.strip() for name in names]

    except FileNotFoundError:
        names = []

    return jsonify(names)


if __name__ == '__main__':
    app.run(debug=True)
