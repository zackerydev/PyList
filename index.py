from gmusicapi import Mobileclient

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'].encode('ascii', 'ignore'), track['name'].encode('ascii', 'ignore')))
        output_song = track['name'] + ' - ' + track['artists'][0]['name'] + '\n'
        output_song_final = unicode(output_song)
        type(output_song_final)
        output_file.write(output_song_final)

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
if __name__ == '__main__':
    spotify_username = ""
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username,
    client_id='58c7b9bd2da44f2182ca097b970e56af',
    client_secret='cda48ec16700468ab184975dcbeb3487',
    redirect_uri='https://google.com')

    output_file = io.open('playlists.txt', 'w', encoding='utf8')


    if token:
        top = 40
        sp = spotipy.Spotify(auth=token)
        spotify_playlists = sp.user_playlists(username)
        for spotify_playlist in spotify_playlists['items']:
            if spotify_playlist['owner']['id'] == username:
                print()
                print(spotify_playlist['name'].encode('ascii', 'ignore'))
                output_playlist_name = 'P: ' + str(spotify_playlist['name'].encode('ascii', 'ignore')) + '\n'
                output_playlist_name_utf = unicode(output_playlist_name)
                output_file.write(output_playlist_name_utf)
                print('  total tracks', spotify_playlist['tracks']['total'])
                results = sp.user_playlist(username, spotify_playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)

    api = Mobileclient()
    username = str(raw_input("Please enter your Google E-Mail:  (No '@gmail.com' needed)"))
    password = raw_input("Please enter your Google Password: ")
    username = username + "@gmail.com"
    print username
    logged_in = api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)
    if logged_in == True:
        print("Succesfully logged into Google!")
    ## Take a file with song names - artists and Playlists names beginning with P:



    all_playlists = parse_file("playlists.txt")
    missing_songs = []
    for i in all_playlists:
        for j in i:
            if j[0:2] == "P:":
                current_playlist_name = j[3:]
                print("Creating playlist: " + j[3:])
                #current_playlist = api.create_playlist(j[3:]) #COMMENT OUT THIS LINE TO PREVENT PLAYLIST CREATION
            else:
                current_song = j[0][0] + " " + j[0][1]

                search_current_song = api.search_all_access(current_song, 1)
                if search_current_song['song_hits'] == []:
                    print("No results found for " + current_song)
                    missing_songs.append([current_song, current_playlist_name])

                    continue
                current_song_id = search_current_song['song_hits'][0]['track']['storeId']
                print("Adding " + current_song + " to playlist " + current_playlist_name )
                #api.add_songs_to_playlist(current_playlist, current_song_id) #COMMENT OUT THIS LINE TO PREVENT PLAYLIST CREATION
    for i in missing_songs:
        print("Could not find " + i[0] + " for playlist " + i[1])

    ##desperado = api.search_all_access("Desperado - The Eagles", 1)
    ##print(desperado['song_hits'])
    ##for i in desperado['song_hits']:
        ##song_ids = [i['track']['storeId']]

    ##playlist = api.create_playlist("GMUSIC API TEST", public=True)
    ##api.add_songs_to_playlist(playlist, song_ids)
