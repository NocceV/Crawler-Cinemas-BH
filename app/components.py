from fasthtml.common import Div, H1, P, Button, A
from search import iniciar 

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo, style={"textAlign": "center"}),  
        P(subtitulo, style={"textAlign": "center"}), 
        A("Clique aqui para pesquisar", href="/pesquisar", style={"display": "block", "textAlign": "center", "color": "blue", "cursor": "pointer"})
    )
