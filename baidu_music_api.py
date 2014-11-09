﻿#coding=utf-8
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
    print u'*1.新歌榜'
    print u'*2.热歌榜'
    print u'*3.搜索音乐'
#---------初始化公共参数---------
    def __init__(self):
        self.val = {'from': 'webapp_music',
                    'format': 'json',
                    'callback': '',
                    '_': int(time.time()),
                    '_t' : int(time.time()),
                    'method': 'baidu.ting.search.catalogSug',
                    }
#定义HEADER
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.header = {'User-Agent': user_agent}
#--------------获取搜索音乐JSON------------------
    def Input_SongName(self):
        query = raw_input(u'请输入要搜索的音乐')
        self.val['query'] = query
        self.val['size'] = '1'
#API_URL,处理URL参数
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting'
        url_values = urllib.urlencode(self.val)
#发送REQUEST请求
        req = urllib2.Request(url, url_values, self.header)
#得到RESPONSE响应
        response = urllib2.urlopen(req,timeout=10) #10秒后timeout
        jsons = response.read()
###################处理JSON#################
#加载JSON数据
        j = json.loads(jsons)
        songname=[]
        songid=[]
        artistname=[]
        try:
            for i in range(0,10):
                #用 双list 存储 歌名与id
                songname.append(j['song'][i]['songname'])
                songid.append(j['song'][i]['songid'])
                artistname.append(j['song'][i]['artistname'])
        except:
            print u'列表越界,最多显示10个'
        print u'############获取列表成功##############'
        return songname,songid,artistname
#----------获取新歌榜单JSON-------
    def Get_New_Music(self):
        self.val['method'] = 'baidu.ting.billboard.billList'
        self.val['callback'] = '__.cb_list'
        self.val['size'] = '50'
        self.val['type'] = '1'
#API_URL,处理URL参数
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting'
        url_values = urllib.urlencode(self.val)
#发送REQUEST请求
        req = urllib2.Request(url, url_values, self.header)
#得到RESPONSE响应
        response = urllib2.urlopen(req,timeout=10) #10秒后timeout
        jsons = response.read()
        jsons = jsons.replace('/**/__.cb_list(','')
        jsons = jsons.replace('});','}')
        jsons = jsons.replace('\/','')
###################处理JSON#################
#加载JSON数据
        j = json.loads(jsons)
        songname=[]
        songid=[]
        artistname=[]
        try:
            for i in range(50):
                songid.append(j['song_list'][i]['song_id'])
                songname.append(j['song_list'][i]['title'])
                artistname.append(j['song_list'][i]['author'])
        except:
            print u'获取下载地址失败'
        return songname,songid,artistname
#------------下载函数-------------
    def Down_Music(self, song_url ,song_name, formats):
        print u'开始下载......'
        urllib.urlretrieve(song_url, song_name+'.'+formats)
        print u'下载完成,已保持到当前目录下'
#-------------获取下载url地址-------------
    def Get_MusicUrl(self, song_num):
        self.val['callback'] = '__.cb_download'
        self.val['rate']='320'
        self.val['songIds'] = song_num
        self.val['type'] = 'flac,mp3'
#API_URL,处理URL参数
        url = 'http://music.baidu.com/data/music/fmlink'
        url_values = urllib.urlencode(self.val)
#发送REQUEST请求
        req = urllib2.Request(url, url_values, self.header)
#得到RESPONSE响应
        response = urllib2.urlopen(req,timeout=10) #10秒后timeout
        jsons = response.read()
        jsons = jsons.replace('__cb_download(','')
        jsons = jsons.replace('}]}})','}]}}')
        jsons = jsons.replace('\/','')
###################处理JSON#################
#加载JSON数据
        j = json.loads(jsons)
        try:    
            songLinks =  j['data']['songList'][0]['songLink']
            formats = j['data']['songList'][0]['format']
        except:
            print u'获取下载地址失败'
        return songLinks,formats
#----------------运行---------------------
Music = Baidu_Music()
while 1:
    no = raw_input(u'输入功能编号')
    no = int(no)
    if no ==1:
        songname,songid,artistname = Music.Get_New_Music()
        for i in range(0,len(songname)):
            print str(i+1)+'. '+songname[i] + '--' + artistname[i]
        #输入音乐编号
        print u'#####################################'
        song_num = raw_input(u'输入音乐编号,进行下载')
        song_name = songname[int(song_num)-1] 
        song_num = songid[int(song_num)-1]
        songLink, formats = Music.Get_MusicUrl(song_num)
        Music.Down_Music(songLink, song_name, formats)
        break
    elif no ==2:
        print 'this is 2'
        break
    elif no ==3:
        songname,songid,artistname = Music.Input_SongName()
        for i in range(0,len(songname)):
            print str(i+1)+'. '+songname[i] + '--' + artistname[i]
        #输入音乐编号
        print u'#####################################'
        song_num = raw_input(u'输入音乐编号,进行下载')
        song_name = songname[int(song_num)-1] 
        song_num = songid[int(song_num)-1]
        songLink, formats = Music.Get_MusicUrl(song_num)
        Music.Down_Music(songLink, song_name, formats)
        break
    else:
        no = raw_input(u'输入错误请重新输入')