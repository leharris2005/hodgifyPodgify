# Hodgify Podgify
https://leharris2005.github.io/hodgifyPodgify/index.html

Website that shows your spotify statistics. Uses python and HTML.
- 4 week recap collage
    - top songs
    - top artists
    - top genres
    - currently playing
- Bucket list
    - recommends new songs (reccomendations) and artists (related artists) based on user listening
- to do list
-   8 most recently played songs with checkmarks

## APIs Used
Used the Spotipy API, a Python wrapper for Spotify's Web API, to gather user's spotify data, such as their top played songs, favorite artists, and recommended artists and songs generated from Spotify's algorithm.

## Framework
Backend used Python to generate user Spotify data with the Spotipy API, then writing it into JSON format. Javascript is then used to parse through the JSON to put the user's data onto their dedicated spaces on the website. Standard HTML and CSS is used for front-end design, with background images hand-drawn by the lovely Emerson!

## Unfinished Features
By the end of the Hello World 2024 hackathon, our project has not completed adding the bucket list page data, or synced the spotify data to the current user (right now it takes data from Lauren's spotify data). We wish to continue adding such features in the near future.
