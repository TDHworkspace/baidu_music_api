#encoding=utf-8
'''
Created on 2014年11月07日
@author: ci_knight
'''
################导包##################
import urllib
import urllib2
import time
import json
#--------------获取搜索音乐JSON------------------
def input_songname():
#    query = raw_input()
    data = {}
#定义GET参数
    data['from'] = 'webapp_music'
    data['method'] = 'baidu.ting.search.catalogSug'
    data['format'] = 'json'
    data['callback'] = ''
#   data['query'] = query
    data['query'] = '红玫瑰' #测试使用
    data['_'] = int(time.time())
    data['size'] = '1'
#处理URL,定义接口URL
    url_values = urllib.urlencode(data)
    url = 'http://tingapi.ting.baidu.com/v1/restserver/ting'
#定义HEADER
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    header = {'User-Agent': user_agent}
#发送REQUEST请求
    req = urllib2.Request(url, url_values, header)
#得到RESPONSE响应
    response = urllib2.urlopen(req,timeout=10) #10秒后timeout
    jsons = response.read()
#    print jsons
#f = open('1.mp3','w+')
#f = f.write(html)
#print html
###################处理JSON#################
#加载JSON数据
    j = json.loads(jsons)
    songname=[]
    songid=[]
    try:
        for i in range(1,100):
            #用 双list 存储 歌名与id
            songname.append(j['song'][i]['songname'])
            songid.append(j['song'][i]['songid'])
    except:
        print u'不需理会异常'
    print '############获取列表成功##############'
    return songname,songid


#----------------运行---------------------
songname,songid = input_songname()
for i in range(0,len(songname)):
    print str(i+1)+'. '+u'歌曲名: '+songname[i] +'  id: '+songid[i]


