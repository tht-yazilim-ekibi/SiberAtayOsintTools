from bs4 import BeautifulSoup as bs
from getpass import getuser
from colorama import Fore, init, Style
import requests

init(autoreset=True)

class UrlVoidDomainİnformations(object):
    def __init__(self) -> None:
        print(Fore.LIGHTCYAN_EX+r""""
 ____                                                      ___         
/\  _`\                              __                  /'___\        
\ \ \/\ \   ___    ___ ___      __  /\_\    ___     ___ /\ \__/  ___   
 \ \ \ \ \ / __`\/' __` __`\  /'__`\\/\ \ /' _ `\ /' _ `\ \ ,__\/ __`\ 
  \ \ \_\ /\ \L\ /\ \/\ \/\ \/\ \L\.\\ \ \/\ \/\ \/\ \/\ \ \ \_/\ \L\ \
   \ \____\ \____\ \_\ \_\ \_\ \__/.\_\ \_\ \_\ \_\ \_\ \_\ \_\\ \____/
    \/___/ \/___/ \/_/\/_/\/_/\/__/\/_/\/_/\/_/\/_/\/_/\/_/\/_/ \/___/ 

                    #Author :  @Nemesis

""")
        print(f'{Style.BRIGHT}{Fore.GREEN}domaininfo@{getuser()}{Fore.WHITE}:{Fore.BLUE}~[domain]{Fore.WHITE}${Style.RESET_ALL} ',end="")
        self.__url = input()

    def getContent(self) -> str:
        self.__requests = requests.get(url=f"https://www.urlvoid.com/scan/{self.__url}/")
        if self.__requests.status_code == 200:
            return self.__requests.content


    def parseContent(self):
        content = self.getContent()
        self.parse = bs(content, "lxml").find_all("table", attrs={"class":"table table-custom table-striped"}, limit=2)
        for data1 in self.parse:
            for data2 in data1.find("tbody").find_all("tr"):

                print(Fore.RED+"[ - ]", Fore.WHITE+data2.find_all("td")[0].getText()+Fore.RESET,Fore.YELLOW+"==== >> "+Fore.RESET+Fore.LIGHTWHITE_EX+data2.find_all("td")[1].getText()+Fore.RESET)


if __name__ == "__main__":
    void = UrlVoidDomainİnformations()
    void.parseContent()


