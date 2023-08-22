import sqlite3

# Nos devuelve una conexion
conexion = sqlite3.connect("databaseTest1.db")

#Linea para ejecutar sentencias SQL
cursor = conexion.cursor()

cursor.execute("INSERT INTO WEBS VALUES"
               +"(1,'Cursos Hacking','https://www.reydes.com/d/','Videos sobre temas de Hacking Etico')")

conexion.commit()
conexion.close()
