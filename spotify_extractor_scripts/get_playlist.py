import spotipy
import pandas
from ETL_path_manager_scripts.ETL_path_manager import make_subfolders
from spotify_extractor_scripts.get_spotify_client import get_spotify_client
from spotify_extractor_scripts.get_playlist_URI import get_playlist_URI
from spotify_extractor_scripts.save_playlist_image import save_playlist_image

def get_playlist():
    """
    retrieves the user's desired Daily Top 50 - Country playlist
    then retrieves all the tracks in that playlist along with any misc information
    including playlist image
    the function also creates all the subfolders where subsequent ppts, csvs, images and plots will be saved to
    """
    
    sp = get_spotify_client()
    
    playlist_URI = get_playlist_URI(sp)
    
    # playlist_tracks contains information stored within lists/dictionaries of lists/dictionaries
    playlist_tracks = sp.playlist_tracks(playlist_URI)['items']
    playlist = sp.playlist(playlist_URI)
    
    playlist_name = 'Daily ' + playlist['name']
    make_subfolders(playlist_name)
    
    playlist_image_URL = playlist['images'][0]['url']
    save_playlist_image(playlist_image_URL, playlist_name)
    
    return playlist_tracks, playlist_name, sp
