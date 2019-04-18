import re

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "María López"
nombre4 = "Lara García"

if re.match("Sandra", nombre1):
	print("Nombre encontrado!")
else:
	print("El nombre no está")
print("La función match() busca al comienzo")
if re.match("López", nombre1):
	print("Apellido encontrado!")
else:
	print("El apellido sí está pero al final, match() no lo encuentra")

print("La función search() busca en todo")
if re.search("López", nombre1):
	print("Apellido encontrado!")
else:
	print("El apellido no está")


if re.match("anTONio", nombre2, re.IGNORECASE):
	print("Nombre encontrado!")
else:
	print("El nombre no está")

print("---- comodín . ----")
if re.match(".ara", nombre4, re.IGNORECASE):
	print("SI!")
else:
	print("No")


cadena1 = "546546546"
cadena2 = "a54654654"

print("--- \d ---")
if re.match("\d", cadena1):
	print("Número encontrado")
else:
	print("Not found")
print("mismo ejemplo")
if re.match("\d", cadena2):
	print("Número encontrado")
else:
	print("Not found")

