# componente Button para crear una accion
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi APP...")

#Definimos la funcion accion
def accion():
    label = tkinter.Label(raiz, text="Accion ejecutada")
    label.config(fg="green",bg="lightgrey",font=("Cortana",10))
    label.pack()

# Creacion y configuracion del componente Button con raiz, texto a mostrar y funcion
boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
# configurar area de texto
boton.config(fg="blue")
boton.pack()  

raiz.mainloop()