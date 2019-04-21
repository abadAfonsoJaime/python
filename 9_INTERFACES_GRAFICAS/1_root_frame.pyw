from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas") # HTML Document
raiz.iconbitmap("favicon.ico") # path del favicon --> conversor imagenes .ico
# raiz.resizable(1,0) # solo permite redimensionar a lo ancho
# raiz.geometry("650x350") # La raiz se adapta al tamaño de su contenedor interno (Frame)
raiz.config(bg="yellow")

raiz.config(bd=50)
raiz.config(relief="sunken")
raiz.config(cursor="hand2")
#---------------------------
miFrame = Frame()
miFrame.pack()
# miFrame.pack(side="right")
# miFrame.pack(side="bottom", anchor="w")
# miFrame.pack(fill="x")
# miFrame.pack(fill="y", expand=True)
#miFrame.pack(fill="both", expand=True)

miFrame.config(bg="purple")
miFrame.config(width="650", height="350")

miFrame.config(bd=35)
miFrame.config(relief="groove")

miFrame.config(cursor="pirate")



raiz.mainloop() # para que la ventana esté en ejecución debe permanecer a la escucha de eventos