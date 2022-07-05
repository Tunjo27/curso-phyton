x = 5 #declaracion de entero
print(x) #impresion del entero

x = "hola mundo" #declaracion de una cadena
x = x.upper() #se asigna funcion para ver la cadena como mayuscula y lower para minuscula
print(x) #impresion de la cadena

print(len(x)) #devolvemos la cantidad de caracteres de la cadena x
z = "prueba"
test = z.replace("p", "t") #funcion para reemplazar un caracter por otro
print(test) #impresion de la variable modificada con la funcion

print(x[0:3]) #impresion por caracter marcando la extension de inicio y final
print(x[::2]) #impresion con espacios entre caracter y caracter
# print(x[90]) #error

print(pow(3, 3)) #potencia primer numero normal y segundo a lo que se quiere potenciar

"""impresion de la variable con la funcion de redondeo de entero cercano
en diferentes casos"""
b = -5.4
print(round(b))
c = 5.6
print(round(c))
d = 15
print(round(d))

a = int(input("digite un valor")) #input
print(a) #impresion del input luego de ingresado

# comentario una sola linea
"""
comentario multilinea
.....
"""