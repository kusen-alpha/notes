import json

import requests
import execjs

# https://www.qimingpian.cn/finosda/project/pinvestment

data = 'time_interval=&tag=&tag_type=&province=&lunci=&page=1&num=20&unionid='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
response = requests.post('https://vipapi.qimingpian.com/DataList/productListVip', json=data, headers=headers)
encrypt_data = response.json()['encrypt_data']
with open('./test.js', encoding='utf8') as f:
    js_code = f.read()

result = execjs.compile(js_code).call('o', encrypt_data)  # JSON.parse可不在js中解析，在python中解析
result_json = json.loads(result)
print(result_json)
