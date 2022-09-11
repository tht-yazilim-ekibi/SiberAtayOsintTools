# Author: Helmsys
#   Main App #
from time import (time,sleep)
from urllib.request import ProxyBasicAuthHandler
from weakref import proxy
from gryphon.util.portscanner import port_scaner
from gryphon import Gryphon,CLI

import os

class App:
    def __init__(self) -> None:
        self.__createFolder()
        print(CLI.banner)
        while True:
            print(CLI.gryphoncommandline, end="")
            input_ = input()
            if input_ == '0':
                print(CLI.usercommandline, end="")
                q = input()
                print(CLI.proxycommandline, end="")
                proxyTyp = input()
                Gryphon.UserFinder(q=q,prxtype=proxyTyp)

            elif input_ == "1":
                port_scaner()
                

            elif input_.lower() == 'h':
                print(CLI.help(self))

            elif input_.lower() == 'e':
                print('Bye')
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    def __createFolder(self):
        try:
            return os.mkdir('gryphon_OUTPUT')
        except FileExistsError:
            pass

def main():
    App()
    
main()