from flask import Flask, jsonify, request
from flask_cors import CORS
import json


with open("db.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

app = Flask(__name__)
CORS(app)


@app.route('/locais',methods=['GET'])
def locais():
    query = request.args.get('name')
    if query:
        filtered_locais = [local for local in data if query.lower() in local['name'].lower()]
        return jsonify(filtered_locais)
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)