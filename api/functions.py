##############################
###   KENA MOBILE WORKER   ###
###      By @Matt0550      ###
##############################

import requests
from bs4 import BeautifulSoup

class KenaMobileWorker:
    def __init__(self):
        self.url = "https://www.kenamobile.it/wp-admin/admin-ajax.php"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }
        self.timeout = 5
        self.session = requests.Session()
        self.cookies = {}

    # ! NOT WORKING YET
    def login(self, username, password):
        data = {
            'action': 'kena_set_tpc_cookie',
            'referrer': 'https://www.kenamobile.it/',
            'page': 'https://www.kenamobile.it/mykena/#/dashboard',
            'agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'campaign': 'false',
            'cookie_value': ''
        }
        response = self.session.post(self.url, headers=self.headers, data=data, timeout=self.timeout)
        print(response.text)
        self.cookies = response.cookies.get_dict()
        print(self.cookies)

        response = self.session.get("https://www.kenamobile.it/mykena/login", headers=self.headers, cookies=self.cookies, timeout=self.timeout)
        # Get sessionDataKey from hidden input
        soup = BeautifulSoup(response.text, 'html.parser')
        sessionDataKey = soup.find('input', {'name': 'sessionDataKey'}).get('value')
        print(sessionDataKey)

        data = {
            'username': username,
            'password': password,
            'sessionDataKey': sessionDataKey,
        }

        response = self.session.post("https://auth.kenamobile.it/wso2is/oauth2/authorize?sessionDataKey=" + sessionDataKey, headers=self.headers, cookies=self.cookies, timeout=self.timeout)

        
        # Pass data as form data to https://auth.kenamobile.it/wso2is/commonauth
        response = self.session.post("https://auth.kenamobile.it/wso2is/commonauth", headers=self.headers, data=data, cookies=self.cookies, timeout=self.timeout)
        print(response.text)
        
        
    
        print(self.session.cookies.get_dict())


