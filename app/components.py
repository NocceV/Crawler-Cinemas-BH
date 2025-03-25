from fasthtml.common import Div, H1, P, Button, A, Ul, Li

def gerar_titulo(titulo, subtitulo, movies_list):
    return Div(
        H1(titulo, style={"textAlign": "center"}),  
        P(subtitulo, style={"textAlign": "center"}), 
        Ul(
            *[Li(f"🎬 {movie['title']} - ⏰ {', '.join(movie['schedule'])}") for movie in movies_list], 
            style={"textAlign": "center", "listStyleType": "none"}
        ) if movies_list else P("Nenhum filme encontrado.", style={"textAlign": "center"}),
        A("Clique aqui para pesquisar", href="/pesquisar", style={"display": "block", "textAlign": "center", "color": "blue", "cursor": "pointer"})
    )
