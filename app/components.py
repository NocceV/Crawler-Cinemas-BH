from fasthtml.common import Div, H1, P, A, Ul, Li, Strong

def generate_title(titulo, subtitulo, movies_list):
    # Agrupar filmes por cinema
    cinema_dict = {}
    for movie in movies_list:
        cinema_name = movie["cinema"]
        if cinema_name not in cinema_dict:
            cinema_dict[cinema_name] = []
        cinema_dict[cinema_name].append(movie)

    return Div(
        H1(titulo, style={"textAlign": "center"}),  
        P(subtitulo, style={"textAlign": "center"}), 
        Ul(
            *[
                Li(
                    Strong(f"📍 {cinema}"), 
                    Ul(
                        *[
                            Li(f"🎬 {movie['title']} - ⏰ {', '.join(movie['schedule'])},")
                            for movie in movies
                        ], style={"listStyleType": "none", "marginLeft": "20px"}
                    )
                )
                for cinema, movies in cinema_dict.items()
            ], 
            style={"textAlign": "center", "listStyleType": "none"}
        ) if movies_list else P("Nenhum filme encontrado.", style={"textAlign": "center"}),
        A("Clique aqui para pesquisar", href="/pesquisar", style={"display": "block", "textAlign": "center", "color": "blue", "cursor": "pointer"})
    )