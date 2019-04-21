from tkinter import *

root = Tk()


# ----------------------- RADIO ----------------------- #
varOpcion = IntVar()

def imprimir():
	print( varOpcion.get() )
	if varOpcion.get() == 1:
		etiqueta.config(text="Has elegido Masculino")
	elif varOpcion.get() == 2:
		etiqueta.config(text="Has elegido Femenino")
	else:
		etiqueta.config(text="Has elegido Transexual")


Label(root, text="Genero: ").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Transexual", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()


# ----------------------- CHECK ----------------------- #

playa 			= IntVar()
montaña 		= IntVar()
turismoRural 	= IntVar()

def opcionesViaje():
	opcionEscogida = ""

	if playa.get() == 1:
		opcionEscogida += " playa"
	if montaña.get() == 1:
		opcionEscogida += " montaña"
	if turismoRural.get() == 1:
		opcionEscogida += " turismo rural"

	textoFinal.config(text=opcionEscogida)


root.title("Ejemplo")

foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()
Label(frame, text="Elige destinos", width=50).pack()


Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()