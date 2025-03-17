from fasthtml.common import *
from components import gerar_titulo
app,routes = fast_app()

@routes("/")
def homePage():
    from search import iniciar
    moviesList = iniciar()  # Chama automaticamente ao carregar a página
    return gerar_titulo("Pesquisador de Filmes", "Resultado da busca de filmes em cartaz:",moviesList)

serve()
