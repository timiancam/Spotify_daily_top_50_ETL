from spotify_extractor_scripts.get_playlist import get_playlist
from spotify_extractor_scripts.get_main_track_info import get_main_track_info
from spotify_extractor_scripts.get_audio_features import get_audio_features
from spotify_extractor_scripts.get_artist_genres import get_artist_genres
from spotify_extractor_scripts.sort_artist_genres import sort_artist_genres
import spotipy
import pandas as pd

def get_playlist_info():
    """
    retrieves all information for a given playlist
    """
    
    playlist_tracks, playlist_name, sp = get_playlist()
    
    main_track_info = get_main_track_info(playlist_tracks)
    
    audio_features = get_audio_features(main_track_info['track_URIs'], sp)
    
    artist_genres = get_artist_genres(main_track_info['artist_URIs'], sp)
    artist_genres = sort_artist_genres(artist_genres, main_track_info['artist_URIs'])
    
    return main_track_info, audio_features, artist_genres, playlist_name
