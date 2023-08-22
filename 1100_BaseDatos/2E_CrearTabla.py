#importando SQLite
import sqlite3

conexion = sqlite3.connect("databaseTest1.db")

#creacion de un cursor
cursor = conexion.cursor()

cursor.execute("CREATE TABLE WEBS "
               + "(id INTEGER,nombre_sitio TEXT, url TEXT, descripcion TEXT)")

conexion.commit()
conexion.close()