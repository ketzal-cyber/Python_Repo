# componente RadioButton para seleccion opcion multiple
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi APP...")

#Definimos la funcion accion
def seleccionar():
    label = tkinter.Label(raiz, text="Opcion {}  seleccionada".format(opcion.get()))
    label.config(fg="green",bg="lightgrey",font=("Cortana",10))
    label.pack()

opcion = tkinter.IntVar()
# Creacion y configuracion del componente RadioButton
#  con raiz, texto a mostrar,
#  variable opcion con valor 1 y ejecutara funcion seleccionar
radioButon = tkinter.Radiobutton(raiz, text="Opcion1", variable=opcion, value=1, command=seleccionar)
radioButon.pack() 
radioButon1 = tkinter.Radiobutton(raiz, text="Opcion2", variable=opcion, value=2, command=seleccionar)
radioButon1.pack() 
radioButon2 = tkinter.Radiobutton(raiz, text="Opcion3", variable=opcion, value=3, command=seleccionar)
radioButon2.pack()  

raiz.mainloop()