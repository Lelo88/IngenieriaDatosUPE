# 07 - Desarrolle un algoritmo que permita leer un valor cualquiera y escriba si dicho numero es par o impar

def isOddNumber():
    while True:
        try:
            number = int(input("Ingrese un numero: "))
            if number % 2 == 0:
                return print(f"El numero {number} es par")
            else:
                return print(f"El numero {number} es impar")
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)

isOddNumber()