"""
# El modulo Tkinter tiene una serie de componenetes llamados widgets
# Los   widgets son componentes graficos
# Tk es el componente raiz que contiene al resto de componentes
# Frame es un marco que puede contener otros widgets y tiene un tamaño propio
- Label es una etiqueta donde podemos insertar un texto
- Entry es un campo de texto sencillo para escribir un texto corto como un nombre de un formulario
- Text es un campo de texto grande para escribir  varias lineas  de texto
- Button es un botón sobre el cual se puede hacer un clic
- RadioButton es un botón para elegir una opcion entre varias posibilidades
- CheckButton es un botón para marcar un opcion de tipo tic activado/desactivado
- Menu es un componente para crear menus de las aplicaciones
- Dialogs es un componente para crear ventanas emergentes para mostrar informacion
    al usuario, como alertas o confirmaciones
"""
import tkinter

# la funcion Tk devuelve el elemento raiz
raiz = tkinter.Tk()
raiz.title("Mi APP Python...")

# linea para iniciar y este asta que se cierre el componente
raiz.mainloop()