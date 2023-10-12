class GameStyle(ABC):  #Creacion del estilo de juego
    @abstractmethod
    def sayHi(self):
        pass

    @abstractmethod
    def sayPlay(self):
        pass


class FighterStyle(GameStyle):  #Estilo tipo peleador
    def sayHi(self):
        print("¡Listo para la batalla, camarada!")

    def sayPlay(self):
        print("¡Vamos a jugar! Yo cubriré tu espalda (҂◡̀_◡́)ᕤ")


class WizardStyle(GameStyle):   #Estilo tipo echicero
    def sayHi(self):
        print("Que los arcanos guíen tu camino.")

    def sayPlay(self):
        print("¡Vamos a jugar! Desde lejos lanzaré hechizos para ayudarte (◑_◑)")


class HealerStyle(GameStyle):   #Estilo tipo sanador
    def sayHi(self):
        print("Que la paz y curación te acompañen.")

    def sayPlay(self):
        print("¡Vamos a jugar! Estoy para curarte y no dejarte desfallecer (ɔ◔‿◔)ɔ ♥")


class Player:   #Creacion de jugador con sus estilos de juego
    def __init__(self, id, name, style: GameStyle):
        self.__id = id
        self.name = name
        self.style = style

    def getId(self):
        return self.__id

    def sayHi(self):
        self.style.sayHi()

    def sayPlay(self):
        self.style.sayPlay()


pepo = Player(1, "Pepo", FighterStyle())
pepo.sayHi()
pepo.sayPlay()
pepa = Player(2, "Pepa", WizardStyle())
pepa.sayHi()
pepa.sayPlay()
nana = Player(3, "Nana", HealerStyle())
nana.sayHi()
nana.sayPlay()

 








 