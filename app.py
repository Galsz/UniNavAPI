from flask import Flask, jsonify, request
from flask_cors import CORS
import json


with open("db.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

    bike_location = {
    "lat": -23.50032060569367, 
    "lng":  -47.397640478763826
}


app = Flask(__name__)
CORS(app)


@app.route('/locais',methods=['GET'])
def locais():
    query = request.args.get('name')
    if query:
        filtered_locais = [local for local in data if query.lower() in local['name'].lower()]
        return jsonify(filtered_locais)
    
    return jsonify(data)


@app.route('/bike-location', methods=['GET'])
def get_bike_location():
    if bike_location["lat"] is not None and bike_location["lng"] is not None:
        return jsonify(bike_location)
    return jsonify({"error": "Localização não disponível"}), 404

@app.route('/bike-location', methods=['POST'])
def update_bike_location():
    if not request.is_json:
        return jsonify({"error": "Formato de dados incorreto. Envie um JSON."}), 400

    data = request.get_json()

    if 'lat' in data and 'lng' in data:
        bike_location["lat"] = data['lat']
        bike_location["lng"] = data['lng']
        return jsonify({"message": "Localização atualizada com sucesso!"}), 200
    else:
        return jsonify({"error": "Os campos 'lat' e 'lng' são obrigatórios."}), 400


if __name__ == '__main__':
    app.run(debug=False)