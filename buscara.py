import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# URL de la página web
url = "https://example.com"  # Reemplaza con la URL correcta

# Realizar la solicitud GET a la página web
response = requests.get(url)

# Crear el objeto BeautifulSoup a partir del contenido HTML
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar todos los elementos <a> con la función onclick
elements = soup.find_all("a", onclick=True)

# Variable para almacenar si se encontró el texto en algún elemento
found_text = False

# Recorrer cada elemento <a> y verificar si el texto está presente en la función onclick
for element in elements:
    onclick_value = element["onclick"]
    if "indicadores_dengue_diario_distrito.xlsx" in onclick_value:
        found_text = True

        # Hacer clic en el elemento utilizando Selenium
        driver = webdriver.Chrome()  # Reemplaza con el controlador de navegador adecuado
        driver.get(url)
        driver.execute_script(onclick_value)
        driver.quit()

        break

# Continuar con el código después de hacer clic en el elemento <a>, si es necesario
if found_text:
    # Código adicional después de hacer clic en el elemento <a>
    print("Se hizo clic en el elemento <a>.")
else:
    print("El texto no está presente en ningún elemento <a>.")