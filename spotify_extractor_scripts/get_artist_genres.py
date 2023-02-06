import spotipy as sp
import pandas
from spotify_extractor_scripts.remove_dupes_and_flatten import remove_dupes_and_flatten
from spotify_extractor_scripts.adjust_artist_URIs_size import adjust_artist_URIs_size

def get_artist_genres(artist_URIs, sp):   
    """
    retrieves the genres for a given artist in a given playlist
    one artist can appear more than once in a playlist and must be removed
    the API call only accepts a maximum list size of 50
    so the artist_list is adjusted
    """
    
    genres = {}
    
    # playlist can contain multiples of one artist
    artist_URIs = remove_dupes_and_flatten(artist_URIs)
    
    # Spotify artist API call can only process 50 URIs
    # adjusts the list to contain lists of max size 50
    artist_URIs = adjust_artist_URIs_size(artist_URIs)
    
    # retrieves genres for each artist
    # see spotipy documentation
    genres_object = [sp.artists(subset) for subset in artist_URIs]
    
    # creates a dictionary where the key is artist_URIs
    # and the values are the genres
    # indexing of genres_object is the same as indexing of artist_URIs
    for idx_subset, subset in enumerate(genres_object):
        for idx_artist, artist in enumerate(subset['artists']):
            genres[artist_URIs[idx_subset][idx_artist]] = artist['genres']
    
    return genres
