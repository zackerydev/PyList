# shows a user's playlists (need to be authenticated via oauth)
# MY USER 1240630908
# -*- coding: utf-8 -*-
import sys
import os
import spotipy
import spotipy.util as util
import io

def show_tracks(results):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))
        output_song = track['name'] + ' - ' + track['artists'][0]['name'] + '\n'
        output_song_final = unicode(output_song)
        type(output_song_final)
        output_file.write(output_song_final)


if __name__ == '__main__':
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
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                output_playlist_name = 'P: ' + str(playlist['name']) + '\n'
                output_playlist_name_utf = unicode(output_playlist_name)
                output_file.write(output_playlist_name_utf)
                print('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)
