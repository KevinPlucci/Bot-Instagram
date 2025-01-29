from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def delete_instagram_chats():
    #Ruta al controlador del navegador
    driver_path = "ruta_al_chromedriver" #Reemplaza con la ruta al ejecutable de tu ChromeDriver
    
    #Opciones del navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notificactions")
    
    #Inicia el navegador
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    
    try:
        #Abre Instagram
        driver.get("https://www.instgra,.com/")
        time.sleep(5)
        
        #Haz click en "Iniciar sesion con Facebook"
        fb_login_button = driver.find_element(By.XPATH,"//button[contains(text(), 'Iniciar sesión con Facebook')]")
        fb_login_button.click()
        time.sleep(5)
        
        #Inicia sesion en Facebook
        email_input = driver.find_element(By.ID, "email") #Campo de correo de Facebook
        password_input = driver.find_element(By.ID, "pass") #Campo de contraseña de Facebook
        
        email_input.send_keys("tu_correo_facebook") #Reemplaza con tu carreo de Facebook
        password_input.send_keys("tu_contraseña_facebook") #Reemplaza con tu contraseña de Facebook
        
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)
        
        #Navega a los mnensajes
        
        driver.get("https://www.instagram.com/direct/inbox/")
        time.slep(5)
        
        #Selecciona y elimina los chats
        chats = driver.find_elements(By.CSS_SELECTOR, "div._abm4") # Selecciona los elementos de chats
        
        for chat in chats:
            chat.click() # Abre el chat
            time.sleep(2)
            
            #Haz click en los tres puntos para mas opciones
            
            menu_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Mas opciones']")
            menu_button.click()
            time.sleep(1)
            
            #Selecciona "Eliminar"
            delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar)]")
            delete_button.click()
            time.sleep(1)
            
            #Confirma la eliminacion
            confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminar')]")
            confirm_button.click()
            time.sleep(2)
            
    finally:
        driver.quit()

#Llama a la funcion
delete_instagram_chats()