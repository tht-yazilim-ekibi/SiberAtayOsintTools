from colorama import Fore, init
import requests
import json
import sys


init(autoreset=True)

reset = Fore.RESET
blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN

def getİpİnformations(ip: str) -> str:

    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    r = requests.get(f'http://ip-api.com/json/{ip}',headers=header)
    jsondict = json.loads(r.text)
    if jsondict["status"] == "fail":
        print(red+"Process Resulted in an Error")
        sys.exit()
    else:
        print(f"""
------------
[-] İşlem: {jsondict["status"]}
[-] Ülke: {jsondict["country"]}
[-] Ülke Kodu: {jsondict["countryCode"]}
[-] Bölge: {jsondict["region"]}
[-] Bölge Adı: {jsondict["regionName"]}
[-] Şehir: {jsondict["city"]}
[-] Zip: {jsondict["zip"]}
[-] lat: {jsondict["lat"]}
[-] lon: {jsondict["lon"]}
[-] Saat Dilimi: {jsondict["timezone"]}
[-] isp: {jsondict["isp"]}
[-] Organizasyon: {jsondict["org"]}
[-] İp: {jsondict["query"]}
------------
""")


if __name__ == "__main__":
    print(blue+r"""
    __       _______          ______    ________  __    _____  ___  ___________  
    |" \     |   __ "\        /    " \  /"       )|" \  (\"   \|"  \("     _   ") 
    ||  |    (. |__) :)      // ____  \(:   \___/ ||  | |.\\   \    |)__/  \\__/  
    |:  |    |:  ____/      /  /    ) :)\___  \   |:  | |: \.   \\  |   \\_ /     
    |.  |    (|  /         (: (____/ //  __/  \\  |.  | |.  \    \. |   |.  |     
    /\  |\  /|__/ \         \        /  /" \   :) /\  |\|    \    \ |   \:  |     
    (__\_|_)(_______)         \"_____/  (_______/ (__\_|_)\___|\____\)    \__|     
                                                                                    
                    [-] Athena Osint Tools - Ar-Ge [-]
                        #Author : @MuhammedTr768
        
    """)
    print(f"{green}[ ? ] {reset} İp adresini girin :  ", end="")
    ip_address = str(input())
    getİpİnformations(ip=ip_address)