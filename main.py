# https://www.jizhy.com/44/school/library
# 极志愿 大学排名
# -*- coding: utf-8 -*-
# Date:2024-08-24 02 04
import hashlib
import time
import requests
import execjs

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'Hm_lvt_2610e5c202b60841b30a62960fbef0ad=1724429265; PI=44; Hm_lpvt_2610e5c202b60841b30a62960fbef0ad=1724431275',
    'origin': 'https://www.jizhy.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.jizhy.com/44/school/library',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

U = "146fd1e66513611ac7af69f21f1d7725"

with open('static/sign.js', 'r', encoding='utf-8') as file:
    js_code = file.read()

json_data = {
    'page': 1,
    'page_len': 10,
    'filter': {},
    'app_id': '98357f659cf8fb6001cff80f7c6b85f2',
    'ts': 1724431628696,
    'platform': 'desktop',
    'v': 210,
}

current_timestamp = int(time.time() * 1000)
json_data['ts'] = current_timestamp
ordered_keys = ['app_id', 'filter', 'page', 'page_len', 'platform', 'ts', 'v']
query_string = '{' + '&'.join(f"{key}={json_data[key]}" for key in ordered_keys) + '}' + "&key=" + U
context = execjs.compile(js_code)

sign = hashlib.md5(query_string.encode("utf-8")).hexdigest().upper()
print(sign)
result_sign = context.call('Xt', query_string)
print(result_sign)
json_data['sign'] = result_sign

response = requests.post('https://www.jizhy.com/gaokao/sch/filter', headers=headers, json=json_data)

print(response.text)
