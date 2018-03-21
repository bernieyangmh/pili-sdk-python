# -*- coding: utf-8 -*-

from pili import Mac, Hub

access_key = "..."


# 替换成自己 Qiniu 账号的 SecretKey
secret_key = "..."


hub_name = "..."

stream_name = "..."

fname = 'example_fname.mp4'

mac = Mac(access_key, secret_key)

hub = Hub(mac, hub_name)

stream = hub.get(stream_name)

print(stream.saveas(start_second=0, end_second=0, format='mp4', fname=fname))
