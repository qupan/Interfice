# _*_ coding:utf-8 _*_
from base import *

class GetCustomerInfo(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.session=requests.session()

	# @unittest.skip('Debug pass')
	def test_001_get_eu_info(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[0]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertNotIn('<status>E</status>', resp.text)
		self.assertEqual(200, resp.status_code)

	# @unittest.skip('Debug pass')
	def test_002_get_in_info(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[1]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertNotIn('<status>E</status>', resp.text)

	# @unittest.skip('Debug pass')
	def test_003_get_na_info(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[2]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertNotIn('<status>E</status>', resp.text)

	# @unittest.skip('Debug pass')
	def test_004_get_it_info(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[3]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertNotIn('<status>E</status>', resp.text)

	# @unittest.skip('Debug pass')
	def test_005_vkorg_vtweg_long_input(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[4]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertNotIn('<status>E</status>', resp.text)

	# @unittest.skip('Debug pass')
	def test_006_kunnr_long_input(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[5]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertIn('<status>E</status>', resp.text)

	# @unittest.skip('Debug pass')
	def test_007_vkorg_null(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[6]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertIn('Sales organization or distribution channel cannot be empty', resp.text)

	# @unittest.skip('Debug pass')
	def test_008_vtweg_null(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[7]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertIn('Sales organization or distribution channel cannot be empty', resp.text)

	# @unittest.skip('Debug pass')
	def test_009_kunnr_null(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[8]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertIn('ns0:MT_GET_CUSTOMERINFO_RESP', resp.text)
		self.assertEqual(200, resp.status_code)

	# @unittest.skip('Debug pass')
	def test_010_not_exist_user(self):
		data=GET_CUSTOMERINFO_DATA%GET_CUSTOMERINFO_list[9]
		resp=self.session.post(url, auth=auth,data=data, headers=headers)
		self.assertIn('ns0:MT_GET_CUSTOMERINFO_RESP', resp.text)
		self.assertEqual(200, resp.status_code)

	@classmethod
	def tearDownClass(cls):
		cls.session.close()

if __name__=="__main__":
	unittest.main()
