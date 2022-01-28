import chromedriver_autoinstaller
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = Chrome()
waiter = WebDriverWait(driver, 10)

# Entrar no google
driver.get("https://www.google.com.br")

# Pesquisar a temperatura no google
input_search: WebElement = waiter.until(EC.presence_of_element_located((By.NAME, "q")))
input_search.send_keys("temperatura na zona sul sp" + Keys.ENTER)

# Obter a temperatura
temp_celsius: WebElement = waiter.until(
    EC.presence_of_element_located((By.ID, "wob_tm"))
)


print(f"A temperatura na Zona sul em SP é: {temp_celsius.text}°C.")

driver.close()
