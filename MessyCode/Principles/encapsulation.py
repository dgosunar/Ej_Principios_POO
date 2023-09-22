from Entities.player import Player

def enExample():
    '''
        Encapsulation example execution explained 
    '''

    print('\n\r\n\r......................................../ Encapsulamiento /........................................\n\r\n\r')

    print('''          <<< El encapsulamiento es una manera de proteger los atributos y métodos de \n\r( ^o^)_/      las entidades que representan nuestras clases para que no sean de fácil acceso. >>>\n\r''')

    print("Por ejemplo, dada una instancia de la clase 'Player':\n\r")
    player2 = Player(2, 'Paula')

    print("Encontramos que el atributo 'id' es privado. Por lo tanto no tenemos acceso a este y nos genera un error.")
    try:
        print("    ID", player2.__id)
    except AttributeError:
        print("    AttributeError: 'Player' object has no attribute '__id'")
    print("--> Por esto se crea el getter para ese atributo.")
    print("         ID:", player2.getId())

    print("\n\rLo mismo sucede con el método 'defineRank()', es privado y solo accesible dentro de la clase.")
    try:
        player2.__defineRank()
    except AttributeError:
        print("    AttributeError: 'Player' object has no attribute '__defineRank'")

    print("\n\r\n\r(っ＾▿＾)っ Aquí termina 'encapsulamiento'.")
    print('.................................................................................................\n\r\n\r')