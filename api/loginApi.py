'''
   ip = 'http://121.42.15.146:9090'
    headers = {'X-Requested-With':'XMLHttpRequest'}

    @pytest.mark.parametrize("accouts,pwd,exp", data_li,ids=ids)
    def test_login(self,accouts, pwd, exp):
        url_login = self.ip + '/mtx/index.php?s=/index/user/login.html'
'''
from config import IP,HEADERS
import requests
class MtxLogin(object):
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'

    def login(self, session, data):
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login