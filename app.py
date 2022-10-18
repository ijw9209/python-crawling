#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 이 url에서 response라는 곳으로 담는다.
# response = urlopen('https://en.wikipedia.org/wiki/Main_Page') 과 같은 내용이다.
with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
    #response를 soup 변수에 넣겠다.
    soup = BeautifulSoup(response, 'html.parser')
    #for문이다. find_all <a>태그의 주소를 가져와서 출력해준다.
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))