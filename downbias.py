# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 20:41:53 2019

@author: dingxu
"""

import urllib.request
import re
import os
import sys

downroute = sys.argv[1]

#downroute = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201223/CSP-VAR-0645/'
# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.fit)'
    #reg = r'(?:href|HREF)="?((?:https://)?.+?\.fts)'
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('gb2312'))
    return(url_lst)

def getFile(url):
    file_name = url.split('/')[-1]
    #print(file_name)
    u = urllib.request.urlopen(url)
    #print(u.read()) 
    
    f = open(file_name, 'wb')
    #print(u)
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)

raw_url = downroute
root_url = raw_url
#root_url = downroute.split('index')[0]
html = getHtml(raw_url)
url_lst = getUrl(html)

#downpath = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201223\\CSP-VAR-0645\\'
downpath = sys.argv[2]
os.chdir(downpath)

for url in url_lst[:]:
    url = root_url + url
    print(url)
    try:
        getFile(url)
    except:
        continue

