from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pagar', methods=['POST'])
def pagar():
    data = request.json
    if data["numero_tarjeta"] == 123456789 and data["monto"] <= 1000:
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/comprar', methods=['POST'])
def comprar():
    data = request.json
    if data["total"] == data["precio"] * data["numero_productos"]:
        return jsonify({"success": True})
    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
