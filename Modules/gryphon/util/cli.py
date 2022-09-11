import sys
from colorama import Style,Fore,init
from getpass import getuser
import os

init(autoreset=True)
class CLI:
    banner = f"""{Style.RESET_ALL}{Fore.CYAN}
    \t\t                        ______
    \t\t             ______,---'__,---'
    \t\t         _,-'---_---__,---'
    \t\t  /_    (,  ---____',
    \t\t /  ',,   `, ,-'
    \t\t;/)   ,',,_/,'
    \t\t| /\   ,.'//\\
    \t\t`-` \ ,,'    `.
    \t\t     `',   ,-- `.
    \t\t     '/ / |      `,         _
    \t\t     //'',.\_    .\\      ,==>- 
    \t\t  __//   __;_`-  \ `;.__,;'
    \t\t((,--,) (((,------;  `--'
    \t\t\t-= GRYPHON =-
    \t\t\t    {Fore.GREEN}AR-GE{Fore.CYAN}{Style.BRIGHT}
    \t[ {Fore.MAGENTA}0{Fore.CYAN} ] User-Finder\t\t[ {Fore.MAGENTA}1{Fore.CYAN} ] Port-Scanner
    \t[ {Fore.MAGENTA}e{Fore.CYAN} ] Exit\t\t\t[ {Fore.MAGENTA}h{Fore.CYAN} ] Help\n"""
    try:
      gryphoncommandline = f'{Style.BRIGHT}{Fore.GREEN}gryphon@{getuser()}{Fore.WHITE}:{Fore.BLUE}~{os.getcwd().split(getuser())[1]}{Fore.WHITE}${Style.RESET_ALL} '
      dorkcommandline = f'{Style.BRIGHT}{Fore.GREEN}Port Scanner@{getuser()}{Fore.WHITE}:{Fore.BLUE}~[Ip Address]{Fore.WHITE}${Style.RESET_ALL} '
      usercommandline = f'{Style.BRIGHT}{Fore.GREEN}userfinder@{getuser()}{Fore.WHITE}:{Fore.BLUE}~[USER]{Fore.WHITE}${Style.RESET_ALL} '
      proxycommandline = f'{Style.BRIGHT}{Fore.GREEN}proxy@{getuser()}{Fore.WHITE}:{Fore.BLUE}~{Fore.WHITE}${Style.RESET_ALL} '
    except : ... 
    def print_(self,string):
      sys.stdout.write(f"{Fore.CYAN}[ {Fore.YELLOW}+{Fore.CYAN} ] {string}\n")
      sys.stdout.flush()

    def help(self):
        return f"""\t  {Fore.LIGHTYELLOW_EX}.
          {Fore.LIGHTYELLOW_EX}.{Fore.CYAN}
        [ {Fore.LIGHTYELLOW_EX}0{Fore.CYAN} ] ==> Önce işlemlerden biri seçilir.
        [ {Fore.LIGHTYELLOW_EX}1{Fore.CYAN} ] ==> Ardından işleme göre bir girdi girilir.
        [ {Fore.LIGHTYELLOW_EX}2{Fore.CYAN} ] ==> Son olarak proxy türü istenir.
        [ {Fore.LIGHTYELLOW_EX}3{Fore.CYAN} ] ==> Proxy türleri socks5, socks4 ve http dir.
        [ {Fore.LIGHTYELLOW_EX}4{Fore.CYAN} ] ==> Elinizde txt dosyasına yazılmış bir proxy listesi varsa
        [ {Fore.LIGHTYELLOW_EX}5{Fore.CYAN} ] ==> Bunun yolunu ve dosya uzantısını belirterek işlem yapabilirsiniz.
        [ {Fore.LIGHTYELLOW_EX}6{Fore.CYAN} ] ==> Proxy kullanılmak istenmiyorsa "false" yazılması yeterli.
          {Fore.LIGHTYELLOW_EX}.
          {Fore.LIGHTYELLOW_EX}."""