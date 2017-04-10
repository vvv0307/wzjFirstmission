# -*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import itertools
import re
import sys
import pymysql.cursors

value = input("请输入一个日期（格式:xxxx-xx/xx）:")
s = re.findall('[0-9]+',value)
date = ''.join(s)
for i in range(1,25):
    if i<10:
        num = "0"+str(i)
    else:
        num = str(i)

    url = "http://paper.people.com.cn/rmrb/html/"+value+"/nbs.D110000renmrb_"+num+".htm"
    # print(url)
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,"html.parser")
    content = soup.find_all('area')
    # newsUrl = "http://paper.people.com.cn/rmrb/html/2017-03/30/"+content[0].get('href')
    # res = requests.get(newsUrl)
    # res.encoding = 'utf-8'
    # soup = BeautifulSoup(res.text,"html.parser")
    # content = soup.find("div",id="articleContent")
    # print(content)
    for j in range(len(content)):
        # print(type(i))
        newsUrl = "http://paper.people.com.cn/rmrb/html/"+value+"/"+content[j].get('href')
        res = requests.get(newsUrl)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,"html.parser")
        title = soup.find("title")
        time = soup.find("div",id="riqi_")
        articleContent = soup.find("div", id="articleContent").findAll('p')
        newsTitle = ""
        newsTitle = newsTitle.join(itertools.chain(*title))
        newsTime = ""
        newsTime = newsTime.join(itertools.chain(*time))
        newsContent = ""
        newsContent = newsContent.join(itertools.chain(*articleContent))
        # news = newsTitle+'\n'+newsTime+'\n'+newsContent
        # print(news)
        conn = pymysql.Connect(host='localhost',user='root',password='zht1741105',db='news',charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO news(page,date,title,time,content) VALUES('%d','%s','%s','%s','%s');" %(i,date,newsTitle,newsTime,newsContent)
        cursor.execute(sql)
        cursor.close()
        conn.close()
print("end")

