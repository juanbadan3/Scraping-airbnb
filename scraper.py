import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def setup_driver(url):
    """
    Inicializa el controlador de Chrome y carga la URL especificada.

    Args:
        url (str): La URL que se desea cargar.

    Returns:
        WebDriver: Una instancia del controlador de Selenium.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def wait_for_element(driver, xpath, timeout=30):
    """
    Espera hasta que un elemento sea visible en la página.

    Args:
        driver (WebDriver): El controlador de Selenium.
        xpath (str): El XPath del elemento que se está buscando.
        timeout (int): Tiempo máximo de espera en segundos.

    Returns:
        WebElement: El elemento encontrado.
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def wait_for_elements(driver, xpath, timeout=30):
    """
    Espera hasta que varios elementos sean presentes en la página.

    Args:
        driver (WebDriver): El controlador de Selenium.
        xpath (str): El XPath de los elementos que se están buscando.
        timeout (int): Tiempo máximo de espera en segundos.

    Returns:
        list: Una lista de elementos encontrados.
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

def close_property_window(driver):
    """
    Cierra la ventana de la propiedad si hay más de una ventana abierta.

    Args:
        driver (WebDriver): El controlador de Selenium.
    """
    if len(driver.window_handles) > 1:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

def extract_property_data(driver):
    """
    Extrae los datos de una propiedad específica.

    Args:
        driver (WebDriver): El controlador de Selenium.

    Returns:
        list: Una lista con los datos de la propiedad (nombre, ubicación, precio, huéspedes, habitaciones, camas, baños, puntuación).
    """
    try:
        property_name = wait_for_element(driver, '//h2[@class="hpipapi atm_7l_1kw7nm4 atm_c8_1x4eueo atm_cs_1kw7nm4 atm_g3_1kw7nm4 atm_gi_idpfg4 atm_l8_idpfg4 atm_kd_idpfg4_pfnrn2 dir dir-ltr"]').text

        # Manejo de ubicación
        try:
            location = wait_for_element(driver, '//div[@class="_152qbzi"]').text.strip()
        except Exception:
            location = wait_for_element(driver, '//div[@class="_1t2xqmi"]').text.strip()

        # Manejo de precio
        try:
            price = wait_for_element(driver, '//div[@class="_1avmy66"]').text.strip()
        except Exception:
            price = wait_for_element(driver, '//span[contains(@class, "_1k4xcdh")]').text.strip()

        # Extraer otras informaciones
        guests = wait_for_element(driver, '//li[contains(@class, "l7n4lsf") and contains(text(), "huéspedes")]').text
        rooms = wait_for_element(driver, '//li[contains(@class, "l7n4lsf") and (contains(text(), "habitaciones") or contains(text(), "habitación"))]').text
        try:
            beds = wait_for_element(driver, '//li[contains(@class, "l7n4lsf") and contains(text(), "cama")]').text
        except Exception:
                beds = "informacion no disponible"
        baths = wait_for_element(driver, '//li[contains(@class, "l7n4lsf") and contains(text(), "baño")]').text
        
        # Extraer la puntuación de reseñas
        try:
            rating = wait_for_element(driver, '//div[contains(@class, "a8jhwcl")]').text
        except Exception:
            rating = wait_for_element(driver, '//div[contains(@class, "r1lutz1s ")]').text

        return [property_name, location, price, guests, rooms, beds, baths, rating]
    except Exception as e:
        print(f'Ocurrió un error al extraer información de la propiedad: {traceback.format_exc()}')
        return None

def save_to_csv(data):
    """
    Guarda los datos extraídos en un archivo CSV.

    Args:
        data (list): Los datos a guardar.
    """
    if data:
        with open('properties_data3.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Nombre', 'Ubicación', 'Precio', 'Huéspedes', 'Habitaciones', 'Camas', 'Baños', 'Puntuación'])
            writer.writerows(data)
    else:
        print("No se extrajeron datos para guardar.")

def main():
    """
    Función principal que orquesta el proceso de extracción de datos de propiedades de Airbnb.
    """
    url = 'https://www.airbnb.com.co/s/Barcelona--Espa%C3%B1a/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-11-01&monthly_length=3&monthly_end_date=2025-02-01&price_filter_input_type=0&channel=EXPLORE&query=Barcelona%2C%20Espa%C3%B1a&place_id=ChIJ5TCOcRaYpBIRCmZHTz37sEQ&date_picker_type=calendar&checkin=2024-10-31&checkout=2024-11-01&adults=1&source=structured_search_input_header&search_type=filter_change&search_mode=flex_destinations_search&price_filter_num_nights=1&category_tag=Tag%3A4104&location_search=MIN_MAP_BOUNDS&room_types%5B%5D=Entire%20home%2Fapt'
    
    driver = setup_driver(url)
    properties_data = []
    num_properties_scraped = 0

    try:
        while num_properties_scraped < 100:
            time.sleep(5)

            images = wait_for_elements(driver, '//div[contains(@class, "cy5jw6o")]')
            for i in range(min(17, len(images))):
                if num_properties_scraped >= 100:
                    break
                    
                images[i].click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])

                # Intentar cerrar la ventana de la propiedad
                try:
                    close_button = wait_for_element(driver, '//button[@aria-label="Cerrar"]', timeout=10)
                    close_button.click()
                except Exception:
                    pass

                property_data = extract_property_data(driver)
                if property_data:
                    properties_data.append(property_data)
                    num_properties_scraped += 1
                
                close_property_window(driver)

            if num_properties_scraped < 100:
                try:
                    next_button = wait_for_element(driver, '//a[@aria-label="Siguiente"]')
                    next_button.click()
                    time.sleep(5)
                except Exception:
                    print("No se pudo encontrar el botón de siguiente o se alcanzó el final de las páginas.")
                    break

    finally:
        save_to_csv(properties_data)
        driver.quit()
        print('La acción finalizó con éxito')

if __name__ == "__main__":
    main()
