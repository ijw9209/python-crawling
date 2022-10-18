#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 이 url에서 response라는 곳으로 담는다.
# 자신이 크롤링할 url로 변경해준다. 나는 네이버 뉴스로 url을 변경해주었다.
with urlopen('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100') as response:
    f = open("C:/workspace/crawling/새파일.txt", 'w', encoding="UTF-8")
    i = 1   
    soup = BeautifulSoup(response, 'html.parser')
    #이부분을 네이버 헤드라인 타이틀 클래스인 .cluster_text_headline 으로 바꾸어준다.
    for anchor in soup.select('a.cluster_text_headline'):
        data = str(i) + " : " + anchor.get_text() + "\n"
        i = i + 1
        f.write(data)
f.close()
    