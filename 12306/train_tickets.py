# -*- coding:utf-8-*-
# version 1.0

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

username = "your_usename"
password = "your_password"

from_station = "%u5317%u4EAC%2CBJP" # 出发地：北京
to_station = "%u957F%u6625%2CCCT"   # 目的地：长春
from_date= "2018-02-05"


def login():
    login_url = "https://kyfw.12306.cn/otn/login/init"
    login_done_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    browser = webdriver.Chrome()
    browser.get(login_url)
    
    user = browser.find_element_by_id("username")  # 找到用户名输入框
    user.clear  # 清除用户名输入框内容
    user.send_keys(username)  # 在框中输入用户名
    
    pwd = browser.find_element_by_id("password")  # 找到密码输入框
    pwd.clear
    pwd.send_keys(password)

    while True:
        current_page_url = browser.current_url   # 获取当前页面url
        if current_page_url != login_url:
            if current_page_url[:-1] != login_url:  # 排除错误验证码页面
                if current_page_url == login_done_url:  # 跳转成功
                    break
                
        else:
            time.sleep(1)
            print("自行点击，进行图片验证")
    return browser
   

def query(browser):
    
    query_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    browser.get(query_url)

    browser.add_cookie({"name": "_jc_save_fromStation",
                       "value": from_station
                       })

    browser.add_cookie({"name": "_jc_save_toStation",
                       "value": to_station
                       })

    browser.add_cookie({"name": "_jc_save_fromDate",
                       "value": from_date
                       })
    browser.refresh()
    # browser.find_element_by_xpath("/html/body/div[5]/div[5]/div[2]/div[2]/div[2]/ul/li[2]/label").click()
    browser.find_element_by_xpath('//input[@name="cc_type" and @value="Z"]').click()
    
    browser.find_element_by_id("query_ticket").click()   


def book(browser):
    print("you are booking")
    query_times = 0
    time_begin = time.time()

    while True:
        time.sleep(0.1)
        try:
            ticket = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="RW_2400000Z630C"]'))
                )
            ticket_status = ticket.text
        except:
            ticket = WebDriverWait(browser, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="RW_2400000Z630C"]'))
                )
            ticket_status = ticket.text
        
        if ticket_status == "无" or ticket_status == "*":
            query_times += 1
            time_end = time.time()
            print("第{}次查询，总耗时为{}秒".format(query_times, time_end-time_begin))
            continue
        else:
            browser.find_element_by_xpath('//*[@id="ticket_2400000Z630C"]/td[13]/a').click()
            break

    passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    while True:
        if browser.current_url == passenger_url:
            print("进入选择乘客信息界面")
            break
        else:
            print("等待页面跳转")

    while True:
        try:
            browser.find_element_by_xpath('//*[@id="normalPassenger_0"]').click()
            break
        except:
            print("等待刷新联系人列表")

    browser.find_element_by_xpath('//*[@id="submitOrder_id"]').click()

    while True:
        try:
            
            browser.find_element_by_id("qr_submit_id").click()
            
            print ("Success!")
            break
        except:
            print ("请手动通过图片验证码")
            time.sleep(3)
            break
    return "Welcome to back home!"        

            

if __name__ == "__main__":
    browser = login()
    query(browser)
    book(browser)







