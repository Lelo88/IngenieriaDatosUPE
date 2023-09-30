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

import json

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
