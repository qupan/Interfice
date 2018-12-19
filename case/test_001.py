# -*- coding:utf-8 -*-
from base import *

class TestGetCustomerInfo:
	'''接口'''

	@pytest.mark.parametrize('data,code,msg',data_01[0])
	@pytest.mark.ok
	def test_01(self,s,data,code,msg):
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert code == resp.status_code
		assert msg  not in resp.text

	@pytest.mark.parametrize('data,code,msg',data_01[1])
	@pytest.mark.ok
	def test_02(self,s,data,code,msg):
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert code == resp.status_code
		assert msg in resp.text

	@pytest.mark.parametrize('data,code,msg',data_01[2])
	@pytest.mark.ok
	def test_03(self,s,data,code,msg):
		'''处理特殊逻辑'''
		resp=s.post(url, auth=auth,data=data, headers=headers)
		shipto=re.findall(r'<SHIPTO_ID>(.*?)</SHIPTO_ID>', resp.text, re.S|re.M)[0]
		assert 560000 <= int(shipto) <= 5999999
		assert msg  not in resp.text

if __name__=='__main__':
	pytest.main(['-q','-m','ok','test_01GetCustomerInfo.py',])
