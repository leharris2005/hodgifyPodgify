
function populateSongs(obj) {
    const top5Songs = document.querySelector('.overlay-text-fivesongs');
    const text = document.createElement('p');
    text.textContent = `${obj.title} - ${obj.artists.join(' - ')}`;
    top5Songs.appendChild(text);
}

function populateArtists(obj) {
    const topArtists = document.querySelector('.overlay-text-topartists');
    const text = document.createElement('p');
    text.textContent = `${obj.name.name}\n`;
    topArtists.appendChild(text);
}

function populateRecentSongs(obj) {
    const recentlyPlayedSongs = document.querySelector('.overlay-text-past8songs');
    const text = document.createElement('p');
    text.textContent = `${obj.title} - ${obj.artists.join(' - ')}`;
    recentlyPlayedSongs.appendChild(text);
}

function populateGenre(obj) {
    const genres = document.querySelector('.overlay-text-genres');
    const text = document.createElement('p');
    text.textContent = `${obj.title}\n`;
    genres.appendChild(text);
}

fetch('spotify_data.json')
    .then(response => response.json())
    .then(data => {
        const topSongs = data.top_5_songs;
        topSongs.forEach(song => {
            console.log(`Title: ${song.title}`);
            console.log(`Artists: ${song.artists.join(', ')}`);
            console.log(`Album Art: ${song.album_art}`);
            populateSongs(song)
        });
        const topArtist = data.top_3_artists;
        topArtist.forEach(topArtist => {
            console.log(`Name: ${topArtist.name.name}`);
            console.log(`Art: ${topArtist.art}`);
            populateArtists(topArtist);
        });
        const topAlbum = top_3_album_covers;
        topAlbum.forEach(album => {
            console.log(`Name: ${album.name}`);
            console.log(`Art: ${album.art}`);
        });
        const recentSongs = recently_played_songs;
        recentSongs.forEach(song => {
            console.log(`Title: ${song.title}`);
            console.log(`Artists: ${song.artists.join(', ')}`);
            populateRecentSongs(song);
        })
        const recommendedSong = data.recommended_songs;
        recommendedSong.forEach(song => {
            console.log(`Title: ${song.name}`);
            console.log(`Artists: ${song.artists}`);
            console.log(`Album: ${song.album}`);
        });
        const recommendedArtist = data.recommended_artists;
        recommendedArtist.forEach(artist => {
            console.log(`Name: ${artist.name}`);
            console.log(`Art: ${artist.url}`);
        });
        const currentSong = data.current_song;
        currentSong.forEach(song => {
            console.log(`Title: ${song.title}`);
            console.log(`Artists: ${song.artists.join(', ')}`);
            console.log(`Album Art: ${song.album_art}`);
        });
        const topGenre = data.top_genres;
        topGenre.forEach(genre => {
            console.log('${genre}')
        })
    })
    .catch(error => console.error('Error loading JSON:', error));
