# 4 - Escribir un programa que cree un diccionario simulando un carrito de la compra. El
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el
# usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el
# coste total, guardando la misma en un archivo JSon.

import json

# Crear un diccionario para el carrito de la compra
carrito = {}

# Función para solicitar y validar el precio del artículo
def obtener_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del artículo: "))
            if precio <= 0:
                raise ValueError("El precio debe ser un valor positivo.")
            return precio
        except ValueError as error:
            print(f"Error: {error}")

# Solicitar artículos y precios al usuario
while True:
    articulo = input("Ingrese el nombre del artículo (o 'terminar' para finalizar): ")
    if articulo.lower() == 'terminar':
        break
    precio = obtener_precio()
    carrito[articulo] = precio

# Mostrar la lista de la compra y el costo total
print("\nLista de la Compra:")
total = 0
for articulo, precio in carrito.items():
    print(f"{articulo}: ${precio:.2f}")
    total += precio
print(f"Costo Total: ${total:.2f}")

# Guardar la lista de la compra en un archivo JSON
nombre_archivo = input("Ingrese el nombre del archivo JSON para guardar la lista de la compra: ")
try:
    with open(nombre_archivo, 'w') as archivo:
        json.dump(carrito, archivo)
    print(f"La lista de la compra se ha guardado en '{nombre_archivo}'.")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
