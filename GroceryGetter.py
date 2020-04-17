import requests
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver


class LoadHtml:

    def __init__(self):
        self.__options = webdriver.FirefoxOptions()
        self.__options.add_argument('--ignore-certificate-errors')
        self.__options.add_argument("--test-type")
        self.__options.binary_location = sys.argv[1]
        self.__driver = webdriver.Firefox(firefox_options=self.__options)
        self.__driver.get("https://www.instacart.com")
        pass

    def deal_with_page(self):
        user = self.__driver.find_element_by_id('nextgen-authenticate.all.log_in_email')
        user.send_keys(sys.argv[2])

    def scrape_page(self):
        self.deal_with_page()
        url = 'https://www.instacart.com'
    #    url = "https://www.google.com"
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "build_sha=97ef76b51262f55819429f463e084e3a0b6c16a5; ahoy_visitor=408b3ed4-8c21-4307-a624-0fbf002f7f0b; ahoy_visit=a85a7084-0a20-47ee-8462-6b8c496c1969; _instacart_session=VmV3ZEpsdEsrNHRBYUh4TzJWMEZEOTd1bzhkekNvcUw0OHFPQlRUZVRPS0xvdFNsRU81TUlWWVo0N1pSb1Z2Yit2bEt0OXVGOERqTnNtWGxQYkVvWDFCZk5FalZBTGVmcEJnYTI5ZmpqUlI1QVNnVWFRUTlPZDdrVlg5OWg0cmM4RlVGaWVCeGVxRS9qU0EwZnhRRnorR3NFeGdyQTJVTTIvWlkwQmRMOHFBcWN4V1hzbHIwRGJ6alpCb1Njd1huVE00dUNYa3FLVWlLQXd0QnlXdU1mUy9LNjQyb1hydEtVR01EejJKWS9Ob1BEaEUvcUpKc0cwK01sMm5Zdld0MS0tcGwvZExTYkVuc0htNzE3VlZ3VzAxdz09--612e390766190c176d0b059cf000274ea7d6598a; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%223ea42bf7-e232-4803-9fff-0315f5059010%22; amplitude_idundefinedinstacart.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; amplitude_id_b87e0e586f364c2c189272540d489b01instacart.com=eyJkZXZpY2VJZCI6ImFlZWVhZmYxLTA0MzUtNDQ0ZS1hYjhmLWU2NmMyNjBmZjA5ZlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4NzA5MjI1MTA3NywibGFzdEV2ZW50VGltZSI6MTU4NzA5MjQyMzE2MywiZXZlbnRJZCI6OCwiaWRlbnRpZnlJZCI6NCwic2VxdWVuY2VOdW1iZXIiOjEyfQ==; _gcl_au=1.1.1401813578.1587092252; _fbp=fb.1.1587092253182.1471469588; _uetsid=_uet19cefabc-d632-4815-9824-8c604f0f0a9f",
            "Host": "www.instacart.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        inputEmail = soup.find('input', {"id": "nextgen-authenticate.all.log_in_email"})


if __name__ == "__main__":
    html = LoadHtml()
    html.scrape_page()