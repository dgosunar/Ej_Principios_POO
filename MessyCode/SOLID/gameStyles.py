from abc import abstractmethod, ABC
class GameStyle(ABC):
    @abstractmethod
    def sayHi(self):
        pass
    @abstractmethod
    def sayPlay(self):
        pass
class FighterStyle(GameStyle):
    def sayHi(self):
        print("¡Listo para la batalla, camarada!")
    def sayPlay(self):
        print("¡Vamos a jugar! Yo cubriré tu espalda (҂◡̀_◡́)ᕤ")
class WizardStyle(GameStyle):
    def sayHi(self):
        print("Que los arcanos guíen tu camino.")
    def sayPlay(self):
        print("¡Vamos a jugar! Desde lejos lanzaré hechizos para ayudarte (◑_◑)")
class HealerStyle(GameStyle):
    def sayHi(self):
        print("Que la paz y curación te acompañen.")
    def sayPlay(self):
        print("¡Vamos a jugar! Estoy para curarte y no dejarte desfallecer (ɔ◔‿◔)ɔ ♥")
