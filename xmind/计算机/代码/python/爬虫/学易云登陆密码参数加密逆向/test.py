import execjs
import requests

# response = requests.get('http://passport.xueyiyun.com/api/account/rsaPublicKeyToBit')
# rsaPublicKey = response.json() # 可能是固定的

with open('./test.js', encoding='utf8') as f:
    js_code = f.read()
passwd = "123"
rsaPublicKey = {"dwKeySize": 2048, "exponent": "010001",
                "modulus": "B84DB8167B9059532D1ED2283BDFEF69FAE89666A8A38A6EB32AF44803739892BE13053264872E1FD42775C1553266530AEED97D57441822AC9B9863B250AE1078B6B8C7050416EC56D6750FF5C11876430D8A5CDB5C0B3C4BD21A02524D8DEE7B56D53F078F5C684385D94EC79AB3EEFBA20B11877B30BBFCC8CCA8A0AFE6E7EE9D1E3B79DBD8B7FF0212F123012A738D1E515B82AAD85C00D8610E61D818E3B975D63E0C02FE39B68A8C8E58771362A2AEBBE9FFDD52E814EA4902F59AD5E3FEE10DDEBF54961EAFED8B0E95FB2B5D7BC8142DE0219D08E43CF64E91F3EF8682E1E156F9E9924C32EB82CB30C1040747A673419F71CB171A67ECBF0E39A285"}
password = execjs.compile(js_code).call('get_pwd', passwd, rsaPublicKey)
print(password)
