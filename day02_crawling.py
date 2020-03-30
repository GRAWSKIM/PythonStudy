#File > Settings > Project interpreter > '+' > Library 설피
#python https 통신 library
import requests
#html 파싱 Library
from bs4 import BeautifulSoup

def crawler(url):
    """
    html 소스를 가져온다
    :return: void
    """
    src = requests.get(url)
    return src

html = crawler('https://finance.naver.com/item/main.nhn?code=005180')
soup = BeautifulSoup(html.content,'html.parser')

soup.select('.chart')

#웹페이지 만들기