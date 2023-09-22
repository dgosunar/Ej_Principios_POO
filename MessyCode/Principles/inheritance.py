from Entities.player import Player
from Entities.gameStyles import Fighter, Wizard, Healer

def inhExample():
    '''
        Inheritance example execution explained 
    '''
    
    print('\n\r\n\r........................................../ Herencia /..........................................\n\r\n\r')

    print('''          <<< La herencia nos permite crear objetos a partir de otros ya definidos. De esta manera, \n\r( ^o^)_/       creamos una super clase, de la cual, clases hijas podrán heredar sus atributos y métodos. >>>\n\r''')

    print("\n\r---> Por ejemplo, de la clase 'Player' extienden las clases 'Fighter', 'Wizard' y 'Healer'\n\rque serán jugadores pero con estilos especiales de juego.")
    print("Todos ellos estarán descritos por los atributos de una instancia de la clase 'Player' y podrán usar\n\rsus métodos. Además, tendrán atributos y métodos adicionales propios del estilo de juego de las clases hijas.")

    player3 = Player(3, 'Daniel')
    player4 = Fighter(4, 'Carolina', 'liviano')
    player5 = Wizard(5, 'Juan', 'Magia Negra')
    player6 = Healer(6, 'Fer', 'Bombas de vida')

    print("\n\rLos atributos del player3 de tipo 'Player' son:")
    print('    ID:', player3.getId())
    print('    Nombre:', player3.name)
    print('    Rango:', player3.rank)
    print('    Puntos Totales:', player3.getPoints())
    try:
        print("    Dificultad:", player3.difficulty)
    except AttributeError:
        print("    No posee atributo 'dificultad':")
        print("        AttributeError: 'Player' object has no attribute 'difficulty'")

    print("\n\rLos atributos del player4 de tipo 'Fighter' son:")
    print('    ID:', player4.getId())
    print('    Nombre:', player4.name)
    print('    Rango:', player4.rank)
    print('    Puntos Totales:', player4.getPoints())
    print("    Dificultad:", player4.difficulty)
    print("    Tipo de Fuerza:", player4.fightForce)

    print("\n\rLos atributos del player5 de tipo 'Wizard' son:")
    print('    ID:', player5.getId())
    print('    Nombre:', player5.name)
    print('    Rango:', player5.rank)
    print('    Puntos Totales:', player5.getPoints())
    print("    Dificultad:", player5.difficulty)
    print("    Tipo de Magia:", player5.magicType)

    print("\n\rLos atributos del player6 de tipo 'Healer' son:")
    print('    ID:', player6.getId())
    print('    Nombre:', player6.name)
    print('    Rango:', player6.rank)
    print('    Puntos Totales:', player6.getPoints())
    print("    Dificultad:", player6.difficulty)
    print("    Herramienta de sanación:", player6.healTool)

    print("\n\r---> Por ejemplo, la clase hija 'Healer' puede usar el método 'increasePoints()' de la clase padre 'Player'.\n\rY así mismo todas las otras instancias de clases hijas.")
    print("    Puntos iniciales player6:", player6.getPoints())
    print('    Rango Inicial player6:', player6.rank)
    player6.increasePoints(52)
    print("    Puntos después del incremento:", player6.getPoints())
    print('    Rango después del incremento:', player6.rank)

    print("\n\r\n\r(っ＾▿＾)っ Aquí termina 'herencia'.")
    print('.................................................................................................\n\r\n\r')