from flask import Flask, jsonify, send_from_directory, abort
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

IMAGE_FOLDER = os.path.join(os.getcwd(), 'planets')

JSON_FILE = 'BD_Planets.json'

def load_json():
    with open(JSON_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

# Carregamento de todos os planetas
@app.route('/', methods=['GET'])
def homepage():
    data = load_json() 
    return jsonify(data)  # Retorna JSON diretamente

# Carregamento dos planetas pelo ID
@app.route('/<int:planet_id>')
def get_planet(planet_id):
    data = load_json()
    planet = next((p for p in data if p["Id"] == planet_id), None)
    if planet:
        return jsonify(planet)
    return jsonify({"error": "Planeta não encontrado"}), 404

# Carregamento das imagens pelo ID de cada planeta
@app.route('/<int:planet_id>/link')
def get_image(planet_id):
    data = load_json()
    planet = next((p for p in data if p["Id"] == planet_id), None)

    if planet:
        image_filename = planet["Link"]  
        image_path = os.path.join(IMAGE_FOLDER, image_filename)

        if os.path.exists(image_path):
            return send_from_directory(IMAGE_FOLDER, image_filename)
    
    return abort(404, "Imagem não encontrada")

if __name__ == '__main__':
    app.run(debug=True)
