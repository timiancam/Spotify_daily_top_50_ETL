from spotify_extractor_scripts.extract_URI import extract_URI

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
