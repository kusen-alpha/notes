import execjs
import requests

url = 'https://store.steampowered.com/login/getrsakey/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
data = {
    'donotcache': '1623597699703',
    'username': '15811072625'
}
response = requests.post(url, headers=headers, data=data)
json_data = response.json()
publickey_mod = json_data['publickey_mod']
publickey_exp = json_data['publickey_exp']
with open('test.js') as f:
    js_code = f.read()
password = '123'
result = execjs.compile(js_code).call('get_pwd', password, publickey_mod, publickey_exp)
print(result)
