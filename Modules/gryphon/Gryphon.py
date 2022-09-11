# Author: Helmsys #
#   Gryphon #


from requests_html import HTMLSession
from urllib.parse import urlparse
from urllib3 import disable_warnings
from .util import (ProxyChecker,URL_Shortened,LinkParser,CLI)
from random import choice
import json

disable_warnings()
usingProxy = False
class __Scanner(ProxyChecker):
    def __init__(self, prxtype) -> None:
        global usingProxy
        if prxtype.capitalize() != 'False':
            usingProxy = True
            super().__init__(prxtype=prxtype,isProxyPath=True if prxtype not in ['http','socks4','socks5'] else False, filePath=prxtype)

    def if_used_proxy(self) -> dict:
        if usingProxy:
            return {"http":f"{self._prxtype}://{choice(self.getWorkerProxy)}","https":f"{self._prxtype}://{choice(self.getWorkerProxy)}"}

    def scanner(self,query:str,isUserFinder:bool=False,num=10):
        firstFind = True
        if query:
            with HTMLSession() as session:
                if isUserFinder: # User Finder #
                    while firstFind:
                        try:
                            trash_recv = list(session.get(f'https://www.google.com/search?q=intext:"{query}"',proxies=self.if_used_proxy()).html.absolute_links)
                            link_storage = []
                            for recv in trash_recv:
                                name = urlparse(recv).hostname
                                if 'google.com' in name:
                                    link_storage.append(recv)
                            result = set(trash_recv) - set(link_storage)

                            with open(r"gryphon_OUTPUT\user_find_list.txt","w") as file:
                                for i in result:
                                    CLI.print_(self,i)
                                    file.write(f"{urlparse(i).hostname:<25} == https://{LinkParser(URL_Shortened(i)).parse}"+"\n")

                            if len(trash_recv) > 2 :
                                firstFind = False
                        except Exception:
                            continue

                    if not firstFind:
                        try:
                            __sherlock = "https://raw.githubusercontent.com/sherlock-project/sherlock/master/sherlock/resources/data.json"
                            for key, value in json.loads(session.get(__sherlock).content.decode('utf-8')).items():
                                response = session.get(url=value['url'].replace('{}',query),verify=False)
                                if response.status_code == 200:
                                    CLI.print_(self,value['url'].replace('{}',query))
                                    with open(r"gryphon_OUTPUT\user_find_list.txt","a") as file:
                                        file.write(f"{key:<25} == https://{LinkParser(URL_Shortened(value['url'].replace('{}',query))).parse}"+"\n")
                        except Exception:
                            pass

class UserFinder(__Scanner):
    def __init__(self, q:str,prxtype:str) -> None:
        super().__init__(prxtype)
        self.__query = q
        self.scanner()

    def scanner(self):
        return super().scanner(query=self.__query,isUserFinder=True)
