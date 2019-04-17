from tkinter import *

root=Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()
#------- Después de empaquetar el frame
miImagen = PhotoImage(file="panteraRosa.gif")
Label(miFrame, image=miImagen).place(x=100, y=200)

#Label(miFrame, text="Hola Matrix desde Python", fg="red", font=("Comic Sans MS", 18) ).place(x=100, y=200)
# miLabel.pack() No queremos que el frame se adapte a su contenido
# miLabel.place(x=100, y=200) # Ubica el texto en cualquier lugar mediante coordenadas en px

root.mainloop()
'''
WIDGETS --> LABEL
	Utilizados para mostrar textos o imágenes;
	No se puede interactuar con ellos

variableLabel = Label(contendor, opciones...)
	text: Texto que se muestra en el label
	anchor: Posición del texto si hay espacio suficiente para él (center por defecto)
	bg: Color de fondo
	bitmap: Mapa de bits que se mostrará como gráfico
	bd: Grosor del borde (2px por defecto)
	font: Tipo de fuente a mostrar
	fg: Color de la fuente
	width: Ancho de Label en caracteres (no en píxeles)
	heigth: Altura de Label en caracteres (no en píxeles)
	image: Muestra la imagen en el Label en lugar de texto
	justify: Justificación del textodel Label

La librería tkinter 
'''