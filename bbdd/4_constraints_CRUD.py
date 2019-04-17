import sqlite3

miConexion = sqlite3.connect("DataBase_Name")
miCursor = miConexion.cursor()


miCursor.execute(
	'''
	CREATE TABLE PRODUCTOS (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
		PRECIO INTEGER,
		SECCION VARCHAR(20)
	)
	'''
)

productos = [
	("Camiseta", 10, "Deportes"),
	("Jarrón", 15, "Cerámica"),
	("Playmobil", 7, "Juguetería"),
	("Sillón", 200, "Hogar")
]

miCursor.executemany(
	"INSERT INTO PRODUCTOS VALUES (NULL, ?,?,?)",
	productos
)
miConexion.commit()
# EXECUTE THE PROGRAM
'''

miCursor.execute("SELECT * FROM PRODUCTOS")
results = miCursor.fetchall()
print(results)