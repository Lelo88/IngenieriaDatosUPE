# 05 - En este ejercicio se va a calcular la edad de una madre en el momento de dar a luz a alguno de sus hijos

from datetime import datetime, timedelta

def motherAgeAtBirthChild():
    fecha_cumpleanos_madre = datetime.strptime(input("Ingrese la fecha de cumpleaños de la madre (YYYY-MM-DD): "), "%Y-%m-%d")
    edad_madre_en_cumpleanos = int(input("Ingrese la edad de la madre en su cumpleaños: "))

    fecha_nacimiento_hijo = datetime.strptime(input("Ingrese la fecha de nacimiento del hijo (YYYY-MM-DD): "), "%Y-%m-%d")
    fecha_concepcion_hijo = fecha_nacimiento_hijo - timedelta(days=9*30)

    diferencia_de_edad = fecha_concepcion_hijo.year - fecha_cumpleanos_madre.year

    if fecha_cumpleanos_madre.month > fecha_concepcion_hijo.month or (fecha_cumpleanos_madre.month == fecha_concepcion_hijo.month and fecha_cumpleanos_madre.day > fecha_concepcion_hijo.day):
        edad_madre_en_parto = edad_madre_en_cumpleanos - diferencia_de_edad
    else:
        edad_madre_en_parto = edad_madre_en_cumpleanos - diferencia_de_edad - 1

    return print(f"La edad de la madre en la fecha de nacimiento del hijo es de aproximadamente {edad_madre_en_parto} años.")

def inputValue05():
    while True:
        try:
            motherAgeAtBirthChild()
            break
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
            
inputValue05() 