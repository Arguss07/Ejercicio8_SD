# 🛒 Emulación de Transacciones de Compra con Web Services - Tarea 8A

Este proyecto tiene como objetivo simular transacciones financieras básicas mediante la implementación de **dos Web Services** (RESTful), y un **cliente de escritorio** que los consume. Los servicios están diseñados para:

- Procesar pagos (`/pagar`)
- Realizar compras (`/comprar`)

## 🎯 Objetivo

Comprender el ciclo completo de **creación, despliegue y consumo** de servicios web. Se simulan flujos básicos como el pago con tarjeta y la compra de productos.

## 📦 Estructura del Proyecto

📁 servidor/
└── app.py # Web service con Flask
📁 cliente/
└── cliente.py # Cliente de escritorio que consume los servicios

## 🚀 Tecnologías

- Python 3.x
- Flask (para servicios REST)
- requests (para consumo desde cliente)
- JSON (como formato de intercambio)

## 🧪 Pruebas Realizadas

- ✅ `Pagar(123456789, 1000, "Juan Perez", 456)`
- ✅ `Comprar(101, 250, 4, 1000)`

## 📷 Capturas de ejecución

> Se incluyen en la carpeta `/screenshots`.

## 🔧 Ejecución local

1. Instala dependencias:
pip install flask requests

2. Corre el servidor:
cd servidor
python app.py

3. Ejecuta el cliente:
cd cliente
python cliente.py
---

