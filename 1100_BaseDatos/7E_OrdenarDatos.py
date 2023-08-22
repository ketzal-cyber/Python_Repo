import sqlite3

# Nos devuelve una conexion
conexion = sqlite3.connect("databaseTest1.db")

#Linea para ejecutar sentencias SQL
cursor = conexion.cursor()

#ejecutar la consulta
cursor.execute("SELECT * FROM WEBS ORDER BY nombre_sitio")
sitios_ordenados = cursor.fetchall()

#Recorre la lista de cursor con las filas
for sitio in sitios_ordenados:
    print(sitio)

#cierro la conexion del archivo de base de datos
conexion.close()