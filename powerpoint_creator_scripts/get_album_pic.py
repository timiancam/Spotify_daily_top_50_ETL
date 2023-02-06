import pandas
import collections.abc # put weird import comment here
import urllib.request
from ETL_path_manager_scripts.ETL_path_manager import get_path

def get_album_pic(playlist_name, idx, df):
    
    name = 'song' + str(idx + 1) + '.png'
    path = get_path(playlist_name, name, 'images')
    
    urllib.request.urlretrieve(df.iloc[idx]['album_image_URL'], path)
    
    return path
