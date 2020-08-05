# -*- coding: utf-8 -*-
'''
@File    :   base.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/8/5 21:49   gujiayue      1.0         None
'''

import requests

response = requests.get("http://www.nmc.cn/publish/observations/hourly-precipitation.html")
response.encoding="utf-8"
print(response.status_code)
print(response.text)