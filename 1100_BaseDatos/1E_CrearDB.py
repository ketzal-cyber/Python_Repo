#crear una base de datos desde PYthon Y SQLite
#importanto sqlite 
import sqlite3

# Nos devuelve una conexion
conexion = sqlite3.connect("databaseTest1.db")

conexion.close()