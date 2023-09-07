from datetime import datetime, timedelta
from math import pow, sqrt
from re import match

# 01 - Determinar el area de un cuadrado
def validateInput():
    while True:
        try: 
            sideAdded = int(input('Ingrese el tamaño del lado del cuadrado: '))
            assert sideAdded > 0 , "El valor ingresado no es valido."
            print("Ingreso exitoso")       
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
        else: 
            return sideAdded  
        finally:
            print("Intentelo nuevamente")   
    
def squareArea(sideAdded):
    return  print(f'El area del cuadrado ingresado es {int(pow(sideAdded, 2))}')

side = validateInput()
squareArea(side)

# 02 - Determinar el perimetro de un cuadrado
def validateInput02():
    while True:
        try: 
            sideAdded = int(input('Ingrese el tamaño del lado del cuadrado: '))
            assert sideAdded > 0 , "El valor ingresado no es valido."
            print("Ingreso exitoso")
            squarePerimeter(sideAdded)
            break       
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
 
def squarePerimeter(side):
    return print(f'El perimetro del cuadrado ingresado es {side * 4}')

validateInput02()

# 03 - Realiza el algoritmo necesario para crear un programa que sume dos numeros enteros
def validateInput03():
    while True:
        try: 
            number1 = int(input('Ingrese el primer numero a sumar: '))
            number2 = int(input('Ingrese el segundo numero a sumar: '))
            print("Ingreso exitoso")
            sumNumbers(number1, number2)
            break    
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
    
def sumNumbers(number1, number2):
    return print(f'La suma de los números ingresados es {number1 + number2}')

validateInput03()

# 04 - Realiza el algoritmo necesario para que la computadora te pregunte tu nombre y responda 
# con un saludo personalizado

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

# 05 - En este ejercicio se va a calcular la edad de una madre en el momento de dar a luz a alguno de sus hijos

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

# 06 - Determinar la hipotenusa de un triangulo rectangulo conocidas las longitudes de sus dos catetos. 

def validateInput06():
    while True:
        try: 
            number1 = float(input('Ingrese la longitud del cateto opuesto: '))
            number2 = float(input('Ingrese la longitud del cateto adyacente: '))
            assert (number1 > 0 and number2 > 0) , "El valor ingresado es menor a cero. No condice a un lado del triangulo con valor positivo"
            print("Ingreso exitoso")
            calculateHipotenuse(number1, number2)
            break    
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)
    
def calculateHipotenuse(number1, number2):
    return print(f'La hipotenusa de los catetos ingresados es {round(sqrt(pow(number1, 2) + pow(number2, 2)), 2)}')

validateInput06()

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

# 08 - Crear un algoritmo que muestre por pantalla el doble y el triple de un numero ingresado por teclado

def doubleAndTriple(number):
    return print(f"El doble de {number} es {number * 2} y el triple de {number} es {number * 3}")
def inputValue08():
    while True: 
        try:
            numero = int(input("Ingrese un numero: "))
            assert type(numero) == int, "El valor ingresado no es valido."
            doubleAndTriple(numero)
            break
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)

inputValue08()

# 09 -  Diseñar un algoritmo que imprima el cuadrado y el cubo de un numero ingresado por teclado

def doubleAndTriple(number):
    return print(f"El cuadrado de {number} es {int(pow(number, 2))} y el cubo de {number} es {int(pow(number, 3))}")
def inputValue09():
    while True: 
        try:
            numero = int(input("Ingrese un numero: "))
            assert type(numero) == int, "El valor ingresado no es valido."
            doubleAndTriple(numero)
            break
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)

inputValue09()

# 10 - Diseñar un numero que pida un numero por teclado y luego imprima el numero del siguiente a ingresado

def inputValue10():
    while True: 
        try:
            numero = int(input("Ingrese un numero: "))
            assert type(numero) == int, "El valor ingresado no es valido."
            return print(f'El siguiente al numero {numero} es {numero + 1}')
        except ValueError as error_Value:
            print(error_Value)
        except AssertionError as assertionError:
            print(assertionError)

inputValue10()