from Principles.abstraction import absExample
from Principles.encapsulation import enExample
from Principles.inheritance import inhExample
from Principles.polymorphism import polyExample

print("\n\r\n\r------------------------------# Principios Básicos de POO #----------------------------- \n\r\n\r ¡Hola!  (•◡•)/")

running = True

while running:
    print('''
        Ruta de Aprendizaje:
            1) Abstracción
            2) Encapsulamiento
            3) Herencia
            4) Polimorfismo
            
        -> Presiona cualquier letra para salir
    ''')
    option = input('¿Qué quieres aprender? \n\rEscribe el número correspondiente: ')

    if option == "1":
        absExample()
    elif option == "2":
        enExample()
    elif option == "3":
        inhExample()
    elif option == "4":
        polyExample()
    else:
        running = False

print('\n\r\n\r¡Bye! (^◡^)/')