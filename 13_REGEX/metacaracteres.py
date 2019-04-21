import re

lista_nombres = [
	'Ana Gómez',
	'María Martín',
	'Sandra López',
	'Santiago Martín'
]

for el in lista_nombres:
	if re.findall('^San', el):
		print(el)

for el in lista_nombres:
	if re.findall('Martín$', el):
		print(el)

listaDominios = [
	'http://pildorasinformaticas.es',
	'http://appian.com',
	'ftp://pildorasinformaticas.es',
	'ftp://santander.com',
	'https://informaticaenespaña.es'
]
print("-----------------------")
for el in listaDominios:
	if re.findall('.es$', el):
		print(el)
print("-----------------------")
for el in listaDominios:
	if re.findall('^ftp://', el):
		print(el)
print("-----------------------")
for el in listaDominios:
	if re.findall('[ñ]', el):
		print(el)

personType = [
	'hombres',
	'mujeres',
	'niños',
	'niñas',
	'cabrón',
	'cabrona'
]
print("-----------------------")
for el in personType:
	if re.findall('niñ[oa]s', el):
		print(el)

print("-----------------------")
for el in personType:
	if re.findall('cabr[oó]', el):
		print(el)

print("------- RANGOS ------")

for el in lista_nombres:
	if re.findall('[o-t]', el):
		print(el)
print("\n")		
for el in lista_nombres:
	if re.findall('[n-t]$', el):
		print(el)


listaPedidos = [
	"Mad1:",
	"Sev1",
	"Mad2",
	"Bcn1",
	"Val1.",
	"Val2:",
	"Mad3",
	"Mad4",
	"MadA.",
	"MadB",
	"MadC"
]
print("------------------")
for el in listaPedidos:
	if re.findall('Mad[0-3]', el):
		print(el)
print("Negación del rango")
for el in listaPedidos:
	if re.findall('Mad[^0-3]', el):
		print(el)

print("------------------")
for el in listaPedidos:
	if re.findall('Mad[0-3A-B]', el):
		print(el)
print("masssssssssss")
for el in listaPedidos:
	if re.findall('[.:]', el):
		print(el)