# -*- coding：utf-8 -*-
#2017/11/11 11:11:11

from PIL import Image

import numpy as np

a = np.asarray(Image.open(r'C:\myself.jpg').convert('L')).astype('float')
depth = 27.
grad = np.gradient(a)    #取图像灰度的梯度值
grad_x, grad_y = grad    #分别取横纵图像梯度值
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_e1 = np.pi / 2.     #光源俯视角度，弧度值
vec_az = np.pi / 4.      #光源方位角度，弧度值
dx = np.cos(vec_e1) * np.cos(vec_az)
dy = np.cos(vec_e1) * np.sin(vec_az)
dz = np.sin(vec_e1)

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))
im.save(r'C:\drawing.jpg')
                         
