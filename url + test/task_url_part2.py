#link: https://api.vk.com/method/users.get?user_ids=100,777,dm,skorking&v=5.8&fields=nickname,sex,status,education,online,last_seen

import urllib.request,json, pprint
import requests

def url_constractor(*args):
    html = 'https://api.vk.com/method/users.get?user_ids='
    for item in args:
        html += str(item) + ','
    html = html[0:-1]
    html += '&v=5.8&fields=nickname,sex,status,education,online,last_seen'
    return html

def main():
    ids = [100,777,'dm','skorking']
    try:
      html = urllib.request.urlopen(url_constractor(*ids)).read()
    except requests.exceptions.HTTPError as e:
        print('>>{}!'.format(e)) #~
    except requests.exceptions.ConnectionError as e:
        print('>>{}!'.format(e)) #~
    else:
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

main()