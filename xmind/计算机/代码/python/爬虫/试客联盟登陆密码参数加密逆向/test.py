import re
import execjs
import requests

# response = requests.get('http://login.shikee.com/')
# v = re.findall(r'src="/getkey\?v=(.*?)"',response.text, flags=re.M|re.S)[0]
# response = requests.get('http://login.shikee.com/getkey?v=%s'%v)
# rsa_n = re.findall(r'rsa_n = "(.*?)"', response.text)[0]

# 可能是固定的
rsa_n = "DC1683EEAA2B709F97743773E18F53E3C9A15D12465CE82227A6E447E6EC590D0B569876BB631B0AB4D67881E7EC874066D6E022E2978B4C6EAA8903EC1774AAE040A3BEAF9C2B48730ADD46BEF5F0C8109DB6FCEFED0F4A84CCD7AFFDB4FB4214DA0D0FF1A8E2831E81FA4D7C2F4346184EEC87CE42230FC320B2B4E392ECDF"

with open('./test.js', encoding='utf8') as f:
    js_code = f.read()
passwd = "123"

password = execjs.compile(js_code).call('get_pwd', passwd, rsa_n)
print(password)
