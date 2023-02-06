def remove_dupes_and_flatten(messy_list):
    # https://stackoverflow.com/a/952952
    flat_list = [item for sublist in messy_list for item in sublist]
    
    return list(dict.fromkeys(flat_list)) 
