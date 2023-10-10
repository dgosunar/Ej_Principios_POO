from gameStyles import GameStyle, FighterStyle, WizardStyle
class Player:
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
pepo = Player(1, 'Pepo', FighterStyle())
pepo.sayHi()
pepo.sayPlay()
pepa = Player(2, 'Pepa', WizardStyle())
pepa.sayHi()
pepa.sayPlay()
nana = Player(3, 'Nana', HealerStyle())
nana.sayHi()
nana.sayPlay()
