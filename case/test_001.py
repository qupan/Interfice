# -*- coding:utf-8 -*-
from base import *

class TestGetCustomerInfo:

	@pytest.mark.ok
	def test_01(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[0]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert '<status>E</status>' not in resp.text

	@pytest.mark.ok
	def test_002_get_in_info(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[1]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert '<status>E</status>' not in resp.text

	@pytest.mark.ok
	def test_003_get_na_info(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[2]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert '<status>E</status>' not in resp.text

	@pytest.mark.ok
	def test_004_get_it_info(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[3]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert '<status>E</status>' not in resp.text

	@pytest.mark.ok
	def test_005_vkorg_vtweg_long_input(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[4]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert '<status>E</status>' not in resp.text

	@pytest.mark.ok
	def test_006_kunnr_long_input(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[5]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert '<status>E</status>' in resp.text

	@pytest.mark.ok
	def test_007_vkorg_null(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[6]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert 'Sales organization or distribution channel cannot be empty' in resp.text

	@pytest.mark.ok
	def test_008_vtweg_null(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[7]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert 'Sales organization or distribution channel cannot be empty' in resp.text

	@pytest.mark.ok
	def test_009_kunnr_null(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[8]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert 'ns0:MT_GET_CUSTOMERINFO_RESP' in resp.text

	@pytest.mark.ok
	def test_010_not_exist_user(self,s):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[9]
		resp=s.post(url, auth=auth,data=data, headers=headers)
		assert 200 == resp.status_code
		assert 'ns0:MT_GET_CUSTOMERINFO_RESP' in resp.text

if __name__=='__main__':
	pytest.main(['-v','-m','ok','test_001.py',])
