'''
Created on 2018年4月26日

@author: bomber
'''
from urllib import request
from urllib.request import ProxyHandler, HTTPSHandler, HTTPRedirectHandler, \
    HTTPCookieProcessor
import urllib
from http import cookiejar

class UrlManager(object):
    def __init__(self):
        self._new_urls=set()
        self._old_urls=set()
    
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self._new_urls and url not in self._old_urls:
            self._new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):
        return len(self._new_urls)!=0

    
    def get_new_url(self):
        new_url=self._new_urls.pop()
        self._old_urls.add(new_url)
        return new_url

# def urlmanage1(url):
#     with request.urlopen('http://www.baidu.com') as resp:
#         print(resp.getcode())
#         cont = resp.read()
#     return cont
# 
#     
# def urlmanage2(url):
#     req = request.Request(url)
#     data = bytes(urllib.parse.urlencode({'a':'1'}),encoding='utf-8')
#     req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
#     with request.urlopen(req,data=data) as resp:
#         cont = resp.read()
#     return cont
# 
# 
# def urlmanage3(url):
# #     HTTPCookieProcessor
# #     ProxyHandler
# #     HTTPSHandler
# #     HTTPRedirectHandler
#     cj = cookiejar.CookieJar()
# 
#     handler = HTTPCookieProcessor(cj)
#     opener = request.build_opener(handler)
#     request.install_opener(opener)
#     
#     req = request.Request(url)
#     data = bytes(urllib.parse.urlencode({'a':'1'}),encoding='utf-8')
#     req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
#     with request.urlopen(req,data) as resp:
#         print(cj)
#         cont = resp.read()
#     return cont
# 
# if __name__=='__main__':
#     url='http://www.baidu.com/'
#     
#     print('第一种方法')
#     print(len(urlmanage1(url)))
#     
#     print('第二种方法')
#     print(len(urlmanage2(url)))
#     
#     print('第三种方法')
#     print(len(urlmanage3(url)))
