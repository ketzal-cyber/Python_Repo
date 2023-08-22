# componente MessageBox para hacer una pregunta
import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi APP...")

def preguntar():
    # devuelve un resultado, lo que contesto el usuario
    resultado = tkinter.messagebox.askquestion("Question", "¿Quieres borrar este fichero?")
    if (resultado == "yes"):
        print("Borrando el fichero...")
    else:
        print("No se Borrara el fichero...")

# Creacion y configuracion del componente MessageBox ventana de informacion
#  con raiz, texto a mostrar,
#  funcion preguntar 
boton = tkinter.Button(raiz, text="Avisar", command=preguntar)
boton.pack() 
  

raiz.mainloop()