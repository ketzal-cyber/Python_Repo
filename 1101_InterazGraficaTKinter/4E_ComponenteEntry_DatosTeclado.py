# componente Entry Entrada de datos por teclado
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi APP...")

# Creacion y configuracion del componente Entry
entrada = tkinter.Entry(raiz)
entrada.config(justify="center")
entrada.pack()  

raiz.mainloop()