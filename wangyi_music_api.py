#encoding: utf-8
'''
Created on 2014年11月9日

@author: ci_knight
'''
import urllib
import urllib2
import time
import json
import mp3play

def Get_WangYi_Music(s):
    val = {}
    val = {'limit': '10',
           #'sub': 'false',
           'type': '1',
           's': s,
           'offset': '0',
           }
#API_URL,处理URL参数
    url = 'http://s.music.163.com/search/get/'
    url_values = urllib.urlencode(val)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent': user_agent,
              #'Cookie': 'appver=1.5.2',
              }
    print url+'?'+url_values
#发送REQUEST请求
    req = urllib2.Request(url, url_values, header)
#得到RESPONSE响应
    response = urllib2.urlopen(req,timeout=10) #10秒后timeout
    jsons = response.read()
    #print jsons
###################处理JSON#################
#加载JSON数据
    j = json.loads(jsons)
    num = int(j['result']['songCount'])
    print num
    link = []
    try:
        for i in range(10):
            print str(i)+'. '+j['result']['songs'][i]['name']+'-'+j['result']['songs'][i]['artists'][0]['name']
            link.append(j['result']['songs'][i]['audio'])
    except:
        print u'获取下载地址失败'
    return link

def playMp3(filename):
    #filename = r'one year.mp3'
    #filename = r'http://m1.music.126.net/uCNvR9xHLoQIj1kIRyzadQ==/1012650209189889.mp3'
    mp3 = mp3play.load(filename)
    while(1):
        mp3.play()
        print mp3.seconds()
        time.sleep(mp3.seconds())
        mp3.stop()
print u'输入歌名'
name = raw_input()
filelist = Get_WangYi_Music(name)
print u'输入编号'
num = int(raw_input())
playMp3(filelist[num])
