import spotipy as sp
import pandas

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
    
    for key in audio_features:
        audio_features[key] = [d[key] for d in audio_features_object]
    
    return audio_features
