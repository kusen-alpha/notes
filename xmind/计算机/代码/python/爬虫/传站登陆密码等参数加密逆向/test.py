import re

import requests
import execjs

response = requests.get('https://yhz566.com/')
vvccookie = re.findall(r'id="vvccookie" name="vvccookie" value="(.*?)"', response.text)[0]
with open('./test.js', encoding='utf8') as f:
    js_code = f.read()
username = '15811072625'
loginpass = "hu119454"
code = "512939"

password = execjs.compile(js_code).call('get_pwd', username, loginpass, code, vvccookie)
print(password)
