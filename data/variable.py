
# -*- coding:utf-8 -*-

url = "http://demo"
auth=('111','111')
headers = {'content-type': "text/xml","Accept":'application/xml'}


# 01-得到获取用户信息
GET_CUSTOMERINFO_list=[
('1','1','1'),('1','1','1'),('1','1','1'),('1','1','1'),
('1','1','1'),('1','20','1'),('','20','1'),
('1','','1'),('1','20','1'),('1','20','1'),('1','20','1'),]
GET_CUSTOMERINFO_DATA='''<soapenv:Envelope xmlns:soapenv="http://demo">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:MT_GET_CUSTOMERINFO_REQ>
         <!--Optional:-->
         <VKORG>%s</VKORG>
         <!--Optional:-->
         <VTWEG>%s</VTWEG>
         <!--Zero or more repetitions:-->
         <ITEM>
            <!--Optional:-->
            <KUNNR>%s</KUNNR>
         </ITEM>
      </urn:MT_GET_CUSTOMERINFO_REQ>
   </soapenv:Body>
</soapenv:Envelope>'''
