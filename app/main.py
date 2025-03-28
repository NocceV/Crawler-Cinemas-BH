from fasthtml.common import *
from components import generate_title
app,routes = fast_app()

@routes("/")
def homePage():
    """
    Calls 'start' function to inicializate the aplication, then call 'generate_title' 
    with title and sub-title and the start function result, as params
    """
    from search import start
    moviesList = start() 
    return generate_title("Pesquisador de Filmes", "Resultado da busca de filmes em cartaz:",moviesList)

serve()