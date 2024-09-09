##############################
###   KENA MOBILE WORKER   ###
###      By @Matt0550      ###
##############################

import requests
from bs4 import BeautifulSoup
from models import CustomerDTO, UserCreditInfo, PromoModel

class KenaMobileWorker:
    def __init__(self):
        self.url = "https://www.kenamobile.it/wp-admin/admin-ajax.php"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }
        self.timeout = 5
        self.session = requests.Session()
        self.cookies = {}

    def setPhpSession(self, PHPSESSID):
        self.cookies["PHPSESSID"] = PHPSESSID
    
    def getCustomerDTO(self, phoneNumber):
        # Check if PHPSESSID is set
        if "PHPSESSID" not in self.cookies:
            return {"error": "PHPSESSID not set"}
        
        data = {
            "action": "mykena_apigtw",
            "apigtw_action": "getCustomerByMsisdn",
            "msisdn": phoneNumber,
            "nonce": "c000fcaaaa"
        }

        response = self.session.post(self.url, headers=self.headers, cookies=self.cookies, data=data, timeout=self.timeout)

        if response.status_code == 200:
            data = response.json()
            if data["success"] == True:
                return CustomerDTO(**data["data"]["data"]["customerDTO"])
            else:
                return {"error": data["message"]}
        else:
            return {"error": "Request failed"}
        
    def getUserCreditInfo(self, phoneNumber):
        # Check if PHPSESSID is set
        if "PHPSESSID" not in self.cookies:
            return {"error": "PHPSESSID not set"}
        
        data = {
            "action": "mykena_apigtw",
            "apigtw_action": "getCreditInfo",
            "msisdn": phoneNumber,
            "nonce": "c000fcaaaa"
        }

        response = self.session.post(self.url, headers=self.headers, cookies=self.cookies, data=data, timeout=self.timeout)

        if response.status_code == 200:
            data = response.json()
            if data["success"] == True:
                return UserCreditInfo(**data["data"]["data"])
            else:
                return {"error": data["message"]}
        else:
            return {"error": "Request failed"}
        
    def getUserPromo(self, phoneNumber):
        # Check if PHPSESSID is set
        if "PHPSESSID" not in self.cookies:
            return {"error": "PHPSESSID not set"}
        
        data = {
            "action": "mykena_apigtw",
            "apigtw_action": "getLastPromoUser",
            "msisdn": phoneNumber,
            "nonce": "c000fcaaaa"
        }

        response = self.session.post(self.url, headers=self.headers, cookies=self.cookies, data=data, timeout=self.timeout)

        if response.status_code == 200:
            data = response.json()
            if data["success"] == True:
                # List of promos
                promos = []
                for promo in data["data"]["data"]:
                    promos.append(PromoModel(**promo))

                return promos
            else:
                return {"error": data["message"]}
        else:
            return {"error": "Request failed"}
