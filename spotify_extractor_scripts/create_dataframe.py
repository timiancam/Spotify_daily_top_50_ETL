from spotify_extractor_scripts.get_playlist_info import get_playlist_info
import pandas as pd
from ETL_path_manager_scripts.ETL_path_manager import get_path

def create_dataframe():
    """
    creates a dataframe which is then written to a .csv file
    first retrieves all information for a given playlist
    """
    
    main_track_info, audio_features, artist_genres, playlist_name = get_playlist_info()
    
    data = {
        'track_URI':            main_track_info['track_URIs'],
        'track_name':           main_track_info['track_names'],
        'album_name':           main_track_info['track_albums'],
        'album_image_URL':      main_track_info['track_album_URLs'],
        'artists_URIs':         main_track_info['artist_URIs'],
        'artists':              main_track_info['track_artists'],
        'artist_genres':        artist_genres,
        'danceability':         audio_features['danceability'],
        'energy':               audio_features['energy'], 
        'loudness':             audio_features['loudness'], 
        'speechiness':          audio_features['speechiness'],
        'acousticness':         audio_features['acousticness'], 
        'instrumentalness':     audio_features['instrumentalness'], 
        'liveness':             audio_features['liveness'], 
        'valence':              audio_features['valence']
    }
    
    dataframe = pd.DataFrame(data = data)
    
    name = playlist_name + '.csv'
    path = get_path(playlist_name, name)
    dataframe.to_csv(path)
    
    return dataframe, playlist_name
