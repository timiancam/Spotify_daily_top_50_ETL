# future improvements
    # creating universal powerpoint object (google python quickstart or odpslides)

# imports
import powerpoint_creator as pc
import spotify_extractor as se

df, playlist_name = se.create_dataframe()
pc.create_powerpoint(df, playlist_name)