import re
import requests
import execjs

response = requests.get('https://passport.5173.com/?returnUrl=http%3a%2f%2fwww.5173.com%2f')
pkey = re.search(r'PasswordKey:"(.*?)"', response.text).group(1)

passwd = '111'
with open('test.js', encoding='utf-8') as f:
    passwd_js = f.read()

passwd = execjs.compile(passwd_js).call('get_pwd', passwd, pkey)
print(passwd)
