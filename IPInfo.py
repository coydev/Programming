import requests
import json
ip = input("[-->] ")  # Get ip the user wants to scrape
banner = "[+]" + "-" * 25 + "[+]"

def get_info(ip):
    url = "https://ipinfo.io/" + ip  # Make a request to the Ipinfo api
    
    r = requests.get(url)  # Return the json
    info = json.loads(r.text)  # parse output from the web api
    
    print(banner + "\n")
    print("[+]" + "IP: " + info["ip"])
    print("[+]" + "Region: " + info["region"])
    print("[+]" + "City: " + info["city"] + "\n")
    print(banner)
    return 

def main(ip):
    get_info(ip)
main(ip)
