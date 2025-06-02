import requests

URL = "http://10.87.6.166:5000"  # Reemplaza con la IP del servidor

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
