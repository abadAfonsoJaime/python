'''
def numero_par(num):
	if num % 2 == 0:
		return True
'''
numeros = [17, 24, 7, 39, 8, 92]

#filtrado = filter(numero_par, numeros)
#print( list(filtrado) )

print(
	list(
		filter(
			lambda pares: pares % 2 == 0,
			numeros
		)
	)
)

########################################
class Empleado:

	def __init__(self, nombre, cargo, salario):
		self.nombre 	= nombre
		self.cargo 		= cargo
		self.salario 	= salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} €".format(
			self.nombre,
			self.cargo,
			self.salario
		)

listaEmpleados = [
	Empleado("Jaime", "Director", 75000),
	Empleado("Yanny", "Secretaria", 20000),
	Empleado("Clara", "Abogada", 40000),
	Empleado("Sonsoles", "Administrativa", 25000),
]

salarios_bajos = filter(
	lambda employee: employee.salario > 35000,
	listaEmpleados
)

for emplado_salario in salarios_bajos:
	print(emplado_salario)