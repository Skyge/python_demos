# -*- coding:utf-8 -*-

from tkinter import *

reset = True
def buttonCallBack(event):
    global label
    global reset
    num = event.widget["text"]
    if num == "C":
        label['text'] = "0"
        return
    if num in "=":
        label['text'] = str(eval(label['text']))
        reset = True
        return 
    init = label['text']  
    if init =='0' or reset == True:  
        init = ""  
        reset = False  
    label['text'] = init + num

root = Tk()
root.title("计算器")

label = Label(root, background="white", anchor="se")
label['width'] = 35
label['height'] = 2
label.grid(row=1, columnspan=4, sticky="se")

showText = "789/456*123-0.C+"
for i in range(4):
    for j in range(4):
        button = Button(root, text=showText[i*4+j], width=7)
        button.grid(row=i+2, column=j)
        button.bind("<Button-1>", buttonCallBack)
        
showText="()"
for i in range(2):
    button = Button(root, text=showText[i], width=7)
    button.grid(row=6, column=2+i)
    button.bind("<Button-1>", buttonCallBack)
button = Button(root, text="=")
button.grid(row=6, columnspan=2, sticky="we")
button.bind("<Button-1>", buttonCallBack)

root.mainloop()

