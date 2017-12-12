#link: https://api.vk.com/method/users.get?user_ids=100,777,dm,skorking&v=5.8&fields=nickname,sex,status,education,online,last_seen

import urllib.request
import json, pprint

html = urllib.request.urlopen("http://bit.ly/2AvZeGj").read()
data = json.loads(html)
s = data.get('response')
#pprint.pprint(s)

print(' ' + '-*-*'*12 + '\n')
for user in s:
    print(" First name: " + str(user['first_name']))
    print(" Last name: " + str(user['last_name']))
    print(" Nickname: " + str(user['nickname']))
    print(" Status: " + str(user['status']))
    print(" Online: " + str(user['online']))
    print(" Sex: " + str(user['sex']))
    print(" Last_seen: " + str(user['last_seen'])+ '\n')
    print(' ' + '-*-*'*12 + '\n')
