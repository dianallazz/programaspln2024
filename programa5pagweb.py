import requests
from bs4 import BeautifulSoup
import re

#url = "https://sre.gob.mx/tramites-y-servicios/pasaportes?id=252"  # URL de la página que quieres analizar

url= input("Ingrese el url que quiere analizar: ")

# Obtener el contenido HTML de la página
respuesta = requests.get(url)
texto_html = respuesta.text

# Crear un objeto BeautifulSoup para parsear el HTML
soup = BeautifulSoup(texto_html, 'html.parser')

# Obtener el texto sin etiquetas
texto_sin_etiquetas = soup.get_text()

# Imprimir el texto sin etiquetas
print(texto_sin_etiquetas)

# Aplicar la expresión regular al texto sin etiquetas
expresion_regular = re.compile(r"......? ")  # Define tu expresión regular aquí
resultados_busqueda = expresion_regular.finditer(texto_sin_etiquetas)

# Imprimir los resultados de la búsqueda
for resultado in resultados_busqueda:
    print(resultado.group(0))
