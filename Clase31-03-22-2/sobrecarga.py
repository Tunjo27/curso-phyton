from multipledispatch import dispatch

@dispatch(int, str)
def funcion1(x, y):
    print(type(x))
    print(type(y))
    print("entero con string")

@dispatch(str, str)
def funcion1(a, b):
    print("string con string")

funcion1(10, "b")