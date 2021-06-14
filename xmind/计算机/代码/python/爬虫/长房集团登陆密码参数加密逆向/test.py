import execjs

with open('test.js', encoding='utf8') as f:
    js_code = f.read()
node = execjs.get()

ctx = node.compile(js_code)
result = ctx.eval('get_pwd("{0}")'.format('123'))
print(result)
