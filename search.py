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

        #Pega os blocos de filmes, ou seja raspa os dados dentro deste pai
        movie_blocks = self.driver.find_elements(By.CSS_SELECTOR, ".relative.my-5.scroll-mt-\\[250px\\].overflow-hidden.rounded-\\[10px\\].bg-ing-neutral-600.p-4")
        #Criação de lista que ira guaardar os filmes 
        movies_list = []

        #Para cada filme dentro do bloco de filmes
        for block in movie_blocks:
            try:
                #Pega o titulo do atual bloco de filme
                title_movie = block.find_element(By.CSS_SELECTOR, '.text-white.no-underline')
                title = title_movie.text.strip()

                # schedules_movie = block.find_elements(By.CSS_SELECTOR, '.mt-4.flex.flex-wrap.gap-2')
                # schedule = [time.text.strip() for time in schedules_movie]
                
                # movie_map = {
                #     "title": title,
                #     # "schedule": schedule
                # }
                #Adiciona o titulo do filme na lista de filmes
                movies_list.append(title)                
            except Exception as e:
                print(f"Erro ao capturar filme: {e}")
        
        #Printa todos os titulos de filmes contidos no site
        for movie in movies_list:
            print(f"🎬 Filme: {movie}")
            # print(f"⏰ Horários: {', '.join(movie['times']) if movie['times'] else 'Nenhum horário disponível'}")
            print("-" * 50)


teste = moviesResearcher()
teste.open_site()
teste.capture_movies()