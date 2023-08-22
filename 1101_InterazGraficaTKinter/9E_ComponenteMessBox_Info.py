# componente MessageBox ppara mostrar informacion
import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi APP...")

def aviso():
    print()
    tkinter.messagebox.showinfo("Titulo", "Mensaje con la información")

# Creacion y configuracion del componente MessageBox ventana de informacion
#  con raiz, texto a mostrar,
#  funcion aviso 
boton = tkinter.Button(raiz, text="Avisar", command=aviso)
boton.pack() 
  

raiz.mainloop()