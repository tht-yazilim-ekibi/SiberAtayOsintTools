from phonenumbers import carrier, parse, geocoder, timezone, is_valid_number
from colorama import Fore, init, Style


init(autoreset=True)
print(Style.BRIGHT+Fore.LIGHTBLUE_EX+"""
______       _____      _       _   
| ___ \     |  _  |    (_)     | |  
| |_/ /_____| | | | ___ _ _ __ | |_ 
|  __/______| | | |/ __| | '_ \| __|
| |         \ \_/ /\__ \ | | | | |_ 
| |_____     \___/ |___/_|_| |_|\__|
|_______|

#Author : @Nemesis

""")
userPhoneNumber = input("[ ➛ ] Telefon numarasını giriniz (exp(+90539111111 )) :")

parseNumber = parse(str(userPhoneNumber), "tr")
operatör = carrier.name_for_number(parseNumber, "tr")
ülke = geocoder.description_for_number(parseNumber, "tr")
saat_dilimi = timezone.time_zones_for_number(parseNumber)
isValidNumber = is_valid_number(parseNumber)

print(f"""
[+] Operatör   :  {operatör}
[+] Ülke       :  {ülke}
[+] Saat Dilimi:  {saat_dilimi}
[+] Telefon numarası geçerlimi : {isValidNumber}
""")