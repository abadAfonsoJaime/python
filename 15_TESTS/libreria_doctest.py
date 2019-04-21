def areaTriangulo(base, altura):
	''' 
	Calcula el área de un tríángulo
	a partir de su base y altura

	>>> areaTriangulo(3,6)
	9.0

	>>> areaTriangulo(4,5)
	10.0
	'''
	return (base*altura)/2


def comprueba_mail(mailUsuario):
	'''
	Evalúa el parámetro en busca de un único @
	que no esté al final

	>>> comprueba_mail("j.a@vass.es")
	True

	>>> comprueba_mail("jaime@vass@a.es")
	False

	>>> comprueba_mail("jaimevass@s")
	True
	
	>>> comprueba_mail("jaime@vass@a.es")
	False

	>>> comprueba_mail("jaime@")
	False
	'''
	arroba = mailUsuario.count('@')
	if (arroba != 1 or mailUsuario.rfind('@') == len(mailUsuario)-1 ):
		return False
	else:
		return True


import doctest
doctest.testmod()