'''
Son 3 funciones (A, B y C) donde A recibe como parámetro B
para devolver C --> Un decorador devuelve una función

def funcion_decorador_A(funcion_parametro_B):
	def funcion_interna_C():
		# código de la función interna
	return funcion_interna_C()
'''
def funcion_decoradora(funcion_parametro):
	
	def funcion_interior():
		# Acciones adicionales que decoran
		print("Vamos a ejecutar una instrucción: ")
		funcion_parametro()
		# Acciones adicionales que decoran
		print("Hemos terminado la ejecución")

	# al no recibir parámetros se debn poner los paréntesis
	return funcion_interior()

@funcion_decoradora
def sayHello():
	print("Hello")

# Funciona exactamente igual sin los *args
def funcion_decoradora_2(funcion_parametro):

	def funcion_interior(*args):
		# Acciones adicionales que decoran
		print("Vamos a ejecutar una instrucción: ")
		funcion_parametro(*args)
		# Acciones adicionales que decoran
		print("Hemos terminado la ejecución")

	return funcion_interior

# Cuando pasamos argumentos como clave valor
def funcion_decoradora_3(funcion_parametro):

	def funcion_interior(*args, **kwargs):
		# Acciones adicionales que decoran
		print("Pasamos argumentos a la función: ")
		funcion_parametro(*args, **kwargs)
		# Acciones adicionales que decoran
		print("Los parámetros se pasaron como key:value")

	# Debe ir sin paréntesis
	return funcion_interior

print("----- kwargs -----")
@funcion_decoradora_3
def potencia(base, exponente):
	print( pow(base, exponente) )

potencia(base=5, exponente=2)