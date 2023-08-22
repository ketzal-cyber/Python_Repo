import sqlite3

# Nos devuelve una conexion
conexion = sqlite3.connect("databaseTest1.db")

#Linea para ejecutar sentencias SQL
cursor = conexion.cursor()

#ejecutar la consulta
cursor.execute("UPDATE WEBS SET nombre_sitio = 'Lenguaje Unificado' WHERE nombre_sitio = 'UML'")

#Conirmar la eecucion de la sentencia
conexion.commit()
#cierro la conexion del archivo de base de datos
conexion.close()