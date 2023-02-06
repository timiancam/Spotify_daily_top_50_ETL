import pandas
from powerpoint_creator_scripts.define_y_axis import define_y_axis
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns
import numpy as np
from ETL_path_manager_scripts.ETL_path_manager import get_path

def create_boxplot(audio_feature, key, playlist_name):
    """
    creates a box plot for the audio features and saves them in a subfolder
    returns a path for the ppt to reference so that the boxplot can be inserted
    """
    
    y_lower, y_upper = define_y_axis(key)
    
    # add comment about numbers
    plt.figure(figsize=(6.752,5.909))
    
    fig = sns.boxplot(data=audio_feature,
                      orient='v',
                      color='#1DB954', # spotify green 
                      width=0.5,
                      showmeans=True,
                      meanline=True,
                      meanprops={'color': 'black', 'linestyle': '-.'})
    
    fig.set(ylim=(y_lower,y_upper), xlim=(-0.5,0.5), xticklabels=[])
    
    mean_line_label = 'Mean = ' + str("%.2f" % np.mean(audio_feature))
    median_line_label = 'Median = ' + str("%.2f" % np.median(audio_feature))
    
    mean_line= mlines.Line2D([], [], label=mean_line_label, linestyle='-.' )
    median_line = mlines.Line2D([], [], label=median_line_label, linestyle='-') 
    fig.legend(handles=[mean_line, median_line])
    
    name = key + '_boxplot.png'
    path = get_path(playlist_name, name, 'plots')
    
    plt.savefig(path)
    plt.clf()
    
    return path
