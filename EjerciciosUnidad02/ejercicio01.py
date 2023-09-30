#  1- Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
#  guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
#  edad, años, vive en dirección y su número de teléfono es <teléfono>.

# Crear un diccionario vacío para almacenar la información del usuario
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

# Mostrar la información por pantalla
print(f"{usuario_info['Nombre']} tiene {usuario_info['Edad']} años, vive en {usuario_info['Dirección']} y su número de teléfono es {usuario_info['Teléfono']}.")
