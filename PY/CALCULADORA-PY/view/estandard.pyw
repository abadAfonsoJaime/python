from tkinter import *

root = Tk()

screenFrame = Frame(root)
screenFrame.pack()

buttonFrame = Frame(root)
buttonFrame.pack()

operacion = ""
resultado = 0

# ------------------------ PANTALLA ------------------------ #
screenInput = StringVar()
storedInput = Listbox()

mainScreen = Entry(screenFrame, textvariable=screenInput)
mainScreen.grid(row=2, column=1, padx=10, columnspan=4)
mainScreen.config(background="black", fg="#03f943", justify="right")

secondPlane = Entry(screenFrame)
secondPlane.grid(row=1, column=1, padx=10, columnspan=4)
secondPlane.config(background="black", fg="#03f943")

# ------------------------ FILA 1 ------------------------ #
_7=Button(buttonFrame, text="7", width=5)
_7.grid(row=1, column=1)
_8=Button(buttonFrame, text="8", width=5)
_8.grid(row=1, column=2)
_9=Button(buttonFrame, text="9", width=5)
_9.grid(row=1, column=3)
divide = Button(buttonFrame, text="/", width=5)
divide.grid(row=1, column=4)

# ------------------------ FILA 2 ------------------------ #
_4=Button(buttonFrame, text="4", width=5)
_4.grid(row=2, column=1)
_5=Button(buttonFrame, text="5", width=5)
_5.grid(row=2, column=2)
_6=Button(buttonFrame, text="6", width=5)
_6.grid(row=2, column=3)
multiply = Button(buttonFrame, text="X", width=5)
multiply.grid(row=2, column=4)

# ----------, width=5-------------- FILA 3 ------------------------ #
_1=Button(buttonFrame, text="1", width=5)
_1.grid(row=3, column=1)
_2=Button(buttonFrame, text="2", width=5)
_2.grid(row=3, column=2)
_3=Button(buttonFrame, text="3", width=5)
_3.grid(row=3, column=3)
rest = Button(buttonFrame, text="/", width=5)
rest.grid(row=3, column=4)


# ------------------------ FILA 4  ------------------------ #
_0=Button(buttonFrame, text="0", width=5)
_0.grid(row=4, column=1)
comma=Button(buttonFrame, text=",", width=5)
comma.grid(row=4, column=2)
equal=Button(buttonFrame, text="=", width=5)
equal.grid(row=4, column=3)
sum = Button(buttonFrame, text="+", width=5)
sum.grid(row=4, column=4)



root.mainloop()