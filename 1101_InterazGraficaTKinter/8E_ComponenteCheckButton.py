# componente CheckButton oton de verificacion
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi APP...")

#Definimos la funcion accion
def verificar():
    if (check1.get() == 1):
        label = tkinter.Label(raiz, text="Opcion {}  veriicada".format(check1.get()))
        label.config(fg="green",bg="lightgrey",font=("Cortana",10))
        label.pack()
    else:
        label = tkinter.Label(raiz, text="Opcion {}  No veriicada".format(check1.get()))
        label.config(fg="green",bg="lightgrey",font=("Cortana",10))
        label.pack()

check1 = tkinter.IntVar()
# Creacion y configuracion del componente CheckButton
#  con raiz, texto a mostrar,
#  variable check1 con valor 1 activadda y 0 no activada, ejecutara funcion verificar
checkButon = tkinter.Checkbutton(raiz, text="Opcion1", variable=check1, onvalue=1, offvalue=0, command=verificar)
checkButon.pack() 
  

raiz.mainloop()