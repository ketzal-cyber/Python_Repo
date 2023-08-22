# componente Text Entrada de varias lineas  como campos tipo comentarios
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi APP...")

# Creacion y configuracion del componente Text
entradaText = tkinter.Text(raiz)
# configurar area de texto
#   tamaño del are, fuente tamaño letra
#   margen del borde al texto, color de fuente y colo de seleccion
entradaText.config(width=20,height=10, font=("verdana",10), padx=10, pady=10, fg="green", selectbackground="lightgrey" )
entradaText.pack()  

raiz.mainloop()