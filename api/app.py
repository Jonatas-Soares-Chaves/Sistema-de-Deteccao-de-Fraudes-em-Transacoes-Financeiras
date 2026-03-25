import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from scripts.fraud_engine import calcular_risco, classificar

app = Flask(__name__)

@app.route("/analisar", methods=["POST"])
def analisar():
    dados = request.json

    score = calcular_risco(dados)
    status = classificar(score)

    return jsonify({
        "risco": score,
        "classificacao": status
    })

if __name__ == "__main__":
    app.run(debug=True)