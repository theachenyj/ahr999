import requests, json, time, math
from datetime import datetime

# api地址
url = 'https://dncapi.fxhapp.com/api/v2/index/arh999?code=bitcoin&webp=1'

# Webhook地址
webhook_url = 'https://discord.com/api/webhooks/925392888312004658/yhnDZr3oyl-V9P1Vh89zbPBZAcdsVEWZuv9AGMHQRr8_6I2oW84Q21nhlQxGhqV11vlS'

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

message = f'【BTC 囤币指标监控】时间: {data_time}\narh999: {arh999}\n{action}'

# 推送discord
payload = {
        "username": "Monitor Cat",
        "content": message
    }
requests.post(webhook_url, json=payload)

print(message)
