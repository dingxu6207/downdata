# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:16:55 2021

@author: dingxu
"""

import os 


path = os.getcwd()

downpath = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\'
newpath = os.chdir(downpath)


def mkdirpath(newpathd):
    isExists = os.path.exists(newpathd)
    if not isExists:
        os.makedirs(newdir)
       
        print (downpath+' 创建成功')
    else:
        print (downpath+' 目录已存在')
    
    os.chdir(newdir)
    try:
        os.makedirs('flat'+newdir)
        os.makedirs('CSP-VAR-0645')
    except:
        print('it is ok!')
    os.chdir(downpath)

    

for i in range(12):
    newdir = '202011'+str(20+i)
    mkdirpath(newdir)
  
        
        

 
    