# componente Label
# importamos el modulo
import tkinter

#Crear componente raiz
raiz = tkinter.Tk()
raiz.title("Mi APP...")

texto = "Hola Mundo"
# Creacion y configuracion del componente Label pasandole la raiz y el texto
etiqueta = tkinter.Label(raiz,text=texto)
# configuracion del label color fuente  fondo de texto, tipo de fuente y tamaño
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
# pack para mostrar por pantalla
etiqueta.pack()

# para ejecucion 
raiz.mainloop()