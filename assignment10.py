
"""C2: Rule-based movie recommendation system (genre, language, type)."""
MOVIES = [
    {"title": "Avengers: Endgame", "genre": "action", "language": "english", "type": "movie"},
    {"title": "Mission Impossible", "genre": "action", "language": "english", "type": "movie"},
    {"title": "War", "genre": "action", "language": "hindi", "type": "movie"},
    {"title": "3 Idiots", "genre": "comedy", "language": "hindi", "type": "movie"},
    {"title": "Hera Pheri", "genre": "comedy", "language": "hindi", "type": "movie"},
    {"title": "The Office", "genre": "comedy", "language": "english", "type": "series"},
    {"title": "Interstellar", "genre": "sci-fi", "language": "english", "type": "movie"},
    {"title": "The Matrix", "genre": "sci-fi", "language": "english", "type": "movie"},
    {"title": "Stranger Things", "genre": "sci-fi", "language": "english", "type": "series"},
    {"title": "Taare Zameen Par", "genre": "drama", "language": "hindi", "type": "movie"},
    {"title": "The Pursuit of Happyness", "genre": "drama", "language": "english", "type": "movie"},
    {"title": "Panchayat", "genre": "drama", "language": "hindi", "type": "series"},
]
 
 
def recommend(genre, language="any", kind="any"):
    """IF genre = g AND language = l AND type = t THEN recommend matching titles.
    'any' acts as a wildcard."""
    result = []
    for m in MOVIES:
        if (m["genre"] == genre
                and language in ("any", m["language"])
                and kind in ("any", m["type"])):
            result.append(m)
    return result
 
 
def ask(prompt, default):
    try:
        value = input(prompt).strip().lower()
        return value if value else default
    except EOFError:
        return default
 
 
if __name__ == "__main__":
    genres = sorted({m["genre"] for m in MOVIES})
    print("Available genres:", ", ".join(genres))
    genre = ask("Enter your preferred genre [default: sci-fi]: ", "sci-fi")
    language = ask("Preferred language (english/hindi/any) [default: any]: ", "any")
    kind = ask("Type (movie/series/any) [default: any]: ", "any")
    results = recommend(genre, language, kind)
    if results:
        print("\nRecommended:")
        for m in results:
            print(f"- {m['title']} ({m['language'].title()}, {m['type']})")
    else:
        fallback = recommend(genre)
        if fallback:
            print("\nNo exact match. Other", genre, "titles:")
            for m in fallback:
                print(f"- {m['title']} ({m['language'].title()}, {m['type']})")
        else:
            print("Sorry, no recommendation available.")
