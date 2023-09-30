# 6 - Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos
# de los clientes de una empresa. El programa incorporar funciones crear el fichero con el
# listado si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo
# cliente y eliminar el teléfono de un cliente. El listado debe estar guardado en el fichero de
# texto telefono.txt donde el nombre del cliente y su teléfono deben aparecer separados por
# comas y cada cliente en una línea distinta.

import os

def crear_fichero_si_no_existe(nombre_fichero):
    if not os.path.exists(nombre_fichero):
        with open(nombre_fichero, 'w') as archivo:
            archivo.write('')

def consultar_telefono(nombre_cliente, nombre_fichero):
    with open(nombre_fichero, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            nombre, telefono = linea.strip().split(',')
            if nombre == nombre_cliente:
                return telefono
    return None

def agregar_cliente(nombre_cliente, telefono, nombre_fichero):
    with open(nombre_fichero, 'a') as archivo:
        archivo.write(f'{nombre_cliente},{telefono}\n')

def eliminar_cliente(nombre_cliente, nombre_fichero):
    with open(nombre_fichero, 'r') as archivo:
        lineas = archivo.readlines()
    with open(nombre_fichero, 'w') as archivo:
        for linea in lineas:
            nombre, _ = linea.strip().split(',')
            if nombre != nombre_cliente:
                archivo.write(linea)

nombre_fichero = 'telefono.txt'

crear_fichero_si_no_existe(nombre_fichero)

while True:
    print("\nMenú de Opciones:")
    print("1. Consultar teléfono de un cliente")
    print("2. Añadir teléfono de un nuevo cliente")
    print("3. Eliminar teléfono de un cliente")
    print("4. Salir")
    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == '1':
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        telefono = consultar_telefono(nombre_cliente, nombre_fichero)
        if telefono:
            print(f"El teléfono de {nombre_cliente} es: {telefono}")
        else:
            print(f"No se encontró el teléfono de {nombre_cliente}.")
    elif opcion == '2':
        nombre_cliente = input("Ingrese el nombre del nuevo cliente: ")
        telefono = input("Ingrese el teléfono del nuevo cliente: ")
        agregar_cliente(nombre_cliente, telefono, nombre_fichero)
        print(f"Se agregó el teléfono de {nombre_cliente} al listado.")
    elif opcion == '3':
        nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ")
        eliminar_cliente(nombre_cliente, nombre_fichero)
        print(f"Se eliminó el teléfono de {nombre_cliente} del listado.")
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
