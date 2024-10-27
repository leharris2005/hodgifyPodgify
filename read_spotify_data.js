
function populateSongs(obj) {
    const top5Songs = document.querySelector('.overlay-text-fivesongs');
    const text = document.createElement('p');
    text.textContent = `Title: ${obj.title}\nArtists: ${obj.artists.join(', ')}\nAlbum Art: ${obj.album_art}`;
    top5Songs.appendChild(text);
}

function populateArtists(obj) {
    const topArtists = document.querySelector('.overlay-text-topartists');
    const text = document.createElement('p');
    text.textContent = `Name: ${obj.name.name}\nArt: ${obj.art}`;
    topArtists.appendChild(text);
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
    })
    .catch(error => console.error('Error loading JSON:', error));
