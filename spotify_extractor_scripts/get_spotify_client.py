import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from decouple import config

def get_spotify_client():
    """
    creates an authenticator for API calls to Spotify Databse
    clientID and secret are stored within the .env file
    """
    
    cid = config('CLIENT_ID')
    secret = config('SECRET')
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    return sp
