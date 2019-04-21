import math

def raizCuadrada(listaNum):
	'''
	Devuelve una lista con la ráiz cuadrada	de los
	 elementos de la lista pasada por parámetro

	>>> raizCuadrada( [9, 16, 25, 36] )
	[3.0, 4.0, 5.0, 6.0]

	>>> lista = []
	>>> for i in [9,25, 49]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[3.0, 5.0, 7.0]

	>>> lista = []
	>>> for i in [4, -9, 16]
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error
	'''
	return [math.sqrt(n) for n in listaNum]