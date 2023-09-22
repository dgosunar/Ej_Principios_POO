from Entities.player import Player

class Fighter(Player):    #Inheritance

    def __init__(self, id, name, fightForce):
        super().__init__(id, name)    #Add Player class attributes
        
        #Only Figther attributes
        self.fightForce = fightForce
        self.difficulty = 1

    #Polymorphism
    def sayHi(self):
        '''
            Player print his greeting telling his game style as Fighter
        '''
        print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Luchador')

    def sayPlay(self):
        '''
            Player print his invitation to play as a fighter
        '''
        print('¡Vamos a jugar! Yo cubriré tu espalda (҂◡̀_◡́)ᕤ')


class Wizard(Player):    #Inheritance

    def __init__(self, id, name, magicType):
        super().__init__(id, name)    #Add Player class attributes
        
        #Only Wizard attributes
        self.magicType = magicType
        self.difficulty = 3

    #Polymorphism
    def sayHi(self):
        '''
            Player print his greeting telling his game style as Wizard
        '''
        print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Mago')

    def sayPlay(self):
        '''
            Player print his invitation to play as a wizard
        '''
        print('¡Vamos a jugar! Desde lejos lanzaré hechizos para ayudarte (◑_◑)')


class Healer(Player):    #Inheritance

    def __init__(self, id, name, healTool):
        super().__init__(id, name)    #Add Player class attributes
        
        #Only Wizard attributes
        self.healTool = healTool
        self.difficulty = 2

    #Polymorphism
    def sayHi(self):
        '''
            Player print his greeting telling his game style as Healer
        '''
        print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Healer')

    def sayPlay(self):
        '''
            Player print his invitation to play as a healer
        '''
        print('¡Vamos a jugar! Estoy para curarte y no dejarte desfallecer (ɔ◔‿◔)ɔ ♥')