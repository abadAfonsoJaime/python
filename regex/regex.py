import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es la polla"

patronBusqueda = "aprender"

if re.search(patronBusqueda, cadena) is not None:
	print("Lo encontré!")
else:
	print("No lo vi")


textoEncontrado = re.search(patronBusqueda, cadena)
print( textoEncontrado.start() )
print( textoEncontrado.end() )
print( textoEncontrado.span() )

segundaBusqueda = "Python"
print( re.findall(segundaBusqueda, cadena) )
