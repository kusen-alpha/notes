import re

import requests
from requests.packages import urllib3
import execjs

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}
response = requests.get('https://authserver.ssti.net.cn/authserver/login', verify=False, headers=headers)
pwdDefaultEncryptSalt = re.findall(r'var pwdDefaultEncryptSalt = "(.*?)"', response.text)[0]
with open('./test.js', encoding='utf8') as f:
    js_code = f.read()
passwd = "123"

password = execjs.compile(js_code).call('get_pwd', passwd, pwdDefaultEncryptSalt)
print(password)
