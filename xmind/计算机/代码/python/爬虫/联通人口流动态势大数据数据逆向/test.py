import requests
import execjs

#  http://unicom_trip.133.cn/city/?system=cjfcts
response = requests.get('https://unicom_trip.133.cn/api/v1/city/source-top/V0152900?date=20210611')

with open('test.js') as f:
    js_code = f.read()

result = execjs.compile(js_code).call('dataDecode', response.text)
print(result)
