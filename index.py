from gmusicapi import Mobileclient

api = Mobileclient()
logged_in = api.login('zgriesinger@gmail.com', '3AltuLSQzzr5', Mobileclient.FROM_MAC_ADDRESS)

print(logged_in)
## Take a file with song names - artists and Playlists names beginning with P:
def parse_file(filename):
    """INPUT: Expects a file with Playlist lines start P: and songs formatted song title - artist
    OUTPUT: outputs a list of lists containing the playlist name then a two item list of song and artist"""
    input_file = open(filename).readlines()
    playlists_and_songs = []
    playlist_temp = []
    for i in input_file:
        if i[0:2] == 'P:' or i == 'end\n':
            playlists_and_songs.append(playlist_temp)
            playlist_temp = []
            i.strip('P: ')
            playlist_temp.append(i.strip("\n"))
        else:
            i = i.strip("\n")
            song_artist = i.split(" - "),
            playlist_temp.append(song_artist)
    playlists_and_songs.remove([])
    return playlists_and_songs


all_playlists = parse_file("playlists.txt")
for i in all_playlists:
    print i
    for j in i:
        if j[0:2] == "P:":
            print "Creating playlist: " + j[3:]
            current_playlist = api.create_playlist(j[3:])
        else:
            current_song = j[0][0] + " " + j[0][1]

            search_current_song = api.search_all_access(current_song, 1)
            if search_current_song['song_hits'] == []:
                print "No results found for " + current_song
                continue
            current_song_id = search_current_song['song_hits'][0]['track']['storeId']

            print current_song_id
            api.add_songs_to_playlist(current_playlist, current_song_id)

##desperado = api.search_all_access("Desperado - The Eagles", 1)
##print(desperado['song_hits'])
##for i in desperado['song_hits']:
    ##song_ids = [i['track']['storeId']]

##playlist = api.create_playlist("GMUSIC API TEST", public=True)
##api.add_songs_to_playlist(playlist, song_ids)
