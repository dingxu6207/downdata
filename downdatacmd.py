# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:17:16 2019

@author: dingxu
"""
import os

'''
listroute = [0 for i in range(22)]
#listroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201122/AutoFlat20201122/'
listpath = [0 for i in range(22)]
#listpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201122\\flat20201122\\'
  
for i in range(22):
    listroute[i] = 'https://nadc.china-vo.org/psp/csp/2020CSP/202012'+str(10+i)+'/AutoFlat202012'+str(10+i)+'/'
    
for i in range(22):
    listpath[i] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\202012'+str(10+i)+'\\flat202012'+str(10+i)+'\\'
    
for i in range(22):
    cmd = 'python downdata.py'+' '+listroute[i]+' '+listpath[i]
    os.system(cmd)
'''    
    
    
dlistroute = [0 for i in range(22)]
#listroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201122/AutoFlat20201122/'
#dlistroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201223/CSP-VAR-0645/'
dlistpath = [0 for i in range(22)]
#dlistpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201223\\CSP-VAR-0645\\'
 

for i in range(22):
    dlistroute[i] = 'https://nadc.china-vo.org/psp/csp/2020CSP/202012'+str(22+i)+'/CSP-VAR-0645'+'/'
    
for i in range(22):
    dlistpath[i] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\202012'+str(22+i)+'\\CSP-VAR-0645'+'\\'

   
for i in range(12):
    cmd = 'python downdata.py'+' '+dlistroute[i]+' '+dlistpath[i]
    os.system(cmd)