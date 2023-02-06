from powerpoint_creator_scripts.get_top_five_genres import get_top_five_genres
from ETL_path_manager_scripts.ETL_path_manager import get_path
import pandas 
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns

def create_genre_countplot(df, playlist_name):
    """creates a countplot for the top 5 popular genres in a given playlist
    returns a path for the ppt to reference so that the countplot can be inserted
    """
    
    top_five_sorted_genres = get_top_five_genres(df)
    
    # add comment for numbers
    plt.figure(figsize=(11.492,4.381))
    sns.countplot(x=top_five_sorted_genres)
    
    name = 'genre_countplot.png'
    path = get_path(playlist_name, name, 'plots')
    
    plt.savefig(path)
    plt.clf() 
    
    return path
