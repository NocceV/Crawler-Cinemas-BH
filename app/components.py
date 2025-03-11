from fasthtml.common import Div, H1, P, Button

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo, style={"textAlign": "center"}),  # Centraliza o texto
        P(subtitulo, style={"textAlign": "center"}),  # Centraliza o texto
        Button(
            "Pesquisar"
        )
    )
