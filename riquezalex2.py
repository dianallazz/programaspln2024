import clase7nlk

def riqueza_lexica(tokens):
    tokens_conjunto=set(tokens)
    palabras_totales=len(tokens)
    palabras_diferentes=len(tokens_conjunto)
    riqueza_lexica=palabras_diferentes/palabras_totales
    return riqueza_lexica


carpeta_nombre = r"C:/Users/diana/OneDrive/Documentos/Escuela/6B/programaspln2024/"
archivo_nombre="texto8.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto=archivo.read()

tokens=clase7nlk.word_tokenize(texto,"spanish")
riqueza_lexica=riqueza_lexica(tokens)
print("riqueza lexica: ",riqueza_lexica)
