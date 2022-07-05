import pyodbc

servidor = "localhost"
basedatos = "adventureworks2019"
usuario = "usuarionuevo"
clave = "9909cris"

#conx = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER="
#                     +servidor+";DATABASE="+basedatos+";UID="+usuario+";PWD="+clave)
print("ok")
conx = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER="
                      +servidor+";DATABASE="+basedatos+";Trusted_Connection=yes")
cursor = conx.cursor()

"""cursor.execute("select @@version")
fila = cursor.fetchone()
print(fila)"""

fila = cursor.fetchone()
while fila is not None:
    fila = cursor.fetchone()
    print(fila[4])

tabla = cursor.fetchall()
print(tabla[10000][4])
print(len(tabla))