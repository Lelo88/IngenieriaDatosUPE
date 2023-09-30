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
