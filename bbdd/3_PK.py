import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

miCursor.execute(
	'''
	CREATE TABLE PRODUCTOS(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		NOMBRE_ARTICULO VARCHAR(50),
		PRECIO INTEGER,
		SECCION VARCHAR(20)
	)
	'''
)

'''
miCursor.execute(
	''3comillas
	CREATE TABLE GESTIONPRODUCTOS(
		CODIGO_ATICULO VARCHAR(4) PRIMARY KEY,
		NOMBRE_ARTICULO VARCHAR(50),
		PRECIO INTEGER,
		SECCION VARCHAR(20)
	)
	''3comillas
)

productosSinPK = [
	("AR01", "pelota", 20, "jugetería"),
	("AR02", "pantalón", 15, "confección"),
	("AR03", "destorinillador", 25, "ferretería"),
	("AR04", "silla", 45, "hogar")
]

miCursor.executemany(
	"INSERT INTO PRODUCTOS VALUES (?,?,?,?)",
	productosSinPK
)
'''

productos = [
	("pelota", 20, "jugetería"),
	("pantalón", 15, "confección"),
	("destorinillador", 25, "ferretería"),
	("silla", 45, "hogar")
]

miCursor.executemany(
	"INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",
	productos
)

miConexion.commit()

miConexion.close()