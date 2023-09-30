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
