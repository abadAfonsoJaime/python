'''
A diferencia de la función filter que aplica una condición,
 Map aplica una función a cada elemento de una lista iterable
 (listas, tuplas etc) devolviendo una lista con los resultados
'''
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
	Empleado("Jaime", "Director", 7000),
	Empleado("Yanny", "Secretaria", 1100),
	Empleado("Clara", "Abogada", 3000),
	Empleado("Sonsoles", "Administrativa", 1500),
]

def calculo_comision(empleado):
	if empleado.salario < 2000:
		empleado.salario = empleado.salario*1.03
	return empleado

listaEmpleadosComision = map(
	calculo_comision,
	listaEmpleados
)
for employee in listaEmpleadosComision:
	print(employee)