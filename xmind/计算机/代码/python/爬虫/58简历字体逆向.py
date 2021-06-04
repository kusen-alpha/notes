import requests
import re
import base64
from fontTools.ttLib import TTFont
from io import BytesIO

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'cookie': 'f=n; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; myLat=""; myLon=""; id58=MvsigmC08TTo4N+WbL3QNA==; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; mcity=bj; 58tj_uuid=a88038f9-6116-4fbe-a31c-bca16f2122fc; new_uv=1; utm_source=market; init_refer=https%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.000000aKLxgxXaekCbtx41o5Wwd_yjQDWKNda1RsBqZiM2wacRB06aMptYHjR8C5sKCgung7fQPn4QEF1JwRabTAcQst06Fdwd_aiMV3xC1uwabgpbUK94x05HkynAdr0iEobaDKdXvoYnpjOS5cnWPmZ2jUxvYTBdEwDjbOchGqi8vfD89GopAyJPnNdsZ0UB2xVcEIhzFLG7IzXGQlrqqyAv5S.DY_NR2Ar5Od66z3PrrW6ButVvkDj3n-vHwYxw_vU85YIMAQV8qhORGyAp7WIu8L6.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPHWPoQ5Z0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5HR31pz1ksKzmLmqnfKdThkxpyfqnHRzP1DkrH6dPfKVINqGujYkPjcznWD3P6KVgv-b5HDsrjmvn1RL0AdYTAkxpyfqnHczP1n0TZuxpyfqn0KGuAnqiD4a0ZKGujYk0APGujY1rjn0mLFW5Hndn1mL%2526ck%253D8252.1.129.366.158.361.151.12; wmda_new_uuid=1; wmda_uuid=4bb9835266891902574298a6d3382795; wmda_session_id_11187958619315=1622470970670-c632d9e0-5bcf-76bb; als=0; new_session=0; wmda_session_id_1731916484865=1622470973827-6e263fe7-160c-cf0f; xxzl_deviceid=2pSMKHEi1KyxMD%2BIEmanH0aFdECa8Xp7JS%2FmgKLsxE%2FkzEQHnf5hnUOi6NQm8efu; f=n; 58home=sz; city=sz; commontopbar_new_city_info=4%7C%E6%B7%B1%E5%9C%B3%7Csz; commontopbar_ipcity=bj%7C%E5%8C%97%E4%BA%AC%7C0; sessionid=3b80e117-1bf4-4ba3-96e6-18f572ab5968; param8616=0; param8716kop=1; wmda_session_id_10104579731767=1622471019935-f665180b-5163-acec; wmda_visited_projects=%3B11187958619315%3B1731916484865%3B10104579731767; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1622471064; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1622471064; www58com="UserID=67124064124182&UserName=lt0pqxfjc"; 58cooper="userid=67124064124182&username=lt0pqxfjc"; 58uname=lt0pqxfjc; PPU=UID=67124064124182&UN=lt0pqxfjc&TT=1bc9b4c34e60772143b38c7b3dbbc1b4&PBODY=S2QNZ5IAPyQnheKTCx5A_SeJ9bupwc7uQyKVPxqODZ1XdyCTyNyy9zQ2yy4KEoVqESILd5Hn2rTxViR0ejaesFW8b-FkBDxFs9mcMd7qE3J6RO5ECGk3yN6RWBWBXUp2_S8asaWO_74G3-PRNwxnIVyANZW0PLXsgtBX2mOTcoc&VER=1; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1622471354; isSmartSortTipShowed=true; ljrzfc=1; xxzl_smartid=b8387f63e0efc4a0c88b1a56ce7a64ac; JSESSIONID=8D752E2F1EAF36F353692798BF3D9950; Hm_lpvt_a3013634de7e7a5d307653e15a0584cf=1622471423; xxzl_cid=d1caac00d3a24c8d943064c067608d64; xzuid=867ed038-61cd-4a1b-a3d5-0538339e27df; jl_list_left_banner=101'
}
url = 'https://sz.58.com/searchjob/'
content = requests.get(url, headers=headers).text
base64_font = re.search(r'base64,(.*?)\)', content, re.S).group(1)
font = base64.b64decode(base64_font)
tf = TTFont(BytesIO(font))
print(tf.getGlyphNames())
with open('58.woff', 'wb') as f:
    f.write(font)

tt_font = TTFont('58.woff')
tt_font.saveXML('58.xml')

for index, glyph_name in enumerate(tf.getGlyphNames()[1:-1]):
    temp = tf['glyf'][glyph_name].coordinates
    x1, y1 = temp[0]
    x2, y2 = temp[1]
    new = (x2-x1, y2-y1)
    key = glyph_name.replace('uni', '&#x').lower()
    print(key)
