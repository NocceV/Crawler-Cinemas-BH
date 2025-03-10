from fasthtml.common import *
from components import gerar_titulo
app,routes = fast_app()

@routes("/")
def homePage():
    return gerar_titulo("Pesquisador de Filmes", "Clique no botão para iniciar a pesquisa dos filmes em cartaz")

serve()