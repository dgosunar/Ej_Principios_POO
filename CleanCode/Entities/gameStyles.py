from Entities.player import Player

class Fighter(Player):    #Inheritance

    def __init__(self, id, name, fightForce):
        super().__init__(id, name)    #Add Player class attributes
        
        #Only Figther attributes
        self.fightForce = fightForce
        self.difficulty = 1

    #Polymorphism
    def sayHi(self):
        print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Luchador')

    def sayPlay(self):
        print('¡Vamos a jugar! Yo cubriré tu espalda (҂◡̀_◡́)ᕤ')


class Wizard(Player):    #Inheritance

    def __init__(self, id, name, magicType):
        super().__init__(id, name)    #Add Player class attributes
        
        #Only Wizard attributes
        self.magicType = magicType
        self.difficulty = 3

    #Polymorphism
    def sayHi(self):
        print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Mago')

    def sayPlay(self):
        print('¡Vamos a jugar! Desde lejos lanzaré hechizos para ayudarte (◑_◑)')


class Healer(Player):    #Inheritance

    def __init__(self, id, name, healTool):
        super().__init__(id, name)    #Add Player class attributes
        
        #Only Wizard attributes
        self.healTool = healTool
        self.difficulty = 2

    #Polymorphism
    def sayHi(self):
        print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Healer')

    def sayPlay(self):
        print('¡Vamos a jugar! Estoy para curarte y no dejarte desfallecer (ɔ◔‿◔)ɔ ♥')