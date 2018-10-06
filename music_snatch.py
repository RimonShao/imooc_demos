#-*- coding:utf-8 -*-
import requests
import json
import re

#爬取网易云音乐的歌词
def download_by_music_id(music_id):
	irc_url = 'http://music.163.com/api/song/lyric?' + 'id='+str(music_id)+'&lv=1&kv=1&tv=-1'
	r = requests.get(irc_url)
	#print(r.text)
	json_obj = r.text
	j=json.loads(json_obj)

	lrc = j['lrc']['lyric']   #获取歌词，此时含有时间

	#对字符串进行处理：去掉[]里面的东西，只剩文字
	pat = re.compile(r'\[.*\]')  #生成正则表达式
	lrc = re.sub(pat,"",lrc) #移除与pat匹配的字符
	lrc = lrc.strip()  #移除字符串头尾指定的字符
	return lrc

#将字符串保存到文件中
def save_to_file(filename,contents):
	try:
		fh= open(filename,'w',encoding="utf-8")
		fh.write(contents) 
		fh.close()
	except IOError:
		print("fail to open file!")
music_content = download_by_music_id(36024838)
# print(music_content) //内容为str类型
save_to_file(str(36024838)+'.txt',music_content)