import sqlite3

# 1
miConexion = sqlite3.connect("DataBase_Name")

# 2
miCursor = miConexion.cursor()

# 3
# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
# Una vez creada la tabla no volver a ejecutar la sentencia

# 4
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
# Cambios en estructura o contenido requiren verificación
miConexion.commit()


miConexion.close()
# Si ejecutamos el programa se crea la el archivo con la bbdd en este mismo directorio
# Google --> descargar visor SQLite
