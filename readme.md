# Spotify Extract Transform Load

The script produces a Microsoft PowerPoint, .csv, plots, images and subfolders for a Spotify Daily - Top 50 "Country" playlist in the directory the script is ran from.

You can also review the `example_subfolder` if you do not wish to run the script or do not have Microsoft PowerPoint installed.

It is recommended to run this script within a Python virtual environment.

## Usage Instructions

1. Clone this repository from GitHub.
2. Ensure your terminal is in the same directory as the `main.py` script.
3. In your terminal, run `pip install -r requirements.txt`. This will install the required packages for this script.
4. Check you have setup your authenication tokens, see below.
5. In your terminal, run `python main.py`.
6. Input a valid country option (displayed when the script is running).
7. Navigate to the `output` subfolder to review the produced presentation and .csv.
8. Thank you for trying my program!

## Spotify API Calls

The script makes API calls to the Spotify database, and hence authentication tokens are required.

Authentication tokens can be retrieved from making an account on <https://developer.spotify.com/dashboard/>.

1. Create an account using the above URL.
2. Login to the Spotify developer dashboard.
3. "CREATE AN APP".
4. Note down the client ID.
5. Click "SHOW CLIENT SECRET" and note the client secret.
6. Open the `.env` file (may be hidden) and input the client ID and secret.
7. Save and close the `.env` file.

## To Do

- For ppt_creator, add comment for the weird import.
- Optimise functions, one responsibility per function.
- Add error handling for Spotify API calls.
- Pull user input function out of spotify_extractor scripts.
- Update ETL 'get_path' function name to 'create_path'.
- Update argument names for 'get path': folder_name, subfolder_name, filename.
- Simple function names (E.g. get_main_track_info --> get_track_info).
- Avoid using the same variable name (E.g. name = name.upper()).
- For getting artist genres, investigate pointer based approach instead of of sublists.
- Make get_audio_features() tidier, no need to use list.keys() for example.
- create_dataframe() should only return a dataframe, granulize the function.
- For ppt_creator, investigate 'closures' instead of global variables.
    - Implement playlist_name variable into this scope.
- Fix the 'magic numbers', add comment for why these values.
- Clear plots at the beginning, not the end, plt.clf().
- Start using string interpolation (E.g. get_album_pic()).
- Functions that return a path instead of an image, use a clearer variable name (E.g. plot_path or img_path).
- Investigate universal powerpoint object - see python quickstart or odpslides.
- Research the proper way to package scripts.
- Fix encoding problems from non-english characters.
- List comprehension for get_main_track_info() for each key instead of iterating over the playlist_tracks?
