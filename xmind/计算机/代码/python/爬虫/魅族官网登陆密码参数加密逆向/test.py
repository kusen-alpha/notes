import execjs

# https://login.flyme.cn/

with open('./test.js', encoding='utf8') as f:
    js_code = f.read()
passwd = "123"

password = execjs.compile(js_code).call('get_pwd', passwd)
print(password)
