#coding=utf-8
'''
Created on 2014年11月10日

@author: ci_knight
'''
import urllib
import urllib2
import mp3play
import time

#----传入url和参数 返回json-----
def r_json(url,param,header):
#发送REQUEST请求
    url_values = urllib.urlencode(param)
    try:
        req = urllib2.Request(url, url_values, header)
#得到RESPONSE响应
        response = urllib2.urlopen(req,timeout=10) #10秒后timeout
    except:
        print '请求url失败'
    jsons = response.read()
    return jsons

#------------下载函数-------------
def Down_Music(song_url ,song_name, formats):
    print u'开始下载......'
    try:
        urllib.urlretrieve(song_url, song_name+'.'+formats,reporthook= report_hook)
    except:
        print u'下载地址出错,下载失败'
    print u'下载完成,已保持到当前目录下'

#------------显示进度条----------
def report_hook(count, block_size, total_size):
    print '%02d%%' %(100.0*count*block_size/total_size)
#--------播放mp3---
def playMp3(filename):
    mp3 = mp3play.load(filename)
    i = 1
    print u'时长'+ str(mp3.seconds()) + u'秒'
    while(i):
        mp3.play()
        time.sleep(mp3.seconds())
        mp3.stop()
        print u'你已经循环了'+ str(i) +u'次了'
        i += 1 