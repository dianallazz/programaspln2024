archivo_abierto= open("C:\\Users\\diana\\OneDrive\\Documentos\\Escuela\\6B\\optativa1\\texto2.txt","w")
archivo_abierto.write("Esto se escribe en el archivo\n")
archivo_abierto.write("Esto también\n")
archivo_abierto.write("Mira, puedo escribir \"cosillas\"\n")
archivo_abierto.write("Gracias a la diagonal invertida \n")

archivo_abierto.close()

archivo_abierto= open("C:\\Users\\diana\\OneDrive\\Documentos\\Escuela\\6B\\optativa1\\texto2.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()