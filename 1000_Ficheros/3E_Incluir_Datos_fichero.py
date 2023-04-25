# Incluir datos en un archivo de texto existente

# nos devuelve un apuntador que guardamos en fichero
# se abrira en modo a de añadir y t texto
# 
fichero = open("fichero_text.txt","at")

cadena_para_incluir = "\nJavaScript"

fichero.write(cadena_para_incluir)

fichero.close()