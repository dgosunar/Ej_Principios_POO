from Entities.player import Player
from Entities.gameStyles import Fighter, Wizard, Healer


def polyExample():
    """
    Polymorphism example execution explained
    """

    print(
        "\n\r\n\r........................................../ Polimorfismo /..........................................\n\r\n\r"
    )

    print(
        """          <<< El polimorfismo es darle "muchas formas" a un atributo o método en diferentes clases \n\r( ^o^)_/       teniendo el mismo nombre pero dándoles un valor o funcionalidad diferente. >>>\n\r"""
    )

    print(
        "--> Para el ejemplo crearemos 4 instancias, una de la clase padre 'Player' y otras tres\n\rinstancias de cada una de las clases hijas de 'Player'."
    )
    player7 = Player(7, "Cristian")
    player8 = Fighter(8, "Carlos", "Fuerte")
    player9 = Wizard(9, "Ana", "Poder vegetal")
    player10 = Healer(10, "Isa", "Torbellinos de agua")

    print(
        "\n\r* El player7 es de tipo 'Player' con id:",
        player7.getId(),
        "y nombre:",
        player7.name,
    )
    print(
        "* El player8 es de tipo 'Fighter' con id:",
        player8.getId(),
        ", nombre:",
        player8.name,
        "y tipo de fuerza:",
        player8.fightForce,
    )
    print(
        "* El player9 es de tipo 'Wizard' con id:",
        player9.getId(),
        ", nombre:",
        player9.name,
        "y tipo de magia:",
        player9.magicType,
    )
    print(
        "* El player10 es de tipo 'Healer' con id:",
        player10.getId(),
        ", nombre:",
        player10.name,
        "y herramienta de sanación:",
        player10.healTool,
    )

    print(
        "\n\rCada una de las clases hijas tomó los métodos 'sayHi()' y 'sayPlay()' de la clase padre 'Player'\n\r y los modificó acorde al estilo de juego propia. Así se les da 'forma diferente' según corresponda."
    )

    print("\n\rLos jugadores saludan con 'sayHi()':")
    print("Player 7:")
    player7.sayHi()
    print("Player 8:")
    player8.sayHi()
    print("Player 9:")
    player9.sayHi()
    print("Player 10:")
    player10.sayHi()

    print("\n\rLos jugadores invitan a jugar con 'sayPlay()':")
    print("Player 7:")
    player7.sayPlay()
    print("Player 8:")
    player8.sayPlay()
    print("Player 9:")
    player9.sayPlay()
    print("Player 10:")
    player10.sayPlay()

    print("\n\r\n\r(っ＾▿＾)っ Aquí termina 'polimorfismo'.")
    print(
        ".................................................................................................\n\r\n\r"
    )
