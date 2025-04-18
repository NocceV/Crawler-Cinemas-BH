from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

links = ["https://www.ingresso.com/cinema/cinemark-bh-shopping?city=belo-horizonte","https://www.ingresso.com/cinema/cineart-boulevard?city=belo-horizonte" \
         ,"https://www.ingresso.com/cinema/cineart-minas-shopping?city=belo-horizonte","https://www.ingresso.com/cinema/cineart-del-rey?city=belo-horizonte",\
            "https://www.ingresso.com/cinema/cinemark-diamond-mall?city=belo-horizonte","https://www.ingresso.com/cinema/cinepolis-estacao-bh?city=belo-horizonte",\
                "https://www.ingresso.com/cinema/cinemark-patio-savassi?city=belo-horizonte"]

class moviesResearcher:

    def __init__(self,link):
        """
        Initialize the movie searcher class, containing the site link
        and the site dictionary map containing xpath, initializing the selenium getter
        """
        self.SITE_LINK = link
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
        """
        Open the actual link
        """
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(2)

    def get_siteName(self):
        """
        Get and return the site/cinema name
        """
        site_name = self.driver.find_element(By.CSS_SELECTOR, '.line-clamp-3.align-middle.text-lg.leading-none.lg\\:text-2xl')
        return site_name.text

    def capture_movies(self):
        """
        Get all movies status like schedule and type
        """
        movie_blocks = self.driver.find_elements(By.CSS_SELECTOR, ".relative.my-5.scroll-mt-\\[250px\\].overflow-hidden.rounded-\\[10px\\].bg-ing-neutral-600.p-4")
        movies_list = []

        for block in movie_blocks:
            try:
                title_movie = block.find_element(By.CSS_SELECTOR, '.text-white.no-underline')
                title = title_movie.text.strip()

                schedules_movie = block.find_elements(By.CSS_SELECTOR, '.mt-4.flex.flex-wrap.gap-2')
                schedule = []
                for time in schedules_movie:
                    schedule.append(time.text.strip())
                
                movie_map = {
                    "title": title,
                    "schedule": schedule
                }
                movies_list.append(movie_map)

            except Exception as e:
                print(f"Erro ao capturar filme: {e}")
        
        return movies_list

    def write_movies(self,movies_list):
        """
        Write all movies statistics
        """
        for movie in movies_list:
            print(f"🎬 Filme: {movie['title']}")
            if movie['schedule']:
                print(f"⏰ Horários: {', '.join(movie['schedule'])}")
            else:
                print("Nenhum horário disponível")
            print("-" * 50)

    def close(self):
        """
        CLose the window
        """
        self.driver.quit()

def start():
    """
    Start the searching process
    """
    all_movies = []
    all_cinema_names = []
    
    for link in links:
        core = moviesResearcher(link)
        core.open_site()
        cinema_name = core.get_siteName()
        all_cinema_names.append(cinema_name)  
        movies_list = core.capture_movies()
        
       
        for movie in movies_list:
            movie["cinema"] = cinema_name 
        
        all_movies.extend(movies_list)  
        core.close()
    
    return all_movies