import nltk

carpeta_nombre = r"C:/Users/diana/OneDrive/Documentos/Escuela/6B/programaspln2024/"
archivo_nombre = "texto8.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
    tokens=nltk.word_tokenize(texto,"spanish")
    texto_nltk=nltk.Text(tokens)
    texto_nltk.similar("familia")