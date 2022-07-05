x = 5 #declaracion del entero

try:
    print("resultado" + x) #mensaje en caso de ser correcto
except TypeError as x:
    print("error", x.__str__()) #mensaje en caso de no ser entero
except:
    print("no se cual fue") #sino se cumplen