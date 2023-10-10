from abc import abstractmethod, ABC

#Abstract Interface
class GameStyle(ABC):
    @abstractmethod
    def sayHi(self):
        pass

    @abstractmethod
    def sayPlay(self):
        pass

## Game styles that depends on the interface ##

class FighterStyle(GameStyle):
    def sayHi(self):
        """
        Player print his greeting telling his game style as Fighter
        """
        print("¡Listo para la batalla, camarada!")

    def sayPlay(self):
        """
        Player print his invitation to play as a fighter
        """
        print("¡Vamos a jugar! Yo cubriré tu espalda (҂◡̀_◡́)ᕤ")


class WizardStyle(GameStyle):
    def sayHi(self):
        """
        Player print his greeting telling his game style as Wizard
        """
        print("Que los arcanos guíen tu camino.")

    def sayPlay(self):
        """
        Player print his invitation to play as a wizard
        """
        print("¡Vamos a jugar! Desde lejos lanzaré hechizos para ayudarte (◑_◑)")


class HealerStyle(GameStyle):
    def sayHi(self):
        """
        Player print his greeting telling his game style as Healer
        """
        print("Que la paz y curación te acompañen.")

    def sayPlay(self):
        """
        Player print his invitation to play as a healer
        """
        print("¡Vamos a jugar! Estoy para curarte y no dejarte desfallecer (ɔ◔‿◔)ɔ ♥")
