
from json import loads
import requests
from colorama import (Fore, init)

init(autoreset=True)

yellow = Fore.YELLOW
white = Fore.LIGHTWHITE_EX
reset = Fore.RESET

class LinkKısaltma(object):
    def __init__(self, links : str = None) -> None:
        
        self.links = links

        self.header = {
            "Authorization": f"Bearer {self.returnToken()}",
            "Content-Type": "application/json"
        }
        self.params = {
            "long_url": str(self.links)
        }
    
    def returnToken(self):
        return loads(open("apis.json", mode="r", encoding="utf-8").read())["link_kisaltma"]

    def sendRequests(self) -> str:
        return requests.post("https://api-ssl.bitly.com/v4/shorten", json=self.params, headers=self.header).json()

    def parseData(self):
        created = self.sendRequests()["created_at"]
        longUrl = self.sendRequests()["long_url"]
        shortUrl = self.sendRequests()["link"]
        print(f"\n\t\t\t[  Link Oluşturuldu  ]\n\t{yellow}[-]{reset}{white} Oluşturulma Zamanı : {created}\n\t{yellow}[-]{reset}{white} Orjinal link : {longUrl}\n\t{yellow}[-]{reset}{white} Kısaltırmış link : {shortUrl}")
    

if __name__ == "__main__":
    print(Fore.LIGHTRED_EX+"""
                        ,--,     .--.--.    
         ,--,         ,--.'|    /  /    '.  
       ,'_ /|  __  ,-.|  | :   |  :  /`. /  
  .--. |  | :,' ,'/ /|:  : '   ;  |  |--`   
,'_ /| :  . |'  | |' ||  ' |   |  :  ;_     
|  ' | |  . .|  |   ,''  | |    \  \    `.  
|  | ' |  | |'  :  /  |  | :     `----.   \ 
:  | | :  ' ;|  | '   '  : |__   __ \  \  | 
|  ; ' |  | ';  : |   |  | '.'| /  /`--'  / 
:  | : ;  ; ||  , ;   ;  :    ;'--'.     /  
'  :  `--'   \---'    |  ,   /   `--'---'   
:  ,      .-./         ---`-'               
 `--`----' 
            #Author : @Nemesis
    
""")

    link = LinkKısaltma(links= input(" --- > Linki Girin : "))
    link.parseData()

