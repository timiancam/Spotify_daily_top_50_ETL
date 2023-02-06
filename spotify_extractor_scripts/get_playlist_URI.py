import spotipy

def get_playlist_URI(sp):
    """
    gets a country input from the user
    function then checks if it is a valid entry
    and then retrieves the relevant uri for 'Daily Top 50 - Country'
    this URI is then used to retrieve all the playlist information
    """
    
    supported_countries = ["global", "argentina", "australia", "austria", "belgium", "bolivia", "brazil", "bulgaria", "canada", "chile", "colombia", "costa rica", "czech republic", "denmark", "dominican republic", "ecuador", "egypt", "el salvador", "estonia", "finland", "france", "germany", "greece", "guatemala", "honduras", "hong kong", "hungary", "iceland", "india", "indonesia", "ireland", "israel", "italy", "japan", "latvia", "lithuania", "luxembourg", "malaysia", "mexico", "netherlands", "new zealand", "nicaragua", "norway", "pakistan", "panama", "paraguay", "peru", "philippines", "poland", "portugal", "romania", "saudi arabia", "singapore", "slovakia", "south africa", "south korea", "spain", "sweden", "switzerland", "taiwan", "thailand", "turkey", "uae", "usa", "ukraine", "united kingdom", "uruguay", "vietnam"]
    
    print('List of supported countries: ' + str(supported_countries))
    print('Or type exit.')

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
