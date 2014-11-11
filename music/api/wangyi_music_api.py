#encoding: utf-8
'''
Created on 2014年11月9日

@author: ci_knight
'''
import json
import sys
from music.api import tools

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
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent': user_agent,
              #'Cookie': 'appver=1.5.2',
              }
    jsons = tools.r_json(url, val, header)
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

if __name__ ==  '__main__': 
    print u'输入歌名'
    name = raw_input().decode('utf-8')
    filelist = Get_WangYi_Music(name)
    print u'输入编号'
    num = int(raw_input())
    tools.playMp3(filelist[num])
