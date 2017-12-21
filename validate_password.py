# -*- coding:utf-8 -*-
# 2017/12/19 18:12
# version 1.0
'''
    Verification of password strength
    密码强度检测

    低级密码要求：
        1. 密码由单纯的数字或字母组成
        2. 密码长度小于等于6位

    中级密码要求：
        1. 密码必须由数字、字母或特殊字符（仅限：`~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
        2. 密码长度小于等于12位

    高级密码要求：
        1. 密码必须由数字、字母及特殊字符（仅限：`~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
        2. 密码只能由字母开头
        3. 密码长度不能低于18位
'''

import string

flag_len = 0
flag_strength = 0
satisfied = False
   

# 打印结果
while True :
    symbols = string.punctuation    # 特殊字符
    chars = string.ascii_letters    # 大小写字母
    nums = string.digits    # 数字

    passwd = input('请输入需要检查的密码组合：')

    # 判断长度
    length = len(passwd)

    while (passwd.isspace() or length == 0) :
        passwd = input("您输入的密码为空，请重新输入：")
        length = len(passwd)

    flag_len = 0
    if length <= 6:
        flag_len = 1
    elif 6 < length <= 12:
        flag_len = 2
    else:
        flag_len = 3

    flag_strength = 0
    # 判断是否包含特殊字符
    for each in passwd:
        if each in symbols:
            flag_strength += 1
            break
        
    # 判断是否包含字母
    for each in passwd:
        if each in chars:
            flag_strength += 1
            break
    
    # 判断是否包含数字
    for each in passwd:
        if each in nums:
            flag_strength += 1
            break
    
    print("密码长度等级：",flag_len,"级")
    print("密码强度等级：",flag_strength,"级")
    print("您的密码安全级别评定为：", end="")
    if flag_len == 1 or flag_strength == 1 :
        print("I级,您的密码强度比较弱，请根据建议及时修改")    
    elif flag_len == 2 or flag_strength == 2 :
        print("II级，您的密码强度良好，可根据建议提升密码强度")
    else :
        print("III级，您的密码强度很高")
        print("请继续保持")
        satisfied = True

    if not satisfied:
        print("请按以下方式提升您的密码安全级别：\n\
        \t1. 密码采用数字、字母及特殊字符三种组合\n\
        \t2. 密码只能由字母开头\n\
        \t3. 密码长度增加至18位'")
    
