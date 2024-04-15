import re
import requests

url = "https://sre.gob.mx/tramites-y-servicios/pasaportes?id=252"  # Reemplaza esto con la URL de la página que quieres analizar

# Obtener el contenido HTML de la página
respuesta = requests.get(url)
texto_html = respuesta.text

# Aplicar la expresión regular al texto HTML
expresion_regular = re.compile(r"......? ")  # Define tu expresión regular aquí
resultados_busqueda = expresion_regular.finditer(texto_html)

# Imprimir los resultados de la búsqueda
for resultado in resultados_busqueda:
    print(resultado.group(0))
