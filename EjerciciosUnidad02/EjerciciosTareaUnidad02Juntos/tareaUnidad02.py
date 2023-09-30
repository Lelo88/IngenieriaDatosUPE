import json, os

#  1- Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
#  guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
#  edad, años, vive en dirección y su número de teléfono es <teléfono>.

usuario_info = {}

def obtener_input(prompt):
    while True:
        try:
            entrada = input(prompt)
            if not entrada:
                raise ValueError("Este campo no puede estar vacío.")
            return entrada
        except ValueError as error:
            print(f"Error: {error}")


nombre = obtener_input("Ingrese su nombre: ")
edad = obtener_input("Ingrese su edad: ")
direccion = obtener_input("Ingrese su dirección: ")
telefono = obtener_input("Ingrese su número de teléfono: ")


usuario_info["Nombre"] = nombre
usuario_info["Edad"] = edad
usuario_info["Dirección"] = direccion
usuario_info["Teléfono"] = telefono

print(f"{usuario_info['Nombre']} tiene {usuario_info['Edad']} años, vive en {usuario_info['Dirección']} y su número de teléfono es {usuario_info['Teléfono']}.")


# --------------------------------------------------------------------------------------------------

# 2- Escribir un programa que guarde en un diccionario los precios de las frutas, pregunte al
# usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número
# de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando
# de ello.

precios_frutas = {
    "manzana": 1.2,
    "banana": 0.8,
    "pera": 1.0,
    "naranja": 1.5,
}

while True:
    try:
        fruta = input("Ingrese el nombre de la fruta: ").lower()  
        kilos = float(input("Ingrese la cantidad en kilos: "))
        
        if fruta in precios_frutas:
            precio_total = precios_frutas[fruta] * kilos
            print(f"El precio de {kilos} kilos de {fruta} es ${precio_total:.2f}")
            break
        else:
            print(f"{fruta} no está en la lista de frutas disponibles.")
    except ValueError:
        print("Por favor, ingrese una cantidad válida en kilos.")


# -----------------------------------------------------------------------------------------------

# 3. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que
# se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del
# diccionario.

persona_info = {}

def obtener_input(prompt):
    while True:
        try:
            entrada = input(prompt)
            if not entrada:
                raise ValueError("Este campo no puede estar vacío.")
            return entrada
        except ValueError as error:
            print(f"Error: {error}")


print("Ingrese información sobre la persona:")
persona_info["Nombre"] = obtener_input("Nombre: ")
persona_info["Edad"] = obtener_input("Edad: ")
persona_info["Sexo"] = obtener_input("Sexo: ")
persona_info["Teléfono"] = obtener_input("Teléfono: ")
persona_info["Correo Electrónico"] = obtener_input("Correo Electrónico: ")


print("\nContenido del diccionario:")
for clave, valor in persona_info.items():
    print(f"{clave}: {valor}")


# ------------------------------------------------------------------------------

# 4 - Escribir un programa que cree un diccionario simulando un carrito de la compra. El
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el
# usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el
# coste total, guardando la misma en un archivo JSon.

carrito = {}

def obtener_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del artículo: "))
            if precio <= 0:
                raise ValueError("El precio debe ser un valor positivo.")
            return precio
        except ValueError as error:
            print(f"Error: {error}")

while True:
    articulo = input("Ingrese el nombre del artículo (o 'terminar' para finalizar): ")
    if articulo.lower() == 'terminar':
        break
    precio = obtener_precio()
    carrito[articulo] = precio

print("\nLista de la Compra:")
total = 0
for articulo, precio in carrito.items():
    print(f"{articulo}: ${precio:.2f}")
    total += precio
print(f"Costo Total: ${total:.2f}")

nombre_archivo = input("Ingrese el nombre del archivo JSON para guardar la lista de la compra: ")
try:
    with open(nombre_archivo, 'w') as archivo:
        json.dump(carrito, archivo)
    print(f"La lista de la compra se ha guardado en '{nombre_archivo}'.")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")

# ---------------------------------------------------------------------------------

# 5 - El directorio de los clientes de una empresa está organizado en una cadena de texto
# como la de más abajo, donde cada línea contiene la información del nombre, email,
# teléfono, CUIT, y el descuento que se le aplica. Las líneas se separan con el carácter de
# cambio de línea \n y la primera línea contiene los nombres de los campos con la información
# contenida en el directorio.
# "cuit;nombre;email;teléfono;descuento\n01234567L;Luis
# González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena
# Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José
# Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen
# Sánchez;carmen@mail.com;667677855;15.7"
# Escribir un programa que genere un diccionario con la información del directorio, donde
# cada elemento corresponda a un cliente y tenga por clave su cuit y por valor otro
# diccionario con el resto de la información del cliente. Los diccionarios con la información de
# cada cliente tendrán como claves los nombres de los campos y como valores la información
# de cada cliente correspondientes a los campos y persistirlos en un archivo JSon.

directorio_clientes = """cuit;nombre;email;teléfono;descuento
01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5
71476342J;Macarena Ramírez;macarena@mail.com;692839321;8
63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2
98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lineas = directorio_clientes.split('\n')

campos = lineas[0].split(';')

directorio_diccionario = {}

for linea in lineas[1:]:
    valores = linea.split(';')
    cuit = valores[0]
    cliente_info = {}
    for i in range(1, len(campos)):
        cliente_info[campos[i]] = valores[i]
    directorio_diccionario[cuit] = cliente_info

nombre_archivo = "directorio_clientes.json"
try:
    with open(nombre_archivo, 'w') as archivo:
        json.dump(directorio_diccionario, archivo, indent=4)
    print(f"El directorio de clientes se ha guardado en '{nombre_archivo}'.")
except Exception as e:
    print(f"Error al guardar el archivo JSON: {e}")


# ------------------------------------------------------------------------------------------------------

# 6 - Escribir un programa para gestionar un listado telefónico con los nombres y los teléfonos
# de los clientes de una empresa. El programa incorporar funciones crear el fichero con el
# listado si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo
# cliente y eliminar el teléfono de un cliente. El listado debe estar guardado en el fichero de
# texto telefono.txt donde el nombre del cliente y su teléfono deben aparecer separados por
# comas y cada cliente en una línea distinta.

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

