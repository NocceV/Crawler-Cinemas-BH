from fasthtml.common import Div, H1, P, Button
from search import iniciar 

def pesquisar_filmes(event):
    iniciar() 

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo, style={"textAlign": "center"}),  
        P(subtitulo, style={"textAlign": "center"}), 
        Button(
            "Pesquisar",
            onClick=pesquisar_filmes
        )
    )
