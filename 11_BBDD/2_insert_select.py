import sqlite3

miConexion = sqlite3.connect("DataBase_Name")
miCursor = miConexion.cursor()

'''
variosProductos = [
	("Camiseta", 10, "Deportes"),
	("Jarrón", 95, "Cerámica"),
	("Playmobil", 7, "Juguetería"),
	("Sillón", 200, "Hogar")
]

miCursor.executemany(
	"INSERT INTO PRODUCTOS VALUES (?,?,?)",
	variosProductos
)
miConexion.commit()
# EXECUTE THE PROGRAM
'''


miCursor.execute("SELECT * FROM PRODUCTOS")
results = miCursor.fetchall()
print(results)
for prod in results:
	print("Nombre Artículo: ", prod[0], "Precio: ", prod[1], "Sección: ", prod[2])
