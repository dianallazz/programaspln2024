import clase7nlk

clase7nlk.download('punkt')

carpeta_nombre = r"C:/Users/diana/OneDrive/Documentos/Escuela/6B/programaspln2024/"
archivo_nombre="texto7.txt"
with open(carpeta_nombre + archivo_nombre, "r") as archivo:

    texto=archivo.read()
tokens=clase7nlk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

palabras_totales=len(tokens)
print("el total de palabras es: ",palabras_totales)