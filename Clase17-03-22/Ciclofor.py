strx = "abcdefgh" #declaracion de una cadena
zz = ['x','y','z'] #declaracion de una lista
for x in strx:
    print(x)
for x in range(3, 6): #for aplicando funcion rango entre valor inicial y final
    print(x, end="")
for x in zz: #for para recorrer el contenido del array
    print(x, " ", end="")
    print(type(x)) #para conocer el tipo de dato del array