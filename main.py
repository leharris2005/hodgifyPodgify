import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
from collections import Counter
import json

scope = None
currentTopArtistsList = []
currentTopSongsList = []

recently_played_songs = []
top_5_songs = []
top_3_album_covers = []
top_3_artists = []
recommended_songs = []
recommended_artists = []
artistList = []

def get_recently_played_songs():
    scope = 'user-read-recently-played'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))

    results = sp.current_user_recently_played(limit=50)
    songs = results['items']
    
    if not songs:
        print("No recently played songs found.")
        return
    
    i = 1
    print("\nYour recently played songs:")
    for item in songs:
        track = item['track']
        currentTopArtistsList.append(artist['id'] for artist in track['artists'])
        currentTopSongsList.append(track['id'])
        if (i<9) :
            print(f"{track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
            song_info = {
            'title': track['name'],
            'artists': [artist['name'] for artist in track['artists']],
            'album_art': track['album']['images'][0]['url'] if track['album']['images'] else None
            }   
            recently_played_songs.append(song_info)
        i = i+1
    print('\n')
    return recently_played_songs

def get_top_5_songs():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))

    results = sp.current_user_top_tracks(time_range='short_term', limit=50)  

    print("Your most listened to songs over the past four weeks:")
    i = 1
    for idx, item in enumerate(results['items']):
        currentTopSongsList.append(item['id'])
        currentTopArtistsList.append(artist['id'] for artist in item['artists'])
        track_name = item['name']
        artists = ", ".join(artist['name'] for artist in item['artists'])
        if (i<6):
            print(f"{idx + 1}: {track_name} by {artists}")
            song_info = {
            'title': track_name,
            'artists': [artist['name'] for artist in item['artists']],
            'album_art': item['album']['images'][0]['url'] if item['album']['images'] else None
            }   
            top_5_songs.append(song_info)
        i = i+1
    print("\n")
    return top_5_songs

def get_top_3_album_covers():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                                   client_secret=config.CLIENT_SECRET,
                                                   redirect_uri=config.REDIRECT_URI,
                                                   scope=scope))

    results = sp.current_user_top_tracks(time_range='short_term', limit=50)
    album_counter = Counter()
    album_details = {}
    top_3_albums_info = []

    for item in results['items']:
        album = item['album']
        album_id = album['id']
    
        album_counter[album_id] += 1

        if album_id not in album_details:
            album_details[album_id] = {
                'name': album['name'],
                'artists': ", ".join(artist['name'] for artist in album['artists']),
                'image': album['images'][0]['url'] if album.get('images') and album['images'] else None
            }
            currentTopArtistsList.append(album_id)

    top_3_albums = album_counter.most_common(3)

    print("Top 3 Albums over the past 4 weeks:")
    for idx, (album_id, count) in enumerate(top_3_albums, start=1):
        album = album_details[album_id]
        print(f"{idx}: {album['name']} by {album['artists']}")


        album_info = {
            'title': album['name'],
            'artists': album['artists'],
            'album_art': album['image']
        }
        top_3_albums_info.append(album_info)

    print("\n")
    return top_3_albums_info

top_albums = get_top_3_album_covers()


def get_top_3_artists():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    results = sp.current_user_top_artists(time_range='short_term', limit=50)
    top_artists = []

    for item in results['items']:
        artist_name = item['name']
        currentTopArtistsList.append([item['id']])
        top_artists.append(item)
    print("\nTop 3 artists over the last 4 weeks:")
    i = 1
    for idx, artist in enumerate(top_artists, start=1):
        if (i < 4): 
            print(f"{idx}: {artist['name']}")
            artist_info = {
            'name': artist,
            'art': artist['images'][0]['url'] if artist['images'] else None
            }   
            top_3_artists.append(artist_info)
            artistList.append(artist)
        i = i+1
    print("\n")
    return top_3_artists
# def get_top_10_genres():
    # spotipy does not have an explicit method to do this

