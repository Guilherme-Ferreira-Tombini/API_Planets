from flask import Flask, Response
import json

app = Flask(__name__)

# Carrega o JSON
with open('BD_Planets.json') as f:
    data = json.load(f)

@app.route('/')
def homepage():
    # Apresenta os dados do JSON na rota raiz da API
    json_data = json.dumps(data, indent=4)
    return Response(json_data, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)
