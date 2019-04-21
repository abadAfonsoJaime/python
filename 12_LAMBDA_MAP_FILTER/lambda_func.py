'''
def area_triangulo(base, altura):
	return (base*altura)/2
'''
area_triangulo = lambda base,altura:(base*altura)/2
# las funciones lambda son de cálculo, no de lógica
# si hay bucles o condicionales no se puede convertir en funcion lambda

#al_cubo = lambda numero:pow(numero,3)
al_cubo = lambda numero:numero**3

destacar_valor = lambda comision: "¡{}! €".format(comision)
comision_Ana = 15585
print( destacar_valor(comision_Ana) )