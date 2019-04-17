from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()
# ---------------------- VARS ---------------------- #
miNombre = StringVar()

# ---------------------- ENTRIES ---------------------- # 
cuadroTextoNombre = Entry(miFrame, textvariable=miNombre)
cuadroTextoNombre.grid(row=0, column=1, padx=10)
cuadroTextoNombre.config(fg="red", justify="center") # aplica al texto contenido

cuadroTextoPass = Entry(miFrame)
cuadroTextoPass.grid(row=1, column=1, padx=10)
cuadroTextoPass.config(show="*")

cuadroTextoApellido = Entry(miFrame)
cuadroTextoApellido.grid(row=2, column=1, padx=10)

cuadroTextoDireccion = Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1, padx=10)

cuadroTextoComentario = Text(miFrame, width=16, height=5)
cuadroTextoComentario.grid(row=4, column=1, padx=10, pady=10)


# ---------------------- scrollbar ---------------------- # 
scrollVert = Scrollbar(miFrame, command=cuadroTextoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
# Lenguaje síncrono, scrollVert must be previously defined
cuadroTextoComentario.config(yscrollcommand=scrollVert.set)

# ---------------------- LABELS ---------------------- #
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Introduzca la contraseña: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección de casa: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# ---------------------- button ---------------------- #
def codigoBoton():
	miNombre.set("Jaime")
	
	

botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()

# cualquier elemento tiene un contenedor padre. El padding es la distancia desde el elemento hasta el límite del contenedor