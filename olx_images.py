import requests
from time import sleep
from PIL import Image
import io
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.olx.com.co/jamundi_g4069086/telefonos-celulares_c831")



# Encuentra el botón de carga para seguir obteniendo los datos en la página
for i in range(10):
    try:
        # Crea tiempo de espera por eventos
        boton = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@data-aut-id= 'btnLoadMore']"))
        )
        # Dale click
        boton.click()
        # Espera la carga de la página 
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//li[@data-aut-id= 'itemBox']//span[@data-aut-id = 'itemPrice']"))
        )
                  
    except:
        break

# Scroll the pages to load the images
driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'})")
sleep(5)
driver.execute_script("window.scrollTo({top: 20000, behavior: 'smooth'})")
sleep(5)


# Lista de todos los celulares
celulares = driver.find_elements(By.XPATH, "//li[@data-aut-id= 'itemBox']")

for i, celular in enumerate(celulares):
    precio = celular.find_element(By.XPATH, ".//span[@data-aut-id = 'itemPrice']").text
    print(precio)
    descripcion = celular.find_element(By.XPATH,".//span[@data-aut-id = 'itemTitle']").text
    print(descripcion)

    try:
        url = celular.find_element(By.XPATH, ".//img").get_attribute("src")
        image_content = requests.get(url).content

        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        path = "C:/Users/Alejandro Dinas.DESKTOP-B98QDHD/Documents/python/images/" + str(i) +".jpg"
        with open(path, "wb") as f:
            image.save(f,"JPEG", quality= 85)

    except:
        print("error")


