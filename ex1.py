'''A classe Avião poderia ter uma associação com a classe Coordenada Geográfica, pois
esta ultima consegue representar a latitude, longitude e permite ainda indicar a
distância em km entre duas Coordenadas Geográficas
A associação entre essas classes seria do tipo Agregação ou Composição?
Quais atributos e métodos deverão permanecer na classe Avião?'''

class Coordenadas:
    def __init__(self) -> None:
        self.__latitude = 0.0
        self.__altitude = 0.0
        self.__distancia = 0.0

    def CalcDistancia(self, distancia, x, y):
        self.distancia = distancia
        x = 0.0
        y = 0.0
        distancia = None

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        self.__latitude = latitude

    @property
    def altitude(self):
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude):
        self.__altitude = altitude
    
    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, distancia):
        self.__distancia = distancia

class Aviao(Coordenadas):
    def __init__(self):
        super().__init__()
    
    def CalcDistancia(self, distancia x, y):
        self.distancia = distancia
        x = self.latitude
        y = 
        distancia = x - y