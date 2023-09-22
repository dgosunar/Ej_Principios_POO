class Player:

    def __init__(self, id, name):
        self.__id = id    #Private attribute
        self._points = 0.0    #Protected attribute
        self.rank = 'bronce'    #Public attribute
        self.name = name    #Public attribute

    def sayHi(self):
        print('¡Hola! Soy el jugador ' + self.name + ' y soy rango ' + self.rank)

    def sayPlay(self):
        print('¡Vamos a jugar! ٩(˘◡˘)۶')

    def getId(self):
        return self.__id
    
    def getPoints(self):
        return self._points

    def increasePoints(self, addition):
        self._points = self._points + addition
        self.__defineRank()

    def __defineRank(self): #Private method
        if self._points <= 25:
            self.rank = 'Bronce'
        elif self._points > 25 and self._points <= 50:
            self.rank = 'Plata'
        elif self._points > 50 and self._points <= 75:
            self.rank = 'Oro'
        elif self._points > 75 and self._points <= 100:
            self.rank = 'Diamante'
        elif self._points > 100:
            self.rank = 'Maestro'