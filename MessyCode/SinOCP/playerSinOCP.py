class Player: 

    def __init__(self, id, name):
    self.__id = id
    self._points = 0.0
    self.rank = 'Bronce'
    self.name = name


    def increasePoints(self, addition):
    self._points = self._points + addition
    self.__defineRank()


    def __defineRank(self):
    if self._points <= 25:
    self.rank = 'Bronce'
    elif 25 < self._points <= 50:
    self.rank = 'Plata'
    elif 50 < self._points <= 75:
    self.rank = 'Oro'
    elif 75 < self._points <= 100:
    self.rank = 'Diamante'
    elif self._points > 100:
    self.rank = 'Maestro'

# Nuevo tipo de jugador: Arquero
class Archer(Player):  # Esta es la modificación que no sigue el OCP
    def __init__(self, id, name, arrowType):
    super().__init__(id, name)
    self.arrowType = arrowType
    self.difficulty = 2

    def sayHi(self):
    print('¡Hola! Soy el jugador ' + self.name + ' y jugaré como Arquero')

    def sayPlay(self):
    print('¡Vamos a jugar! Lanzaré flechas desde la distancia (⌐■_■)')


player1 = Player(1, 'Juan')
player1.increasePoints(30)
print(player1.rank) 

archer = Archer(2, 'Archer1', 'Venom')
archer.increasePoints(40)
print(archer.rank) 





