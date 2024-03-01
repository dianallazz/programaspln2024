carpeta_nombre = r"C:/Users/diana/OneDrive/Documentos/Escuela/6B/optativa1/"  
archivo_nombre = "texto1.txt"  

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

palabras_lista = texto.split()
palabras_lista.sort()

for palabra in palabras_lista:
    print(palabra)
