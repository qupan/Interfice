# -*- coding:utf-8 -*-
import xlrd
from pathlib import Path
import sys,requests,time
import pytest
addr=Path(str(Path().cwd()).split('Interfice')[0])/'Interfice'/'data'/'msg.xlsx'
sys.path.append(str(addr))

a=xlrd.open_workbook(str(addr))
b=a.sheets()[0]
c=b.nrows
d=[]
for i in range(0,c):
  d.append(b.row_values(i))

url = d[2][0]
auth=(d[2][1],d[2][2])
headers = {'content-type': "text/xml","Accept":'application/xml'}
code=[200,500,404] #返回码信息

# 01-得到获取用户信息接口
msg_01=['<status>E</status>','Sales organization or distribution channel cannot be empty',
         'ns0:MT_GET_CUSTOMERINFO_RESP']
data_01=[[(d[20][1]%(d[5][1],d[7][1],d[9][1]),code[0],msg_01[0]),
          (d[20][1]%(d[5][2],d[7][2],d[9][1]),code[0],msg_01[0]),
          (d[20][1]%(d[5][2],d[7][1],d[9][1]),code[0],msg_01[0]),
          (d[20][1]%(d[5][3],d[7][1],d[9][1]),code[0],msg_01[0]),
          (d[20][1]%(d[5][3]+'123',d[7][1]+'123',d[9][1]),code[0],msg_01[0]),
          ],
         [(d[20][1]%(d[5][2],d[7][2],d[9][1]+'1234567'),code[0],msg_01[0]),
          (d[20][1]%('',d[7][2],d[9][1]),code[0],msg_01[1]),
          (d[20][1]%(d[5][2],'',d[9][1]),code[0],msg_01[1]),
          (d[20][1]%(d[5][2],d[7][2],''),code[0],msg_01[2]),
          (d[20][1]%(d[5][2],d[7][2],d[9][2]),code[0],msg_01[2]),
          ],
         [(d[20][1]%(d[5][3],d[7][2],d[9][4]),code[0],msg_01[0]),
          ],
         ]      
