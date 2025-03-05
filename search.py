from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

class moviesResearcher:
    def __init__(self):
        self.SITE_LINK = "https://www.ingresso.com/cinema/cinemark-bh-shopping?city=belo-horizonte"
        self.SITE_MAP = {
            "movies":{
                "movie":{
                        "xpath" : "/html/body/div[2]/div/main/section/div[3]/div/div[1]/div[3]/div[1]/div[2]/h3/a"
                    }
            }
        }

        service = Service("C:\\WebDrivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
    

    def open_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def capture_movies(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.text-white.no-underline')
        for title in elements:
            print(title.text)


teste = moviesResearcher()
teste.open_site()
teste.capture_movies()