import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore, init

init(autoreset=True)

green = Fore.GREEN
reset = Fore.RESET
cyan = Fore.CYAN
yellow = Fore.YELLOW

class HashtagFinder(object):
    def __init__(self, hashtag: str, count: int) -> None:
        self.hashtag = hashtag
        self.count = count
        self.sayac = 1

    def postDataFromWebpage(self):
        self.__headers = {
            "tag": str(self.hashtag)
        }
        hashtagCount = 1
        while True:
            try:

                self.__requestsPost = requests.post(url=f"https://www.hashatit.com/load_more_new/{self.hashtag}/all/{hashtagCount}/20/hashtags", headers=self.__headers).json()
                for i in (bs(self.__requestsPost["html"], "lxml").find_all("div", class_="media-box-content new")):
                    
                    for text, date, hrefLinks in zip(i.find_all("div", class_="media-box-text"),i.find_all("div", class_="media-box-date"), i.find_all("div", class_="media-box-more")):
                        print(f"{yellow}Text ---->{reset} {str(text.getText()).strip()}\n{yellow}Date ---->{reset} {str(date.getText()).strip()}\n{yellow}Link ----> {reset}{hrefLinks.find('a').get('href')}\n")
                        
                        if self.sayac == self.count:
                            print(f"{self.hashtag} hashtag adından {self.count} tane gönderi bulundu ... ")
                            exit()
                        self.sayac += 1


            except KeyError:
                print(f"{self.hashtag} Hashtag adında {self.sayac-1} tane gönderi bulundu ...")
                exit()
                
            hashtagCount += 1

if __name__ == "__main__":
    print(green+"""

  ___ ___             __           _______             
 |   Y   .---.-.-----|  |--.______|       .---.-.-----.
 |.  1   |  _  |__ --|     |______|.|   | |  _  |  _  |
 |.  _   |___._|_____|__|__|      `-|.  |-|___._|___  |
 |:  |   |                          |:  |       |_____|
 |::.|:. |                          |::.|              
 `--- ---'                          `---'              

            #Author : @MuhammedTr768 | @Nemesis
    
""")
    print(f"{cyan}[ ? ]{reset} Hashtag ismini girin : ",end="")
    hashtagN = str(input())
    print(f"{cyan}[ ? ]{reset} Kaç tane gönderi çekilsin : ", end="")
    countHashtag = int(input())
    hashtagFinder = HashtagFinder(hashtag=hashtagN, count=countHashtag)
    hashtagFinder.postDataFromWebpage()
    