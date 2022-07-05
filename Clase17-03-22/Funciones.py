#función sin parámetros o retorno de valores
def diHola():
  print("Hello!")
diHola()  #llamada a la función, 'Hello!' y se muestra en la consola

#función con un parámetro
def holaConNombre(name):
  print("Hello " + name + "!")
holaConNombre("Aida")  #llamada a la función, 'Hello Aida!' se muestra en la consola

#funcion con varios parametros
def funcion1(a, b, c=5):
    #global z
    def funcionz(): #funcion interior
        z = 20

    z = 10
    print(z)
    return 10 + int(a) + b + c, 88

print(funcion1(2, 2, 4)) #sumatoria a la variable entera y el 88 aparte
funcion1(5, 5, 4) #imprime el 10 interior pero no toma los valores de los parametros

#sin funcionar
"""x, y = funcion1("2", 2, 4)
print(y)

def funcion2(x, y):
    #print(x, y)
    return 100"""
