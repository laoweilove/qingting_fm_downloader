import requests as res
import json
import yaml
url = 'https://user.qingting.fm/u2/api/v4/user/login'
h = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
}

user_id = input('手机号')
password = input('密码')


d = {"account_type":"5","device_id":"web","user_id":user_id,"password":password,"area_code":"+86"}
s = res.post(url, json.dumps(d), headers=h)
data = s.json()['data']
qingting_id = data['qingting_id']
access_token = data['access_token']
cookie = s.headers['Set-Cookie'].replace('path=/,', '').replace('path=/', '')
w=open('config.yaml','w')
data = {
    'cookie': cookie,
    'access_token': access_token,
    'qingting_id': qingting_id,
}
yaml.dump(data,w)