
c="C:\\Users\\diana\\OneDrive\\Documentos\\Escuela\\6B\\optativa1\\"
e="texto2.txt"

s="texto3-class2.txt"

e2=open(c+e,"r")

#print(e2.read())

s2=open(c+s,"w")
t=e2.read()
t2=t
s2.write(t2)

e2.close()
s2.close()

#____Forma 1_____
#s3=open(c+s,"r")
#print(s3.read())
#s3.close()

#____Forma 2_____

with open(c+s,"r") as archivo:
    texto=archivo.read()
print(texto)
palabra=input("Escribe la palabra a buscar: ")

if palabra in texto:
    print("Si encontró la palabra: ", palabra)
else: 
    print("No se encontró la palabra")
