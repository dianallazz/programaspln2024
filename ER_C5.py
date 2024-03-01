import re

carpeta_nombre = r"C:/Users/diana/OneDrive/Documentos/Escuela/6B/optativa1/"
archivo_nombre = "texto4.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

expresion_regular = re.compile(r"viaj[aeo](s|ero)?", re.IGNORECASE)

resultados_busqueda = expresion_regular.finditer(texto)

for resultado in resultados_busqueda:
    print(resultado.group(0))
