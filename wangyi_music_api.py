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
import sys

reload(sys) #重新加载sys  
sys.setdefaultencoding('utf-8')

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
    #num = int(j['result']['songCount'])
    #print num
    link = []
    try:
        for i in range(10):
            print str(i)+'. '+j['result']['songs'][i]['name']+'-'+j['result']['songs'][i]['artists'][0]['name']
            link.append(j['result']['songs'][i]['audio'])
    except:
        print u'获取下载地址失败'
    return link

def playMp3(filename):
    mp3 = mp3play.load(filename)
    i = 1
    while(i):
        mp3.play()
        print u'时长'+ str(mp3.seconds()) + u'秒'
        time.sleep(mp3.seconds())
        mp3.stop()
        print u'你已经循环了'+ str(i) +u'了'

if __name__ ==  '__main__': 
    print u'输入歌名'
    name = raw_input().decode('GBK')
    filelist = Get_WangYi_Music(name)
    print u'输入编号'
    num = int(raw_input())
    playMp3(filelist[num])
