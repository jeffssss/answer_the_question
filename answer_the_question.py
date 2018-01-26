# -*- coding: utf-8 -*-

# @Author  : Allen_Liang
# @Time    : 2018/1/14 15:38

from aip import AipOcr  
import requests
import json
import time
from PIL import Image
import os
import matplotlib.pyplot as plt
import webbrowser
#命令行颜色包
from colorama import init,Fore
init()
#ios相关的包
import wda
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 百度OCR_api定义常量
# 输入你的API信息  
APP_ID = ''  
API_KEY = ''  
SECRET_KEY = ''  
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)  

c = wda.Client()
s = c.session()


# 定义参数变量  
options = {  
  'detect_direction': 'true',  
  'language_type': 'CHN_ENG',  
}  

#利用adb从手机中获取屏幕事实截图，并pull到计算机上
def pull_screenshot():
    c.screenshot('screenshot.png')

# 根据你的手机配置屏幕截图信息，我的测试手机是meizu_pro6s,配置如下
# 冲顶大会图片切割
def image_cut_tounao():
    img = Image.open("./screenshot.png")
    #区域由一个4元组定义，表示为坐标是 (x0, y0, x1, x2)
    #问题区域
    question  = img.crop((25, 390, 725,605))
    question.save('question.png')
    resizeImg(ori_img='question.png',dst_img='question_resize.png',dst_w=140,dst_h=43,save_q=35)
    #选线区域
    choices = img.crop((155, 665, 595, 1195))
    choices.save('choices.png')
    resizeImg(ori_img='choices.png',dst_img='choices_resize.png',dst_w=88,dst_h=106,save_q=35)



# 读取问题图片  
def get_file_content(q_filePath):  
    with open(q_filePath, 'rb') as fp:  
        return fp.read()
# OCR识别问题文字
def question_words(q_filePath,options):
    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(q_filePath), options)
    q_Result_s=''
    words_list=[]
    for word_s in result['words_result']:
        words_list.append(word_s['words'])
    q_Result_s = q_Result_s.join(words_list)
    #print(q_Result_s)
    return q_Result_s

# 读取选项图片    
def get_file_content(c_filePath):  
    with open(c_filePath, 'rb') as fp:  
        return fp.read()

# OCR识别问题文字
def choices_words(c_filePath,options):
    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(c_filePath), options)
    c_Result_s=''
    words_list=[]
    for word_s in result['words_result']:
        words_list.append(word_s['words'])
    return words_list

#网页分析统计
def count_base(question,choices):
    #print('题目搜索结果包含选项词频计数')
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text
    #print(content)
    counts = []
    dic = {}
    print(Fore.YELLOW +'-----------------欢迎你使用卖假货学长的小助手---------------------------'+ Fore.RESET)
    print('问题: '+question)
    #print('———————————————————————————')
    if '不是' in question or '不能' in question or '不属于' in question  or '不可以' in question or '不包括' in question:
        print('——————————————————————————')
        for i in range(len(choices)):
            counts.append(content.count(choices[i]))
            dic[choices[i]] = counts[i]
            print(choices[i] + " : " + str(counts[i]))
        if dic:
            if dic[max(dic, key=dic.get)] != dic[min(dic, key=dic.get)]:
                print '请注意此题为否定题，建议选择：', Fore.RED + min(dic, key=dic.get), Fore.RESET
                #print()
    
    else:
        print('——————————————————————————')
        for i in range(len(choices)):
            counts.append(content.count(choices[i]))
            dic[choices[i]] = counts[i]
            print(choices[i] + " : " + str(counts[i]))
        if dic:
            if dic[max(dic, key=dic.get)] != 0:
                
                print u'请注意此题为肯定题，建议选择：', Fore.RED + max(dic, key=dic.get) ,Fore.RESET 
                #print()


def game_fun(image_cut):
    while True:
        start = time.time()
        pull_screenshot()
        #截图参数
        image_cut()
        q_filePath = "question_resize.png"
        c_filePath = "choices_resize.png"
        question = question_words(q_filePath,options)
        choices = choices_words(c_filePath,options)
        count_base(question, choices)
        # count_base(question, choices)
        # count_base(question, choices)
        # count_base(question, choices)
        # count_base(question, choices)
        
        #webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))
        end = time.time()
        print(Fore.YELLOW +'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+ Fore.RESET)
        print(Fore.GREEN +'+++++++++++++++++++++'+'程序用时：' + str(end - start) + '秒'+'+++++++++++++++++++++'+ Fore.RESET)
        #print('程序用时：' + str(end - start) + '秒')
        print(Fore.YELLOW +'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'+ Fore.RESET)
        go = raw_input('输入回车继续运行')

def resizeImg(**args):
    args_key = {'ori_img':'','dst_img':'','dst_w':'','dst_h':'','save_q':75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = Image.open(arg['ori_img'])
    ori_w,ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
        if arg['dst_w'] and ori_w > arg['dst_w']:
            widthRatio = float(arg['dst_w']) / ori_w #正确获取小数的方式
        if arg['dst_h'] and ori_h > arg['dst_h']:
            heightRatio = float(arg['dst_h']) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    im.resize((newWidth,newHeight),Image.ANTIALIAS).save(arg['dst_img'],quality=arg['save_q'])


if __name__ == '__main__':
    init()
    #只要头脑王者就ok
    game_fun(image_cut_tounao)

