import os

from lxml import etree

import requests

from tests import ADMIN_USER, PASSWORD, TEST_RESULTS


class Api:
    def __init__(self):
        self.sess = requests.Session()
        self.sess.headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +
                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    def get_login_page(self):
        response = self.sess.get(url='http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        self.csrf_token = self._get_token_etree(response.text)
        return response

    def authenticate(self, username=ADMIN_USER, password=PASSWORD):
        data = {
            '_csrf_token': self.csrf_token,
            'txtUsername': username,
            'txtPassword': password,
            'Submit': 'LOGIN'
        }

        return self.sess.post(
            url='http://hrm-online.portnov.com/symfony/web/index.php/auth/validateCredentials',
            headers={'Content-Type':'application/x-www-form-urlencoded'},
            data=data
        )

    def _get_token_etree(self, source, token_id='csrf_token'):
        doc = etree.HTML(source)
        return doc.xpath(f"//input[@id='{token_id}']")[0].attrib.get('value')

    def write_to_file(self, source):
        file = open(os.path.join(TEST_RESULTS, 'request_response.html'), 'w')
        file.write(source)
        file.close()



# -------------------------------------------

# TO USE THE Api class:

hrm_client = Api()
hrm_client.get_login_page()
response = hrm_client.authenticate()
hrm_client.write_to_file(response.text)
pass



# requests.get(url='https://www.google.com/search?q=apple')
# requests.get(url='https://www.google.com/search', params={'q': 'apple'})