import execjs

with open('test.js') as f:
    js_code = f.read()

result = execjs.compile(js_code).call('get_pwd', '123', )
print(result)


