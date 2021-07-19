import re

import requests
import execjs


response = requests.get('http://www.csti.cn/uc/login/serviceLogin.htm')
login_salt = re.findall(r'login_salt = "(.*?)"', response.text)[0]

with open('./test.js', encoding='utf8') as f:
    js_code = f.read()

input_password = "111"
password = execjs.compile(js_code).call('get_pwd', input_password, login_salt)
print(password)

