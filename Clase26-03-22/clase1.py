class Carro():

    longitud = 100 #static por ser declarada en la cabecera de la clase
    __privada = 200 #variables privadas
    _protected = 10 #visible hacia las hijas

    @classmethod
    def construirdesdeunstring(cls, cadena):
        #cls.longitud += x
        x, y = cadena.split(' ')
        return cls(x, y)

    @staticmethod #decorador metodo estatico donde no se pone el self
    def infoautos():
        print("los carros son vehiculos que tienen 4 ruedas")


    def __metodoprivado(self):
        print("este metodo es solo de uso interno")

    def frenar(self, x, y): #self hace las veces de this
        print(Carro.__privada)
        return "estoy frenando: " + str(x + y)

#definiendo metodos magicos o dunder
    def __init__(self, x ,y):
        self.x = x #asi creamos variable interna a la clase
        pass #para no escribir codigo

    def __repr__(self):
        return "este es un carro de longitud: " + str(self.longitud)

    def __str__(self):
        return "la convertimos en string como me parezca conveniente"

class Van(Carro): #herencia en el parentesis
    def abrirpuertacorrediza(self):
        print("abriendo puerta corrediza")

    def frenar(self, x):
        print("estamos sobreescribiendo el metodo frenar")

class Bote():
    def navegan(self):
        print("estoy navegando")

    def __init__(self, z):
        pass

class CarroBote(Bote, Carro): #esta herencia multiple no tiene limites
    pass

#instanciacion
"""x = Padre()
x.funcionpadre()
y = Dos()"""