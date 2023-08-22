# componente Filedialog para seleccionar un fichero
import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi APP...")

def abrirFichero():
    # devuelve un resultado, lo que contesto el usuario
    rutaFichero = filedialog.askopenfilename(title="Seleccionar fichero...")
    print(rutaFichero)

# Creacion y configuracion del componente MessageBox ventana de informacion
#  con raiz, texto a mostrar,
#  funcion preguntar 
boton = tkinter.Button(raiz, text="Empezar", command=abrirFichero)
boton.pack() 
  

raiz.mainloop()