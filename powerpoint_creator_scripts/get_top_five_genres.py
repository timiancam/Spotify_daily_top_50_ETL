import pandas as pd
from collections import Counter

def get_top_five_genres(df):
    """
    finds out what the most popular genres are for a given playlist
    please note that spotify doesn't assign genres to songs
    but to artists
    """
    
    top_five_sorted_genres = []
    
    # Counter function only works with flat lists
    flat_genres = [item for sublist in df['artist_genres'] for item in sublist]
    
    top_five_genres = Counter(flat_genres).most_common(5)
    
    for genre, occurence in top_five_genres:
        for _ in range(occurence):
            top_five_sorted_genres.append(genre.capitalize())
    
    return top_five_sorted_genres
