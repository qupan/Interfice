import pytest,requests

@pytest.fixture(scope='session')
def s():
	session=requests.session()

	yield session
	session.close()
