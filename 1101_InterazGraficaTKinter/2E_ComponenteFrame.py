# componente Frame
# importamos el modulo
import tkinter

#Crear componente raiz
raiz = tkinter.Tk()
raiz.title("Mi APP...")

# Creacion y configuracion del componente Frame
# permite incluir otros componentes dentro de Frame
# sobre que raiz se agrega
# devuelve un frame
compFrame = tkinter.Frame(raiz)
# configguracion del frame color, ancho y alto
compFrame.config(bg="blue",width=400,height=300)
# pack para mostrar por pantalla
compFrame.pack()

# para ejecucion 
raiz.mainloop()