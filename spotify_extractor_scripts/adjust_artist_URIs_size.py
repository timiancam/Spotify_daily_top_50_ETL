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
