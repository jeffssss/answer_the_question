# -*- coding: utf-8 -*-
from PIL import Image
import os
import matplotlib.pyplot as plt

#你的图片位置
img = Image.open("screenshot.png")

#区域由一个4元组定义，表示为坐标是 (x0, y0, x1, x2)
question  = img.crop((25, 390, 725,605))
question.save('question.png')
	#选线区域
#区域由一个4元组定义，表示为坐标是 (x0, y0, x1, x2)
choices = img.crop((155, 665, 595, 1195))
choices.save('choices.png')

#图片展示位置
plt.subplot(212)
im = plt.imshow(img, animated=True)
plt.subplot(221)
im2 = plt.imshow(question, animated=True)
plt.subplot(222)
im3 = plt.imshow(choices, animated=True)
plt.show()