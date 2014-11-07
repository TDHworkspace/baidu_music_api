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
class Baidu_Music():
#--------------获取搜索音乐JSON------------------
    def input_songname(self):
#       print u'请输入要搜索的音乐'
#       query = raw_input()
        val = {}
        val['from'] = 'webapp_music'
        val['format'] = 'json'
        val['callback'] = ''
        val['_'] = int(time.time())
        val['method'] = 'baidu.ting.search.catalogSug'
#       data['query'] = query
        val['query'] = '红玫瑰' #测试使用
        val['size'] = '1'
#API_URL,处理URL参数
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting'
        url_values = urllib.urlencode(val)
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
        artistname=[]
        try:
            for i in range(1,100):
                #用 双list 存储 歌名与id
                songname.append(j['song'][i]['songname'])
                songid.append(j['song'][i]['songid'])
                artistname.append(j['song'][i]['artistname'])
        except:
            print u'不需理会异常'
        print u'############获取列表成功##############'
        return songname,songid,artistname
#------------下载函数-------------
    def down_music(self, url ,songname):
        print u'开始下载......'
        urllib.urlretrieve(url, songname+'.mp3')
        print u'下载完成,已保持到当前目录下'
#-------------获取下载url地址----------

#----------------运行---------------------
Music = Baidu_Music()
songname,songid,artistname = Music.input_songname()
for i in range(0,len(songname)):
    print str(i+1)+'. '+songname[i] + '--' + artistname[i]+'  id: '+songid[i]
#输入音乐编号
print u'输入音乐编号,进行下载'
song_num = raw_input()


