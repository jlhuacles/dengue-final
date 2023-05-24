from bs4 import BeautifulSoup
import requests
import re 
import base64

url = 'https://www.dge.gob.pe/sala-situacional-dengue/diaria/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
elements = soup.find_all("a", onclick=True)

encontrado = ""
found_text = False
# Encontrar el enlace de descarga del archivo Excel
for element in elements:
    onclick_value = element["onclick"]
   
    if "indicadores_dengue_diario_distrito.xlsx" in onclick_value:
        found_text = True
        encontrado = element
        break

# Imprimir el resultado
if found_text:
    print("El texto está presente en al menos un elemento <a>.")
   
else:
    print("El texto no está presente en ningún elemento <a>.")


texto_base64 = ''
patron_busqueda = r'base64,(.*?)\'\)\.then'
resultado = re.search(patron_busqueda, encontrado['onclick'])
if resultado:
    texto_base64 = resultado.group(1)
    print("Texto Base64 encontrado:", texto_base64)
else:
    print("Texto Base64 no encontrado.")


decoded_data = base64.b64decode(texto_base64)

# Guardar el archivo decodificado
file_path = "indicadores_dengue_diario_distrito.xlsx"  # Ruta y nombre del archivo de salida
with open(file_path, "wb") as file:
    file.write(decoded_data)

print("Archivo guardado correctamente. Gracias")