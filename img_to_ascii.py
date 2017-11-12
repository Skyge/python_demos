# -*- coding:utf-8 -*-
#2017/11/12 10:38

from PIL import Image

IMG = r'C:\Users\Administrator\Desktop\dora.png'
WIDTH = 80
HEIGHT = 80

ascii_char = list("$@B%8){}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到自定义的字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    #把图片的RGB值转换成灰度值

    unit = (256.0 + 1)/length
    
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)   #更改图片的显示比例
    #设置缩放图片的质量（PIL.Image.NEAREST：最低质量，PIL.Image.BILINEAR：双线性，
    #PIL.Image.BICUBIC：三次样条插值，Image.ANTIALIAS：最高质量）

    txt = ""
    
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.load()[j,i])
            #im.load()通过这个对象访问比方法getpixel()和putpixel()快很多
        txt += '\n'

    print (txt)

    #字符画输出到文件
    with open("output.txt",'w') as f:
        f.write(txt)
