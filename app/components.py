from fasthtml.common import Div, H1, P, Button

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo, style={"textAlign": "center"}),  # Centraliza o texto
        P(subtitulo, style={"textAlign": "center"}),  # Centraliza o texto
        Button(
            "Pesquisar",
            style={
                "backgroundColor": "black",
                "color": "white",
                "border": "none",
                "padding": "10px 20px",
                "cursor": "pointer",
                "marginTop": "10px",
            }
        ),
        style={
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "alignItems": "center",
            "height": "100vh",
            "backgroundColor": "white",
        }
    )
