from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
	fichero = filedialog.askopenfilename(
		title="Abrir",
		initialdir="C:/Users/jaime.abad/Desktop",
		filetypes=( ("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los tipos de ficheros", "*.*") )
	) # Cuando le das a abrir accede a ese archivo por consola
	print(fichero)

Button(root, text="Abri", command=abreFichero).pack()

root.mainloop()

