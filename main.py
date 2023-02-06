from spotify_extractor_scripts.create_dataframe import create_dataframe
from powerpoint_creator_scripts.create_powerpoint import create_powerpoint

def main():
    df, playlist_name = create_dataframe()
    create_powerpoint(df, playlist_name)

main()
