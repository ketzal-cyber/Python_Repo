import sqlite3

# Nos devuelve una conexion
conexion = sqlite3.connect("databaseTest1.db")

#Linea para ejecutar sentencias SQL
cursor = conexion.cursor()

# Lista de datos para ser insertados
lista_sitos = [
    (2,'Cursos Java','https://www.youtube.com/watch?v=qXhc4wbDaqU','Video 168 sobre programacion java Theads'),
    (3,'UML','https://unadzsurlab.com/UML/U2/relaciones.html','Lenguaje UML'),
    (4,'Tutorial REDIS','https://www.ionos.mx/digitalguide/hosting/cuestiones-tecnicas/redis-tutorial-paso-a-paso/','DB Redis en memoria')
]

# funcion executemany para insertar valorios datos a la vez
cursor.executemany("INSERT INTO WEBS VALUES (?,?,?,?)", lista_sitos)               

conexion.commit()
conexion.close()
