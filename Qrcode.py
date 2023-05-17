# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:02:17 2023

@author: HFY
"""


import qrcode
from mainOS import name
from mainOS import ID
from mainOS import filename


data = [name, ID, filename]

# 生成二维码
img = qrcode.make(data)

img.save('qrcode.png')


