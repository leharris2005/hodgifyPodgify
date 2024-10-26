import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
from datetime import datetime, timedelta

scope = None
currentTopArtistsList = []
currentTopSongsList = []

def get_recently_played_songs():
    scope = 'user-read-recently-played'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))

    results = sp.current_user_recently_played(limit=10)
    songs = results['items']
    
    if not songs:
        print("No recently played songs found.")
        return
    
    print("\nYour recently played songs:")
    for item in songs:
        track = item['track']
        currentTopArtistsList.append([artist['id'] for artist in track['artists']])
        currentTopSongsList.append(track)
        print(f"{track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

    print('\n')

def get_top_5_songs():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))

    results = sp.current_user_top_tracks(time_range='short_term', limit=5)  

    print("Your most listened to songs over the past four weeks:")
    for idx, item in enumerate(results['items']):
        currentTopSongsList.append(item)
        currentTopArtistsList.append([artist['id'] for artist in item['artists']])
        track_name = item['name']
        artists = ", ".join(artist['name'] for artist in item['artists'])
        print(f"{idx + 1}: {track_name} by {artists}")

# def get_top_3_album_covers():
    # spotipy does not have an explicit method to do this

def get_top_3_artists():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    results = sp.current_user_top_artists(time_range='short_term', limit=3)
    top_artists = []

    for item in results['items']:
        artist_name = item['name']
        currentTopArtistsList.append([item['id']])
        top_artists.append(artist_name)
    print("\nTop 3 artists over the last 4 weeks:")
    for idx, artist in enumerate(top_artists, start=1):
        print(f"{idx}: {artist}")

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


    recommendations = sp.recommendations(seed_tracks=track_ids, limit=5)

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
        print(f"{idx}: {song['name']} by {song['artist']} (Album: {song['album']}) - {song['url']}")

def recommend_artists():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri=config.REDIRECT_URI,
                                               scope=scope))
    top_artists_results = sp.current_user_top_artists(time_range='short_term', limit=5)
    
    artist_ids = [artist['id'] for artist in top_artists_results['items']]

    recommendations = sp.recommendations(seed_artists=artist_ids, limit=20)  # Fetch a larger set for variety

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
        print(f"{idx}: {artist['name']} - {artist['url']}")


get_recently_played_songs()
get_top_5_songs()
get_top_3_artists()
recommend_songs()
recommend_artists()
