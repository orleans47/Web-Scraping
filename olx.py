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

# Lista de todos los celulares
celulares = driver.find_elements(By.XPATH, "//li[@data-aut-id= 'itemBox']")

for celular in celulares:
    precio = celular.find_element(By.XPATH, ".//span[@data-aut-id = 'itemPrice']").text
    print(precio)
    descripcion = celular.find_element(By.XPATH,".//span[@data-aut-id = 'itemTitle']").text
    print(descripcion)

