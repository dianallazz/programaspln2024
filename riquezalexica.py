
import clase7nlk

clase7nlk.download('punkt')
carpeta_nombre = r"C:/Users/diana/OneDrive/Documentos/Escuela/6B/programaspln2024/"
archivo_nom="texto8.txt"
with open(carpeta_nombre + archivo_nom, "r") as archivo:

    texto=archivo.read()
tokens=clase7nlk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
riquiza_lexica=palabras_diferentes/palabras_totales
print("riqueza lexica: ",riquiza_lexica)
