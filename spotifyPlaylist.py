import spotipy
from spotipy.oauth2 import SpotifyOAuth

username = "Gustavo Santos"
playlist_id = "5pvyrypxnV2YgpoKLCIb8l"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4979aad062c7482a80db275680e1b5ec",
                                               client_secret="3bfbf96ec5ae4e419f773fe1dff91ffe",
                                               redirect_uri="http://localhost:8080/callback",
                                               scope="playlist-modify-public"))

artistasFile =  open("artistas.txt", 'r')
artista = [x.strip('\n') for x in artistasFile.readlines()]

numeroArtistas = len(artista)
tracks = []

QuantMusSTR = input("Quantas músicas você quer por artista em sua playlist? ")
QuantMus = int(QuantMusSTR)

for x in range(0, numeroArtistas):
    result = sp.search(artista[x], limit=QuantMus)
    for i, t in enumerate(result['tracks']['items']):
        tracks.append(str(t['id'].strip( 'u' )))
        print("Adicionando a track", t['id'], t['name'])
while tracks:
    try:
       result = sp.user_playlist_add_tracks(username,playlist_id, tracks[:1])
    except:
        print("Erro")
    tracks = tracks[1:]
