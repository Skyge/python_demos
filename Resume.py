#/usr/bin/env python3
# -*- coding：utf-8 -*-

import random
import re


def color(messages):
  '''
    给已输入的信息渲染颜色

    \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->

    \033[0m          <!--采用终端默认设置，即取消颜色设置-->
  '''
  color_show = [0,1,4]    #显示方式：0：终端默认设置；1：高亮显示；4：使用下划线
  color = '\033[%d;%d;%dm' % (random.choice(color_show),\
                              random.randint(30,37),40)
  return '%s %s\033[0m' % (color,messages)


def len_zh(data):
    '''
        测量信息的字段长度，以便排版。
    '''    
    temp = re.findall('[^\w. ]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)


def colorprint(mes, flag=True):
    def _deco(func):
        def wrapper(args):
            res = func(args)
            print (color(mes + ':\n'))
            if flag:
                for k1, v1 in res.items():
                    zh = len_zh(k1)
                    if not isinstance(v1, dict):
                        print ('{0} {1}'.format(k1.ljust(20+zh), v1))
                    else:
                        print ('{0}'.format(k1.ljust(20+zh)))
                        for k2, v2 in v1.items():
                            zh = len_zh(k2)
                            print ('{0} {1}'.format(k2.ljust(16+zh), v2))
            else:
                for i in res:
                    if not isinstance(i[1], dict):
                        print (i)
                    else:
                        for k, v in i[1].items():
                            zh = len_zh(k)
                            print ('{0}[{1}] {2}'.format(k.ljust(17+zh), i[0], v))
            print ()
            return res
        return wrapper
    return _deco


class Resume():

    def __str__(self):
        return color('李天奇的python简历'.center(200))
                      
    __repr__ = __str__

    @property
    @colorprint('个人信息')
    def personal_information(self):
        return {
            'Name' : '李天奇',
            'Gender' : 'Male',
            'Born' : (1993, 10, 4),
            'Education' : {
                'School Name' : '长春工业大学',
                'Major' : '自动化',
                'Degree' : 'Four-year college',
                'Graduation' : 2016
            },
            'Tel' : '18844062006',
            'Email' : '18844062006@163.com',
            'Target Positions' : re.compile(
                " Python Developer Intern|Python Developer Assistant",re.I|re.M).pattern
        }
    @property
    @colorprint('个人特点')
    def characteristics(self):
        return {
            '心里承受能力强': '从非计算机专业-Linux运维-Python开发',
            '热衷和喜爱': '正是因为喜欢编程, 我才会放弃大学所学专业',
            '自学能力强': '以大学的计算机基础为基础, 不断自学去发现',
            '毅力和耐性': '遇到解决不了的难题，会在专业书籍中查找或去专业网站咨询，无论怎样，从不放弃。',
            'is_geek' : True
        }

    @property
    @colorprint('个人能力')
    def skills(self):
        return {
            'Language' : {
                '熟悉' : ['Python', 'Bash'],
                '了解' : ['C++']},
            'OS' : ['CentOS','Ubuntu'],
            'Tool' : ['PyCharm', 'Git'],
            'Databaseandtools' : ['MySQL','Redis', 'SQLAlchemy'],
            'WebFramework' : {
                '熟悉' : ['Django'],
                '了解' : ['Flask']
            },
            'OtherFramework' : ['bs4','scrapy']
        }

    @property
    @colorprint('工作经验', False)
    def work_experience(self):
        return enumerate([
            {
                'Time period' : '2017.03 - 2017.07',
                'Company Name' : '伟本智能机电（上海）股份有限公司',
                'Position' : '初级工程师'
            }
            
        ])

    @property
    @colorprint('项目经验',False)
    def projectexperience(self):
        return enumerate([
            {
                'Project' : '应用Django开发个人博客',
                'Description' : ('具备博客基本功能（分类，归档，搜索和评论），'
                                 '利用Bootstrap完善前端展示，'
                                 '完成Nginx和uWSGI的服务器端部署')
            },
            {
                'Project' : '基于Socket的聊天工具',
                'Description' : ('还在代码中，'
                                 '客户端图形编程准备使用qt')
            }
        ])

    @property
    @colorprint('@Where', False)
    def findme(self):
        return enumerate([
            {
                'Link' : 'http://github.com/Skyge',
                'Description' : '个人GitHub'},
            {
                'Link' : 'http://weibo.com/u/3227090323',
                'Description' : '微博'}
        ])
    
    def show(self):
        self.personal_information
        for pro in ['characteristics','skills','work_experience','projectexperience','findme']:
            getattr(self, pro)


if __name__ == '__main__':
    resume = Resume()
    print(resume)
    resume.show()
