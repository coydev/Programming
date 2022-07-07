import requests
from bs4 import BeautifulSoup
import sys
import time

username = input("Who ya looking for?: ")

twit = {
    'Platform':'Twitter', 
    'link':f'https://twitter.com/{username}',
}

found = f"[!] {twit['Platform']} account found for {username}\n [+] Located here: https://twitter.com/{username}"

def main():
    
    acc_link = twit['link']

    headers = {
    'user-agent':'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
}
    r = requests.get(twit['link'], headers=headers)
    page = r.text
    soup = BeautifulSoup(page,'html.parser')

    if soup.title.text == "Twitter / Account Suspended":
        print(f"[!] Account suspended [!]\n [-->] {acc_link}")
        time.sleep(5)
        sys.exit()
    if soup.title.text == "Twitter / ?":
        print(f"[!] Page does not exist")
        time.sleep(5)
        sys.exit()
    else:
        print(found)

main()
