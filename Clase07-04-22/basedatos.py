import pyodbc

servidor = "DESKTOP-C1JRKIM"
base = "adevntureworks2019"
usuario = "prueba2"
clave = ""

cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+servidor+'; DATABASE='+base+';UID='+usuario+'; PWD='+clave+'')
print("ya conectados")
cur = cnx.cursor()

cur.execute("select * from production.product")
consulta = cur.fetchall()
print(consulta[0][1])

cur.close()
cnx.close()