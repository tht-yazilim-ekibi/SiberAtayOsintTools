import socket
import sys
from colorama import Fore, init, Style


init(autoreset=True)
def port_scaner():
    print(Fore.YELLOW+Style.BRIGHT+'''

$$$$$$$\                       $$\                                                           
$$  __$$\                      $$ |                                                          
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\                                                         
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|                                                        
$$  ____/ $$ /  $$ |$$ |  \__| $$ |                                                          
$$ |      $$ |  $$ |$$ |       $$ |$$\                                                       
$$ |      \$$$$$$  |$$ |       \$$$$  |                                                      
\__|       \______/ \__|        \____/                                                       
                                                                                             
                         $$$$$$\                                                             
                        $$  __$$\                                                            
                        $$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
                        \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                         \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
                        $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
                        \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
                         \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|      
    
    ''')
    target = input("Hedef ip adresi : ")
    print("|"*40)
    try:
        for port in range(1,65535):
            soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            cevap = soc.connect_ex((target,port))
            if cevap == 0:
                print(f"[ + ] port {port} is open")
            
            
    except KeyboardInterrupt:
        print("Çıkış yapılıyor ... ")
        sys.exit()
