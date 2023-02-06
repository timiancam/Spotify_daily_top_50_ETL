import pandas as pd
from spotify_extractor_scripts.remove_dupes_and_flatten import remove_dupes_and_flatten

def sort_artist_genres(artist_genres, artist_URIs):
    """
    the indexing of artist genres is not consistent with the indexing of the playlist
    this function sorts the genres so that the subsequent dataframe can be properly defined
    the correct indexing comes from the passed argument artist_URIs
    """
    
    temp_genres = artist_genres
    
    # empty the list so that a properly sorted list can be returned
    artist_genres = []
    
    for subset in artist_URIs:
        temp_list = []
        for uri in subset:
            temp_list.append(temp_genres[uri])
        
        # one song can contain multiple artists
        # artists can share the same genre
        # list needs to be flattened so that duplicate genres can be removed 
        temp_list = remove_dupes_and_flatten(temp_list)
        
        artist_genres.append(temp_list)
    
    return artist_genres
