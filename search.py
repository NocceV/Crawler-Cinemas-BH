from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configuração do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rodar sem abrir o navegador
chrome_options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1")

servico = Service("CAMINHO_DO_SEU_CHROMEDRIVER")  # Substitua pelo caminho do seu chromedriver
driver = webdriver.Chrome(service=servico, options=chrome_options)

# Acessa o site
url = "https://www.ingresso.com/cinema/cinemark-bh-shopping?city=belo-horizonte"
driver.get(url)
time.sleep(5)  # Espera carregar o JavaScript

# Pega os títulos dos filmes
filmes = driver.find_elements(By.CSS_SELECTOR, "h3.text-white")  # Ajuste conforme necessário
for filme in filmes:
    print(filme.text)

# Fecha o navegador
driver.quit()