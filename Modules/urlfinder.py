import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs

class urlFinder(object):
    def __init__(self, url: str) -> None:
        self.url = url

    def returnHeaders(self):
        return {'User-Agent': 'Mozilla/5.0', 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    
    def getContent(self) -> str:
        self.__url = requests.get(url=self.url, headers=self.returnHeaders())
        if self.__url.status_code == 200:
            return self.__url.content


    def parseContent(self):
        content = self.getContent()
        self.sayac = 1
        self.parse = bs(content, "lxml").find_all("a")

        for i in self.parse:
            parseHref = i.attrs.get("href")
            if parseHref == "" or parseHref is None:
                ...
            else: 
                print(self.sayac ,"--> ", urljoin(self.url, parseHref))
                self.sayac += 1

        print(f"{self.url} Adresinde toplam {self.sayac - 1} tane link bulundu ... ")
            


if __name__ == "__main__":
    print("""
    
 _____  _____      _____     ________  _                 __                
|_   _||_   _|    |_   _|   |_   __  |(_)               |  ]               
  | |    | | _ .--. | |       | |_ \_|__   _ .--.   .--.| | .---.  _ .--.  
  | '    ' |[ `/'`\]| |   _   |  _|  [  | [ `.-. |/ /'`\' |/ /__\\[ `/'`\] 
   \ \__/ /  | |   _| |__/ | _| |_    | |  | | | || \__/  || \__., | |     
    `.__.'  [___] |________||_____|  [___][___||__]'.__.;__]'.__.'[___]    

                        #Author : @Hê-ll | @Nemesis
""")
    url_user = input("[[ ? ]] Url Adresini girin : ")
    finder = urlFinder(url=url_user)
    finder.parseContent()
