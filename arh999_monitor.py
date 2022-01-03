import requests, json, time, math
from datetime import datetime

# api地址
url = 'https://dncapi.fxhapp.com/api/v2/index/arh999?code=bitcoin&webp=1'

"""# Webhook地址
webhook_url = 'https://discord.com/api/webhooks/924867380746780703/qV7V-z01cxl9d8ynexLB7Z-LKWeBDyenXboxGYz8HHPheVkmMDsNp3xweaOAWRZ_9wSm'
"""
# ifttt arh999 地址
ifttt_url = 'https://maker.ifttt.com/trigger/arh999/with/key/bVGEDkrCumRST4bL2kYcoC'
# 网络请求
r = requests.get(url)
if r.status_code == 200:
    jsonstr = json.loads(r.text)
else:
    print("请求码为{}, 获取数据失败".format(r.status_code))

tmp = jsonstr['data'][len(jsonstr['data'])-1]
arh999 = tmp[1]
data_time = datetime.fromtimestamp(int(tmp[0])).strftime('%Y-%m-%d %H:%M:%S')

if arh999 < 0.45:
	action = '抄底了!'
elif arh999 >= 0.45 and arh999 < 1.2:
	action = '定投了!'
else:
	action = '休息。'


# 推送ifttt
payload = {
        "value1": str(arh999),
        "value2": action
    }
requests.post(ifttt_url, params=payload)
