from tkinter import *
from tkinter import messagebox
import sqlite3

# -------------------------------- FUNCIONES -------------------------------- #
def conexionBBDD():
	conn = sqlite3.connect("Usuarios")
	pointer = conn.cursor()
	try:
		pointer.execute('''
			CREATE TABLE DATOSUSUARIOS (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				NOMBRE_USUARIO VARCHAR(20),
				PASSWORD VARCHAR(20),
				APELLIDO VARCHAR(20),
				DIRECCION VARCHAR(50),
				COMENTARIOS VARCHAR(100)
			)
		''')
		messagebox.showinfo("BBDD", "BBDD creada con éxito")
	except:
		messagebox.showwarning("¡Atención cabrón!", "La BBDD ya existe")

def salirAplicacion():
	valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	if valor == "yes":
		root.destroy()

def resetFields():
	promptID.set("")
	promptNombre.set("")
	promptApellido.set("")
	promptPassword.set("")
	promptDireccion.set("")
	textoComentario.delete(1.0, END)


def createData():
	conn = sqlite3.connect("Usuarios")
	pointer = conn.cursor()
	"""
	pointer.execute('''
		INSERT INTO DATOSUSUARIOS VALUES(
			NULL,
			"''' + promptNombre.get() 	+ '''",
			"''' + promptApellido.get() + '''",
			"''' + promptPassword.get() + '''",
			"''' + promptDireccion.get() + '''",
			"''' + textoComentario.get("1.0", END) + '''"
		)
	''')
	"""
	data = promptNombre.get(), promptApellido.get(), promptPassword.get(), promptDireccion.get(), textoComentario.get("1.0", END)
	pointer.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", data)

	conn.commit()
	messagebox.showinfo("BBDD", "Registro insertado correctamente")


def readData():
	conn = sqlite3.connect("Usuarios")
	pointer = conn.cursor()
	pointer.execute( 'SELECT * FROM DATOSUSUARIOS WHERE ID='+promptID.get() )
	row = pointer.fetchall()
	for user in row:
		promptID.set(user[0])
		promptNombre.set(user[1])
		promptApellido.set(user[2])
		promptPassword.set(user[3])
		promptDireccion.set(user[4])
		textoComentario.insert(1.0, user[5])
	conn.commit()

def updateData():
	conn = sqlite3.connect("Usuarios")
	pointer = conn.cursor()
	data = promptNombre.get(), promptApellido.get(), promptPassword.get(), promptDireccion.get(), textoComentario.get("1.0", END)
	pointer.execute('''UPDATE DATOSUSUARIOS SET 
		NOMBRE_USUARIO=?,
		APELLIDO=?,
		PASSWORD=?,
		DIRECCION=?,
		COMENTARIOS=?
			 WHERE ID=''' + promptID.get(), data)
	"""
	pointer.execute('''
		UPDATE DATOSUSUARIOS SET
			NOMBRE_USUARIO ="''' + promptNombre.get() 	+ '''",
			APELLIDO="''' + promptApellido.get() + '''",
			PASSWORD="''' + promptPassword.get() + '''",
			DIRECCION="''' + promptDireccion.get() + '''",
			COMENTARIOS="''' + textoComentario.get(1.0, END) + '''
				"  WHERE ID=''' + promptID.get())
	"""
	conn.commit()
	messagebox.showinfo("BBDD", "Registro actualizado correctamente")

def deleteData():
	conn = sqlite3.connect("Usuarios")
	pointer = conn.cursor()
	pointer.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + promptID.get() )
	conn.commit()
	messagebox.showinfo("BBDD", "Registro borrado")
# -------------------------------- TKINTER -------------------------------- #
root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=350, height=350)
# -------------------------------- VARIABLES -------------------------------- #
promptID 		= StringVar()
promptNombre 	= StringVar()
promptApellido 	= StringVar()
promptPassword 	= StringVar()
promptDireccion = StringVar()


# -------------------------------- MENU -------------------------------- #
db_menu = Menu(barraMenu, tearoff=0)
db_menu.add_command(label="Conectar", command=conexionBBDD)
db_menu.add_command(label="Salir", command=salirAplicacion)

reset_menu = Menu(barraMenu, tearoff=0)
reset_menu.add_command(label="Limpiar Campos", command=resetFields)

crud_menu = Menu(barraMenu, tearoff=0)
crud_menu.add_command(label="Crear", command=createData)
crud_menu.add_command(label="Leer", command=readData)
crud_menu.add_command(label="Actualizar", command=updateData)
crud_menu.add_command(label="Borrar", command=deleteData)

barraMenu.add_cascade(label="BBDD", menu=db_menu)
barraMenu.add_cascade(label="Reset", menu=reset_menu)
barraMenu.add_cascade(label="CRUD", menu=crud_menu)


# -------------------------------- FIELDS -------------------------------- #
fieldFrame = Frame(root)
fieldFrame.pack()

cuadroID = Entry(fieldFrame, textvariable=promptID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(fieldFrame, textvariable=promptNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass = Entry(fieldFrame, textvariable=promptPassword)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido = Entry(fieldFrame, textvariable=promptApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(fieldFrame, textvariable=promptDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(fieldFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(fieldFrame, command=textoComentario.yview) # eje ordenadas
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)




idLabel = Label(fieldFrame, text= "Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(fieldFrame, text= "Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passwordLabel = Label(fieldFrame, text= "Password: ")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(fieldFrame, text= "Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(fieldFrame, text= "Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(fieldFrame, text= "Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)





# -------------------------------- BOTONES -------------------------------- #
buttonFrame = Frame(root)
buttonFrame.pack()

buttonCreate = Button(buttonFrame, text="Create", command=createData)
buttonCreate.grid(row=0, column=0, sticky="e", padx=10, pady=10)

buttonRead = Button(buttonFrame, text="Read", command=readData)
buttonRead.grid(row=0, column=1, sticky="e", padx=10, pady=10)

buttonUpdate = Button(buttonFrame, text="Update", command=updateData)
buttonUpdate.grid(row=0, column=2, sticky="e", padx=10, pady=10)

buttonDelete = Button(buttonFrame, text="Delete", command=deleteData)
buttonDelete.grid(row=0, column=3, sticky="e", padx=10, pady=10)


root.mainloop()