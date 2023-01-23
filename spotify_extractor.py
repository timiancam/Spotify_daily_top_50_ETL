# imports
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from decouple import config
import json
import urllib.request
import ETL_path_manager as ETL_pm

def get_audio_features(track_URIs, sp):
    """
    retrieves audio features for a set of tracks in a playlist
    audio features are defined by Spotify
    API call returns a list of dictionaries where the keys are the audio features
    """
    
    audio_features = {}
    audio_features['danceability'] = []
    audio_features['energy'] = []
    audio_features['loudness'] = []
    audio_features['speechiness'] = []
    audio_features['acousticness'] = []
    audio_features['instrumentalness'] = []
    audio_features['liveness'] = []
    audio_features['valence'] = []
    
    # see spotipy documentation
    audio_features_object = sp.audio_features(track_URIs)
    
    for key in audio_features.keys():
        audio_features[key] = [d[key] for d in audio_features_object]
    
    return audio_features

def adjust_artist_URIs_size(artist_URIs):
    """
    Re-organizes a flat list into a list of lists
    sp.artists API call only accepts a maximum list size of 50
    function retrieves 50 artists (max) from the passed list
    and appends them to another list
    those 50 artists are then removed from the original list
    """
    
    temp_URIs = artist_URIs
    artist_URIs = []
        
    while temp_URIs:
        if len(temp_URIs) > 50:
            upper_limit = 50
        else:
            upper_limit = len(temp_URIs)
            
        artist_URIs.append(temp_URIs[0:upper_limit])
        
        for x in range(upper_limit):
            temp_URIs.pop(0)
        
    return artist_URIs
    
def remove_dupes_and_flatten(messy_list):
    flat_list = [item for sublist in messy_list for item in sublist]
    
    return list(dict.fromkeys(flat_list)) 

def get_artist_genres(artist_URIs, sp):   
    """
    retrieves the genres for a given artist in a given playlist
    one artist can appear more than once in a playlist and must be removed
    the API call only accepts a maximum list size of 50
    so the artist_list is adjusted
    a dictionary is created where the keys are artist URIs
    and the values are a list of genres relevant for a given artist
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

def extract_URI(artist):
    return artist['uri'].split(':')[-1]

def get_main_track_info(playlist_tracks):
    """
    retrives the main track information for a given set of tracks in a playlist
    this is the information directly accessible from the API call sp.playlist_tracks
    which returns a list of dictionaries
    """
    
    main_track_info = {}
    main_track_info['track_URIs'] = []
    main_track_info['track_names'] = []
    main_track_info['track_albums'] = []
    main_track_info['track_album_URLs'] = []
    main_track_info['artist_URIs'] = []
    main_track_info['track_artists'] = []
    
    for track_object in playlist_tracks:
        track = track_object['track']
        
        main_track_info['track_URIs'].append(track['id'])
        main_track_info['track_names'].append(track['name'])
        main_track_info['track_albums'].append(track['album']['name'])
        main_track_info['track_album_URLs'].append(track['album']['images'][0]['url'])
        
        # artist in track['artists'] returns 'spotify:artist:7tYKF4w9nC0nq9CsPZTHyP'
        # URI is after the last ':'
        # list comprehension necessary as one song can have multiple artists
        artist_URIs = [extract_URI(artist) for artist in track['artists']]
        main_track_info['artist_URIs'].append(artist_URIs)
        
        artists = [artist['name'] for artist in track['artists']]
        main_track_info['track_artists'].append(artists)
    
    return main_track_info

def sort_artist_genres(artist_genres, artist_URIs):
    """
    the indexing of artist genres is not consistent with the indexing of the playlist
    this function sorts the genres so that the subsequent dataframe can be properly defined
    the correct indexing comes from the passed arguemnt artist_URIs
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

def get_playlist_URI(sp):
    """
    gets a country input from the user
    function then checks if it is a valid entry
    and then retrieves the relevant uri for 'Daily Top 50 - Country'
    this uri is then used to retrieve all the playlist information
    """
    
    supported_countries = json.loads(config('SUPPORTED_COUNTRIES'))
    
    print('List of supported countries: ' + str(supported_countries))
    print('Or type exit')

    while True:
        search_term = input('Which country would you like the Spotify Daily Top 50 for? ')
    
        if search_term.lower() in supported_countries:
            country = 'Daily Top 50 - ' + search_term.capitalize()
            playlist_URI = sp.search(country, type='playlist', limit=1)['playlists']['items'][0]['id']
            break
        elif search_term.lower() == 'exit':
            quit()
        else:
            print('That is not a supported option. Why not try Peru or Singapore! Or type exit.')
    
    return playlist_URI

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
    ETL_pm.make_subfolders(playlist_name)
    
    playlist_image_URL = playlist['images'][0]['url']
    save_playlist_image(playlist_image_URL, playlist_name)
    
    return playlist_tracks, playlist_name, sp

def save_playlist_image(playlist_image_URL, playlist_name):

    name = 'playlist_image.png'
    path = ETL_pm.get_path(playlist_name, name, 'images')
    urllib.request.urlretrieve(playlist_image_URL, path)

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

def create_dataframe():
    """
    creates a dataframe which is then written to a .csv file
    first retrieves all information for a given playlist
    """
    
    main_track_info, audio_features, artist_genres, playlist_name = get_playlist_info()
    
    d = {
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
    
    dataframe = pd.DataFrame(data = d)
    
    name = playlist_name + '.csv'
    path = ETL_pm.get_path(playlist_name, name)
    dataframe.to_csv(path)
    
    return dataframe, playlist_name

