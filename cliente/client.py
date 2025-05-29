import requests

# Endpoint base del servidor
URL = "http://127.0.0.1:5000"

# Prueba 1: Pagar
pago = {
    "numero_tarjeta": 123456789,
    "monto": 1000,
    "nombre": "Juan Perez",
    "codigo_CVV": 456
}

resp_pago = requests.post(f"{URL}/pagar", json=pago)
print("PAGAR:", resp_pago.json()["mensaje"])

# Prueba 2: Comprar
compra = {
    "id_producto": 101,
    "precio": 250,
    "numero_productos": 4,
    "total": 1000
}

resp_compra = requests.post(f"{URL}/comprar", json=compra)
print("COMPRAR:", resp_compra.json()["mensaje"])
