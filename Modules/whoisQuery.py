import whois
from colorama import Fore, init


white = Fore.LIGHTWHITE_EX
yellow = Fore.YELLOW
reset = Fore.RESET

init(autoreset=True)
print(Fore.LIGHTRED_EX+r"""
         ___ .___.__  ._______  .___ .________
.___    |   |:   |  \ : .___  \ : __||    ___/
:   | /\|   ||   :   || :   |  || : ||___    \
|   |/  :   ||   .   ||     :  ||   ||       /
|   /       ||___|   | \_. ___/ |   ||__:___/ 
|______/|___|    |___|   :/     |___|   :     
        :                :                    
        :                :
        :________________:
         #Author : @Hê-ll | @Nemesis                                  
""")

user_value = str(input("[ - ] Domain adını giriniz : "))
w = whois.whois(user_value)

print(f"{yellow}[-] {white}Domain Name:",w["domain_name"])
print(f"{yellow}[-] {white}Registrar: ",w["registrar"])
print(f"{yellow}[-] {white}Whois Server: ",w["whois_server"])
print(f"{yellow}[-] {white}Referral Url: ", w["referral_url"])
print(f"{yellow}[-] {white}Updated Date: ",w["updated_date"])
print(f"{yellow}[-] {white}Creation Date: ",w["creation_date"])
print(f"{yellow}[-] {white}Expiration Data: ",w["expiration_date"])
print(f"{yellow}[-] {white}Name Server: ",w["name_servers"])
print(f"{yellow}[-] {white}Status: ",w["status"])
print(f"{yellow}[-] {white}Emails: ",w["emails"])
print(f"{yellow}[-] {white}Dnssec: ",w["dnssec"])
print(f"{yellow}[-] {white}Name: ",w["name"])
print(f"{yellow}[-] {white}Org: ",w["org"])
print(f"{yellow}[-] {white}Address: ",w["address"])
print(f"{yellow}[-] {white}City",w["city"])
print(f"{yellow}[-] {white}State",w["state"])
print(f"{yellow}[-] {white}Registrant Postal Code: ",w["registrant_postal_code"])
print(f"{yellow}[-] {white}County",w["country"])


