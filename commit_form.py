from selenium import webdriver
import time
import requests
from PIL import Image
from io import BytesIO
import io
import random
import re
import pytesseract

#利用pytesseract的验证码识别
def restar5():
    
    try:
        #点击登录
        login_button = browser.find_element_by_id("login")
        login_button.click()
        time.sleep(k)
        print("正在破解验证码...")
        #获取屏幕截图
        browser.get_screenshot_as_file('./screenshot.png')
        #截取验证码位置
        element = browser.find_element_by_id('verifyCode')
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        im = Image.open('screenshot.png')
        im = im.crop((left, top, right, bottom))
        #保存验证码图片
        im.save('./code.png')
        #用py处理文字化输出
        
        im=Image.open('code.png')
        print("识别验证码为：" + pytesseract.image_to_string(im))

        #填入验证码
        text = pytesseract.image_to_string(im)
        verf = browser.find_element_by_id("vcode")
        #检验验证码是否为5位
        if len(text) != 5:
            text = ("error")
        

        verf.send_keys(text)
        time.sleep(k)
        sec_button = browser.find_element_by_xpath("/html/body/div[2]/div[3]/a[2]")
        time.sleep(k)
        sec_button.click()
        time.sleep(k)
        #检查是否成功登录
        check = browser.find_element_by_xpath("/html/body/header/div/a/i")
        if check == True:
            print("登录成功，正在检查表格...")
        else:
            pass
        
    except:
        print("失败，正在重试。。。")
        restar5()
        










#随机时间间隔
k = random.randint(1,3)
#打开网址
print("正在启动...")

browser=webdriver.Chrome()
#在下方填入网址
browser.get('XXXXXXX')
time.sleep(k)
#手动抓cookie后可存入下方跳过登录
try:
    print("尝试使用cookie登录")
    browser.delete_all_cookies()
    browser.add_cookie({'domain': '', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', '': False, 'value': ''})
    time.sleep(2)
    browser.get("")
    check = browser.find_element_by_xpath("/html/body/header/div/a/i")
    print("使用cookie登陆成功")
except:
    #OCR暴力验证码模块
    print("正在填写用户名...")
    name = browser.find_element_by_id('user')
    #填入用户名
    name.send_keys("XXXXXXX")
    time.sleep(k)
    print("正在填写密码...")
    keys = browser.find_element_by_id('pwd')
    #填入密码
    keys.send_keys("XXXXXXXXX")
    time.sleep(k)
    print("正在登陆...")
    restar5()





#点击调查框
try:
    clicktext = browser.find_element_by_xpath("/html/body/ul/li[1]/div")
    clicktext.click()
    time.sleep(k)
except:
    print("没有待填写的表格")
    browser.close()
    exit(0)




choicehubei = browser.find_element_by_xpath("/html/body/form/div[2]/div[1]/label[2]/i")
choicehubei.click()
choicetwice = browser.find_element_by_xpath("/html/body/form/div[2]/div[2]/label[2]/i")
choicetwice.click()
#第一次体温

tempcherfir = browser.find_elements_by_xpath("/html/body/form/div[2]/div[4]/input")
tempchersec = browser.find_elements_by_xpath("/html/body/form/div[2]/div[7]/input")

tempcherfir[0].clear()
tempcherfir[0].send_keys("36.5")
print("正在填写体温(36.5)...")
tempchersec[0].clear()
tempchersec[0].send_keys("36.6")
print("正在填写体温(36.6)...")
time.sleep(k)

try:
    print("正在选择地区...")
    #选择省份
    loca_sheng = browser.find_element_by_xpath("/html/body/form/div[2]/div[9]/div[1]/select[1]")
    loca_sheng.click()
    chose_sheng = browser.find_element_by_xpath("/html/body/form/div[2]/div[9]/div[1]/select[1]/option[2]")
    chose_sheng.click()
    time.sleep(3)
    #选择市
    loca_shi = browser.find_element_by_xpath("/html/body/form/div[2]/div[9]/div[1]/select[2]")
    loca_shi.click()
    chose_shi = browser.find_element_by_xpath("/html/body/form/div[2]/div[9]/div[1]/select[2]/option")
    chose_shi.click()
    #选择区
    loca_qu = browser.find_element_by_xpath("/html/body/form/div[2]/div[9]/div[1]/select[3]")
    loca_qu.click()
    time.sleep(5)
    chose_qu = browser.find_element_by_xpath("/html/body/form/div[2]/div[9]/div[1]/select[3]/option[15]")

    chose_qu.click()
    time.sleep(5)



except:
    print("不需要选择地区")


save_f = browser.find_element_by_xpath("/html/body/button")
time.sleep(k)
save_f.click()
time.sleep(k)
browser.close()
print("Success!")



