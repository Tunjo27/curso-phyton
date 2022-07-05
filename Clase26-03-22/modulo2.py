import math
import modulo1
from math import * #o podria especificar lo que queremos especificar en lugar del *
from clase1 import *

x = Carro(8, 9) #instaciacion
y = Carro(20, 10)

x = Carro(4, 5)
#Carro.incrementarlalongitud(20)

#print(help(Carro)) #describe la clase

x = Carro.construirdesdeunstring("30 40")
print(x.x)

print(x.longitud)
print(Carro.infoautos()) #no necesita de instancia para correr
x.frenar(5, 6)
x.__privada = 100 #intento de llamado de la variable privada de la clase "clase1"
print(x)
#print(x.x)
#print(y.x)
#print(x.frenar(5, 6))

#reasignacion de valores
"""Carro.longitud = 150

y.longitud = 160

print(x.longitud)
print(y.longitud)"""

x.j = 20 #declarar propiedad inexistente
print(x.j) #imprimir

#x.frenar() #invocamos el metodo

def funcion3():
    print("funcion 3")

#print(math.sqrt(10))
#modulo1.funcion1()
#print(sqrt(10))

#print(modulo1.x)

"""CONSTANTE = 100

y = Carro(5, 4)

x = Van(10, 20)#instancia
x.frenar(40)"""

#x.abrirpuertacorrediza()
#print(help(Van))

"""x = Van(4, 5)
print(x.__dict__)"""

x = CarroBote(10)
