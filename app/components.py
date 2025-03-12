from fasthtml.common import Div, H1, P, Button
from search import iniciar 

def pesquisar_filmes(event):
    """Função chamada ao clicar no botão."""
    iniciar()  # Executa a pesquisa de filmes

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo, style={"textAlign": "center"}),  # Centraliza o texto
        P(subtitulo, style={"textAlign": "center"}),  # Centraliza o texto
        Button(
            "Pesquisar",
            onClick=pesquisar_filmes
        )
    )
