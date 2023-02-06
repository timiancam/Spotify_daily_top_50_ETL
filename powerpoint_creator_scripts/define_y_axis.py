def define_y_axis(key):
    """
    defines the y-axis for the box plot
    different audio features possess different scales
    hence the box plot has to be adapated to fit
    """
    
    zero_to_one_keys = ['danceability', 
                        'energy', 
                        'speechiness', 
                        'acousticness', 
                        'liveness',
                        'valence']
    
    if key in zero_to_one_keys:
        y_lower = 0
        y_upper = 1
    elif key == 'instrumentalness':
        y_lower = None
        y_upper = None
    elif key == 'loudness':
        y_lower = -60
        y_upper = 0
        
    return y_lower, y_upper
