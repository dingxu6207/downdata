# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:17:16 2019

@author: dingxu
"""
import os
listroute = [0 for i in range(10)]
#listroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201122/AutoFlat20201122/'
listpath = [0 for i in range(10)]
#listpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201122\\flat20201122\\'
  
for i in range(10):
    listroute[i] = 'https://nadc.china-vo.org/psp/csp/2020CSP/202011'+str(22+i)+'/AutoFlat202011'+str(22+i)+'/'
    
for i in range(10):
    listpath[i] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\202011'+str(22+i)+'\\flat202011'+str(22+i)+'\\'
    
for i in range(10):
    cmd = 'python downdata.py'+' '+listroute[i]+' '+listpath[i]
    os.system(cmd)
    
    
    
dlistroute = [0 for i in range(10)]
#listroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201122/AutoFlat20201122/'
dlistpath = [0 for i in range(10)]
#listpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201122\\flat20201122\\'
  
for i in range(10):
    dlistroute[i] = 'https://nadc.china-vo.org/psp/csp/2020CSP/202011'+str(22+i)+'/CSP-VAR-0645'+'/'
    
for i in range(10):
    dlistpath[i] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\202011'+str(22+i)+'\\CSP-VAR-0645'+'\\'
    
for i in range(10):
    cmd = 'python downdata.py'+' '+dlistroute[i]+' '+dlistpath[i]
    os.system(cmd)