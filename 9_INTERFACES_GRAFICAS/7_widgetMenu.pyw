from tkinter import *
from tkinter import messagebox

root = Tk()

def infoAdicional():
	messagebox.showinfo("Ventana Emergente", "Paquete messagebox de la librería tkinter")

def avisoLicencia():
	messagebox.showwarning(" producto GNU ", "Cambia el icono de la ventana emergente")

'''
def salirApp():
	valor = messagebox.askquestion( " Salir ", "¿Deseas salir de la aplicación?")
	if valor == "yes":
		root.destroy()
'''

def salirApp():
	valor = messagebox.askokcancel( " Salir ", "¿Deseas salir de la aplicación?")
	if valor == True:
		root.destroy()
# Se diferencia de la anterior en los botones

def cerrarDocumento():
	valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
	if valor == False:
		root.destroy()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

file_Tab = Menu(barraMenu, tearoff=0)
edit_Tab = Menu(barraMenu, tearoff=0)
tool_Tab = Menu(barraMenu, tearoff=0)
help_Tab = Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label=" Archivo ", menu=file_Tab)
barraMenu.add_cascade(label=" Editar ", menu=edit_Tab)
barraMenu.add_cascade(label=" Herramients ", menu=tool_Tab)
barraMenu.add_cascade(label=" Ayuda ", menu=help_Tab)

file_Tab.add_command(label= " Nuevo ")
file_Tab.add_separator()
file_Tab.add_command(label= " Guardar ")
file_Tab.add_command(label= " Guardar como... ")
file_Tab.add_separator()
file_Tab.add_command(label= " Cerrar ", command=cerrarDocumento)
file_Tab.add_command(label= " Salir ", command=salirApp)

edit_Tab.add_command(label= " Copiar ")
edit_Tab.add_command(label= " Cortar ")
edit_Tab.add_command(label= " Pegar ")

help_Tab.add_command(label= " Acerca de... ", command=infoAdicional)
help_Tab.add_command(label= " Licencia ", command=avisoLicencia)

root.mainloop()