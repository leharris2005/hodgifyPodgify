fetch('spotify_data.json')
    .then(response => response.json())
    .then(data => {
        const recentSongs = data.recently_played_songs;
        recentSongs.forEach(song => {
            console.log(`Title: ${song.title}`);
            console.log(`Artists: ${song.artists.join(', ')}`);
            console.log(`Album Art: ${song.album_art}`);
        });
        const topSongs = data.top_5_songs;
        topSongs.forEach(song => {
            console.log(`Title: ${song.title}`);
            console.log(`Artists: ${song.artists.join(', ')}`);
            console.log(`Album Art: ${song.album_art}`);
        });
        const topAlbums = data.top_3_album_covers;
        topAlbums.forEach(album => {
            console.log(`Name: ${album.name}`);
            console.log(`Art: ${album.art}`);
        });
        const topArtist = data.top_3_artists;
        topAlbums.forEach(topArtist => {
            console.log(`Name: ${topArtist.name}`);
            console.log(`Art: ${topArtist.art}`);
        });
        const recommendedSong = data.recommended_songs;
        recommendedSong.forEach(song => {
            console.log(`Title: ${song.title}`);
            console.log(`Artists: ${song.artists.join(', ')}`);
            console.log(`Album Art: ${song.album_art}`);
        });
        const recommendedArtist = data.recommended_artists;
        recommendedArtist.forEach(artist => {
            console.log(`Name: ${artist.name}`);
            console.log(`Art: ${artist.art}`);
        });
    })
    .catch(error => console.error('Error loading JSON:', error));
