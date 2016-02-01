#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """
import sys

from PIL import Image

img = Image.open('wanzi.png')
print(img.format, img.size, img.mode)
img.thumbnail((200, 200))
img.save('thumb.jpg', 'JPEG')

print(sys.path)
