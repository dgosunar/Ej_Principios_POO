from gameStyles import GameStyle, FighterStyle, WizardStyle, HealerStyle


class Player:
    def __init__(self, id, name, style: GameStyle):
        self.__id = id  # Private attribute
        self.name = name  # Public attribute
        self.style = style

    def getId(self):
        return self.__id

    def sayHi(self):
        """
        Player print his greeting according with his game style
        """
        self.style.sayHi()  # Abstract method

    def sayPlay(self):
        """
        Player print his invitation to play according with his game style
        """
        self.style.sayPlay()  # Abstract method


## Examples ##

pepo = Player(1, "Pepo", FighterStyle())
pepo.sayHi()
pepo.sayPlay()
print()

pepa = Player(2, "Pepa", WizardStyle())
pepa.sayHi()
pepa.sayPlay()
print()

nana = Player(3, "Nana", HealerStyle())
nana.sayHi()
nana.sayPlay()
print()
