# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:08:32 2021

@author: dingxu
"""

import os


listroute = [0 for i in range(22)]
#https://nadc.china-vo.org/psp/csp/calibration/dark/-35c/20200204/
#listroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201122/AutoFlat20201122/'
listroute[0] = 'https://nadc.china-vo.org/psp/csp/calibration/dark/-40c/20201224/'
listroute[1] = 'https://nadc.china-vo.org/psp/csp/calibration/dark/-40c/20201202/'
listroute[2] = 'https://nadc.china-vo.org/psp/csp/calibration/dark/-35c/20200204/'

listpath = [0 for i in range(22)]
#listpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201122\\flat20201122\\'
listpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\calibration\\dark\\-40c\\20201224\\'
listpath[1] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\calibration\\dark\\-40c\\20201202\\'  
listpath[2] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\calibration\\dark\\-35c\\20200204\\' 

#for i in range(22):
#    listroute[i] = 'https://nadc.china-vo.org/psp/csp/2020CSP/202012'+str(10+i)+'/AutoFlat202012'+str(10+i)+'/'
#    
#for i in range(22):
#    listpath[i] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\202012'+str(10+i)+'\\flat202012'+str(10+i)+'\\'
#    
for i in range(3):
    cmd = 'python downbias.py'+' '+listroute[i]+' '+listpath[i]
    os.system(cmd)
   
    
    
#dlistroute = [0 for i in range(22)]
##listroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201122/AutoFlat20201122/'
##dlistroute[0] = 'https://nadc.china-vo.org/psp/csp/2020CSP/20201223/CSP-VAR-0645/'
#dlistpath = [0 for i in range(22)]
##dlistpath[0] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\20201223\\CSP-VAR-0645\\'
# 
#
#for i in range(22):
#    dlistroute[i] = 'https://nadc.china-vo.org/psp/csp/2020CSP/202012'+str(22+i)+'/CSP-VAR-0645'+'/'
#    
#for i in range(22):
#    dlistpath[i] = 'E:\\shunbianyuan\\data\\xingmingdata\\downdata\\202012'+str(22+i)+'\\CSP-VAR-0645'+'\\'
#
#   
#for i in range(12):
#    cmd = 'python downdata.py'+' '+dlistroute[i]+' '+dlistpath[i]
#    os.system(cmd)
    
    
    