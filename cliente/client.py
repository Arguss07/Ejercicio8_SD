import requests

URL = "http://192.168.9.131:5000"  

pago = {
    "numero_tarjeta": 123456789,
    "monto": 1000,
    "nombre": "Juan Perez",
    "codigo_CVV": 456
}

compra = {
    "id_producto": 101,
    "precio": 250,
    "numero_productos": 4,
    "total": 1000
}

resp_pago = requests.post(f"{URL}/pagar", json=pago)
print("PAGAR:", "TRANSACCIÓN EXITOSA" if resp_pago.json()["success"] else "FALLÓ LA TRANSACCIÓN")

resp_compra = requests.post(f"{URL}/comprar", json=compra)
print("COMPRAR:", "COMPRA EXITOSA" if resp_compra.json()["success"] else "FALLÓ LA COMPRA")
