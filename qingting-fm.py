# -*- coding: utf-8 -*-
# @Author  : laowei
# @Time    : 2022/6/14 下午5:10

import hmac
import time
import requests as res
import pyaria2

rpc = pyaria2.Aria2RPC()

logo = '''

        _                _    _                  ___           
  __ _ (_) _ __    __ _ | |_ (_) _ __    __ _   / __\_ __ ___  
 / _` || || '_ \  / _` || __|| || '_ \  / _` | / _\ | '_ ` _ \ 
| (_| || || | | || (_| || |_ | || | | || (_| |/ /   | | | | | |
 \__, ||_||_| |_| \__, | \__||_||_| |_| \__, |\/    |_| |_| |_|
    |_|           |___/                 |___/                  
                                                by laowei
'''

cookie = open('cookie.txt', 'r').read()

h = {

    'Cookie': cookie,

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',

}


def sign(s):
    key = b'fpMn12&38f_2e'
    signature = hmac.new(key, s.encode(), digestmod='MD5').hexdigest()
    return signature


def download(title, url):
    pro = {
        'out': 'qingting/' + title + '.m4a'

    }
    rpc.addUri([url], pro)


def getm4a(title, uid, item_id):
    ts = int(time.time() * 1000)
    sign_data = f'/audiostream/redirect/{uid}/{item_id}?access_token=&device_id=MOBILESITE&qingting_id=&t={ts}'
    sig = sign(sign_data)
    url = f'https://audio.qtfm.cn/audiostream/redirect/{uid}/{item_id}?access_token=&device_id=MOBILESITE&qingting_id=&t={ts}&sign={sig}'
    s = res.get(url, allow_redirects=False, headers=h).headers['Location']

    download(title, s)


def get_list(name, uid, vid):
    lex = 100
    page = 1
    while lex == 100:
        url = f'https://i.qingting.fm/capi/channel/{uid}/programs/{vid}?curpage={page}&pagesize=100&order=asc'
        s = res.get(url, headers=h).json()['data']['programs']

        lex = len(s)
        for i in s:
            title = i['title']
            item_id = i['id']
            getm4a(name + '/' + title, uid, item_id)
            print(title)
        page += 1


def getuser(channel_id):
    url = f'https://i.qingting.fm/capi/v3/channel/{channel_id}'
    s = res.get(url, headers=h).json()['data']

    title = s['title']
    vid = s['v']
    get_list(title, channel_id, vid)


def main():
    print(logo)
    channel_id = input('输入专辑代码\n')
    getuser(channel_id)


if __name__ == '__main__':
    # 402683
    main()
