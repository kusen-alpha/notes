#  谷歌浏览器分析,主要利用md5加密

def get_md5(s):
    md5 = hashlib.md5()
    if isinstance(s, str):
        md5.update(s.encode('utf-8'))
    else:
        md5.update(s)
    return md5.hexdigest()


def get_salt(lts):
    return lts + str(random.randint(0, 10))


def get_lts():
    return str(int(time.time() * 1000))


def get_sign(word, salt):
    return get_md5('fanyideskweb' + word + salt + 'Tbh5E8=q6U3EXe+&L[4c@')


key = '你好啊'
lts = get_lts()
salt = get_salt(lts)
sign = get_sign(key, salt)
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'lts': lts,
    'bv': '9ff8102373b1562471f4b6881a5653e9',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=553198171@10.169.0.84; JSESSIONID=aaai05uZrLIgkdrviZbNx; OUTFOX_SEARCH_USER_ID_NCOO=770162901.3004788; ___rl__test__cookies=1622454096233',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
}
response = requests.post(url, headers=headers, data=data)
print(response.json())