import requests
from bs4 import BeautifulSoup

link = "https://www.ingresso.com/cinema/cinemark-bh-shopping?city=belo-horizonte"
link2 = "https://www.google.com/search?q=cinemark+pátio+savassi+filmes"
text = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
headers = {"User-Agent": text}

requisicao = requests.get(link, headers = headers)



# print(requisicao)
# # print(requisicao.text)

site =BeautifulSoup(requisicao.text, "html.parser")

pesquisa = site.find("a", class_="text-white no-underline")
# print(site.prettify())



titulo = site.title
titulo2 = site.h2
print(titulo)
print(titulo2)