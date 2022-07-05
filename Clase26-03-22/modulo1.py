x = 100

def funcion1():
    print("funcion 1")

def funcion2():
    print("funcion 2")

#funcion2()
#print(__name__) #variable magica: comprueba que modulo se ejecuta

#corra solo si esta ejecuta de forma directa
if __name__ == '__main__':
    print("corra solo cuando es invocado de forma directa")
else:
    print("corra solo si el modulo es importado")