
from shodan import Shodan
from json import loads
from colorama import Fore, init
import requests

init(autoreset=True)

class ShodanOsint(object):
    def __init__(self) -> None:
        
        self.shodan = Shodan(key=self.returnShodanApiKey())

    def returnShodanApiKey(self) -> str:
        return (loads(open("apis.json", "r").read())["shodan_api_key"])


    def ipQuery(self, ip_host: str=None):
        
        self.host = self.shodan.host(ips=ip_host)["data"]
        for ip_data in self.host:
            
            org = (ip_data["org"])
            transport = ip_data["transport"]
            asn = ip_data["asn"]
            domains = ip_data["domains"]
            ip_str = ip_data["ip_str"]
            city = ip_data["location"]["city"]
            region_code = ip_data["location"]["region_code"]
            area_code = ip_data["location"]["area_code"]
            longitude = ip_data["location"]["longitude"]
            country_name  = ip_data["location"]["country_name"]
            country_code = ip_data["location"]["country_code"]
            latitude = ip_data["location"]["latitude"]

        print(f"""
) Asn               ==> {asn}
) Trasnport         ==> {transport}
) Org               ==> {org}
) City              ==> {city}
) Region Code       ==> {region_code}
) Area Code         ==> {area_code}
) Longitude         ==> {longitude}
) Country Name      ==> {country_name}
) Country Code      ==> {country_code}
) Latitude          ==> {latitude}
) Domains           ==> {domains}
) İp Address        ==> {ip_str}
    """)



    def domainGetIpAddress(self, domain:str = None) -> str:
        return requests.get(url=f"https://api.shodan.io/dns/resolve?hostnames={domain}&key={self.returnShodanApiKey()}").json()
        

    def ipGetDomain(self, ipAddress: str = None) -> str: 
        return requests.get(url=f"https://api.shodan.io/dns/reverse?ips={ipAddress}&key={self.returnShodanApiKey()}").json()


    def myİpAddress(self) -> str:
        return requests.get(url=f"https://api.shodan.io/tools/myip?key={self.returnShodanApiKey()}").json()

    def exit(self):
        print("Çıkış yapılıyor ... ")
        __import__("time").sleep(1)
        exit(0)

    def bannerShodan(self):
        
        print(Fore.LIGHTBLUE_EX+f"""

   _    ___    _                 _                _   
 /'_`\ (  _`\ ( )               ( )             /'_`\ 
(_) ) || (_(_)| |__     _      _| |   _ _   ___(_) ) |
   /'/'`\__ \ |  _ `\ /'_`\  /'_` | /'_` )/' _ `\ /'/'
  |_|  ( )_) || | | |( (_) )( (_| |( (_| || ( ) ||_|  
  (_)  `\____)(_) (_)`\___/'`\__,_)`\__,_)(_) (_)(_)  

                #Author : @Nemesis

\t[0] Çıkış
\t[1] İp Sorgulama\t[3] İp'den domain bul
\t[2] Domain'den ip bul\t[4] İp adresim



""")

        self.queryUser = str(input("[ ? ] Seçiminizi giriniz : "))

        if self.queryUser == "0":
            self.exit()

        if self.queryUser == "1":
            self.ipUser = str(input("\n||| - ||| İp adresini giriniz : "))
            self.ipQuery(ip_host=self.ipUser)

        if self.queryUser == "2":
            self.domain = str(input("\n||| - ||| Domain adresini giriniz : "))
            print(self.domainGetIpAddress(domain=self.domain))

        if self.queryUser == "3":
            self.ip_ = str(input("||| - ||| İp adresini girin : "))
            print(self.ipGetDomain(ipAddress=self.ip_))
        
        if self.queryUser == "4":
            print("İp adresiniz ", self.myİpAddress())


if __name__ == "__main__":
    shodanAPi = ShodanOsint()
    shodanAPi.bannerShodan()