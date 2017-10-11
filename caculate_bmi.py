# -*- coding:utf-8 -*-
#2017/10/11 23:33
'''
    caculate BMI
'''

def caculate_bmi():
    '''
        BMI(Body Mass Index,身体质量指数),是用体重公斤数除以身高

        米数平方得出的数字，是目前国际上常用的衡量人体胖瘦程度以

        及是否健康的一个标准。
        
        分类	BMI 范围
        偏瘦	<= 18.4
        正常	18.5 ~ 23.9
        过重	24.0 ~ 27.9
        肥胖	>= 28.0
    '''
    height=input('请输入您的身高(cm):')
    weight=input('请输入您的体重(kg):')
    BIM=float(weight)/((float(height)/100)**2)
    print('您的BIM指数为：',BIM)
    if BIM <18.5:
        print('您偏瘦，需要加强营养！')
    elif cal_BMI <= 23.9:
        print('很棒！您的身材保持的很好！')
    elif cal_BMI <27.9:
        print('您有一丢丢胖，要注意控制饮食！')
    else:
        print('真糟糕，您要加强锻炼，不能再多吃了！')

if __name__ == '__main__':
    caculate_bmi()
    for i in range(10):
        choose = input('您是否愿意继续计算BMI(y/n)：')
        if choose == 'y':
            caculate_bmi()
        else:
            break
