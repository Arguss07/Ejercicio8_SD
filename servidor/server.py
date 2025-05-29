from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulamos un saldo inicial
saldo_tarjeta = {
    "123456789": 1500  # número de tarjeta y su saldo
}

@app.route('/pagar', methods=['POST'])
def pagar():
    datos = request.get_json()
    numero_tarjeta = str(datos['numero_tarjeta'])
    monto = datos['monto']
    nombre = datos['nombre']
    codigo_CVV = datos['codigo_CVV']

    if numero_tarjeta in saldo_tarjeta and saldo_tarjeta[numero_tarjeta] >= monto:
        saldo_tarjeta[numero_tarjeta] -= monto
        return jsonify({"resultado": True, "mensaje": "TRANSACCIÓN EXITOSA"})
    else:
        return jsonify({"resultado": False, "mensaje": "FALLÓ LA TRANSACCIÓN"})

@app.route('/comprar', methods=['POST'])
def comprar():
    datos = request.get_json()
    id_producto = datos['id_producto']
    precio = datos['precio']
    numero_productos = datos['numero_productos']
    total = datos['total']

    if precio * numero_productos == total:
        return jsonify({"resultado": True, "mensaje": "COMPRA EXITOSA"})
    else:
        return jsonify({"resultado": False, "mensaje": "FALLÓ LA COMPRA"})

if __name__ == '__main__':
    app.run(debug=True)