# def get_time_spent_listening():
    # spotipy does not have an explicit method to do this

def recommend_songs():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    
    top_tracks_results = sp.current_user_top_tracks(time_range='short_term', limit=5)


    track_ids = [track['id'] for track in top_tracks_results['items']]


    recommendations = sp.recommendations(seed_tracks=track_ids, limit=3)

    recommended_tracks = []

    for track in recommendations['tracks']:
        if track not in currentTopSongsList:
            track_info = {
                'name': track['name'],
                'artist': ", ".join(artist['name'] for artist in track['artists']),
                'album': track['album']['name'],
                'url': track['external_urls']['spotify']  # Link to the track
            }
            recommended_tracks.append(track_info)
    
    print("Recommended Songs based on your listening habits:")
    for idx, song in enumerate(recommended_tracks, start=1):
        print(f"{idx}: {song['name']} by {song['artist']}")
    print("\n")
    return recommended_tracks

def recommend_artists():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    top_artists_results = sp.current_user_top_artists(time_range='short_term', limit=5)
    
    artist_ids = [artist['id'] for artist in top_artists_results['items']]

    recommendations = sp.recommendations(seed_artists=artist_ids, limit=3)

    recommended_artists = {}
    for track in recommendations['tracks']:
        for artist in track['artists']:
            artist_id = artist['id']
            if artist_id not in recommended_artists:
                if artist_id not in currentTopArtistsList:
                    recommended_artists[artist_id] = {
                        'name': artist['name'],
                        'url': artist['external_urls']['spotify']
                    }
            if len(recommended_artists) >= 5:
                break

    print("Recommended Artists based on your listening habits:")
    for idx, artist in enumerate(list(recommended_artists.values()), start=1):
        print(f"{idx}: {artist['name']}")
    print("\n")
    return recommended_artists

def songPlayingNow():
    scope = 'user-read-currently-playing'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    current_track = sp.currently_playing()
    if current_track is not None and current_track['is_playing']:
        track = current_track['item']
        artist_name = track['artists'][0]['name']
        track_name = track['name']
        track_info = {
            'title': track_name,
            'artists': artist_name,
            'album_art': track['album']['images'][0]['url'] if track['album']['images'] else None
            }
    else:
        current_track = sp.track('https://open.spotify.com/track/3nc8QB8LOEZOb5H1nMdyzg?si=692ca370223849f5')
        artist_name = current_track['artists'][0]['name']
        track_name = current_track['name']
        track_info = {
            'title': track_name,
            'artists': artist_name,
            'album_art': current_track['album']['images'][0]['url'] if current_track['album']['images'] else None
            }
    
    print(f"Currently playing: {track_name} by {artist_name}")
    return track_info

def get_top_genres():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    results = sp.current_user_top_artists(limit=20, time_range="short_term")
    
    genre_counter = Counter()

    for artist in results['items']:
        genres = artist['genres']
        genre_counter.update(genres)  # Update the counter with artist genres

    # Get the most common genres
    most_common_genres = genre_counter.most_common()

    # Print the top genres
    print("Your top genres over the past four weeks:")
    for idx, (genre, count) in enumerate(most_common_genres[:10], start=1):  # Limit to top 10 genres
        print(f"{idx}: {genre} (played {count} times)")

    return most_common_genres[:9]


def save_data_to_json():
    data = {
        'recently_played_songs': recently_played_songs,
        'top_5_songs': top_5_songs,
        'top_3_album_covers': top_3_album_covers,
        'top_3_artists': top_3_artists,
        'recommended_songs': recommended_songs,
        'recommended_artists': recommended_artists,
        'current_song' : current_song,
        'top_genres' : top_genres
    }
    with open('spotify_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

recently_played_songs = get_recently_played_songs()
top_5_songs = get_top_5_songs()
top_3_album_covers = get_top_3_artists()
recommended_songs = recommend_songs()
recommended_artists = recommend_artists()
current_song = songPlayingNow()
top_genres = get_top_genres()

save_data_to_json()
