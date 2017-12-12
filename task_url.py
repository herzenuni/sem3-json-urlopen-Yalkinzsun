import urllib.request
import json, pprint

html = urllib.request.urlopen("https://api.vk.com/method/users.get?user_ids=100,777,123321,12021&v=5.8&fields=status,%20education,%20last_seen").read()
data = json.loads(html)
s = data.get('response')
#pprint.pprint(s)
for user in data:
    print(" Status: " + str(user['status']))
    print(" Education: " + str(user['education']))
    print(" Last_seen: " + str(user['last_seen'])+ '\n')
    print(' ' + '-*-*'*16 + '\n')
