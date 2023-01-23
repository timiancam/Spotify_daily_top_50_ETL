# imports 
import pathlib
import os

# global variables
ROOT_PATH = pathlib.Path(__file__).resolve().parent

def get_path(playlist_name, name, subfolder=None):
    
    if subfolder == None:
        path = pathlib.PurePath.joinpath(ROOT_PATH, 'output', playlist_name, name)
    else:
        path = pathlib.PurePath.joinpath(ROOT_PATH, 'output', playlist_name, subfolder, name)
    
    # the pptx module object methods only accepts string paths
    path = path.as_posix()
    
    return path

def make_subfolders(playlist_name):
    
    # output folder
    try:
        path = pathlib.PurePath.joinpath(ROOT_PATH, 'output')
        os.mkdir(path)
    except FileExistsError:
        None
        
    # playlist folder
    path = pathlib.PurePath.joinpath(ROOT_PATH, 'output', playlist_name)
    os.mkdir(path)
    
    # plots subfolder
    path = pathlib.PurePath.joinpath(ROOT_PATH, 'output', playlist_name, 'plots')
    os.mkdir(path)
    
    # images subfolder
    path = pathlib.PurePath.joinpath(ROOT_PATH, 'output', playlist_name, 'images')
    os.mkdir(path)

def get_presentation_template():
    return pathlib.PurePath.joinpath(ROOT_PATH, 'template', 'spotify_template.pptx').as_posix()