import urllib.request
from ETL_path_manager_scripts.ETL_path_manager import get_path

def save_playlist_image(playlist_image_URL, playlist_name):

    name = 'playlist_image.png'
    path = get_path(playlist_name, name, 'images')
    urllib.request.urlretrieve(playlist_image_URL, path)
