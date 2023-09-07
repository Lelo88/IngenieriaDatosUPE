# 04 - Realiza el algoritmo necesario para que la computadora te pregunte tu nombre y responda 
# con un saludo personalizado

from re import match

def greeting():
    while True:
        try:
            patron = "^[a-zA-Z]+$"
            nameAdded = input('Ingrese su nombre: ')
            assert len(nameAdded) > 0 , "El valor ingresado no es valido." 
            assert match(patron, nameAdded), "El valor ingresado no es valido."        
            return print(f'Hola {nameAdded}, bienvenido a tus primeros programas en Python!')
        except AssertionError as errorAssertion:
            print(errorAssertion)
        except ValueError as errorValue:
            print(errorValue)

greeting()