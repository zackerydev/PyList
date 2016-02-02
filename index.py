from gmusicapi import Mobileclient

api = Mobileclient()
logged_in = api.login('zgriesinger@gmail.com', '3AltuLSQzzr5', Mobileclient.FROM_MAC_ADDRESS)

print(logged_in)

desperado = api.search_all_access("Desperado - The Eagles", 3)
print(desperado['song_hits'])
for i in desperado['song_hits']:
    print(i['track']['title'])
    print(i['track']['artist'])
    print(i['track']['album'])
    print(i['track']['storeId'])
