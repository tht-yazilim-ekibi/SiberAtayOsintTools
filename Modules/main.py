import os, time
from colorama import Fore, Style, init
from getpass import getuser


init(autoreset=True)

magenta = Fore.MAGENTA
bright = Style.BRIGHT
reset = Fore.RESET
cyan = Fore.CYAN
black = Fore.LIGHTBLACK_EX


print(magenta+bright+f"""

                                                              
                      .::::.      ..::::                     
                    :=+++++++====+++++++=:                   
                    -++++++++++++++++++++++-                  
                  -++++++++++++++++++++++++-                 
                  :++++++++++++++++++++++++++:                
                  =++++++++++++++++++++++++++=                
                -++++++++++++++++++++++++++++-               
                .+++++++++++++++++++++++++++++=.              
        .:-==++++++++++++++++++++++++++++++++++++==-:.       
      .-++++++++++++++++++++++++++++++++++++++++++++++++-:    
    .=+++++++++++++++++++++++++++++++++++++++++++++++++++++.  
    =++++++++++++++++++++++++++++++++++++++++++++++++++++++=  
    .=++++++++++++++++++++++++++++++++++++++++++++++++++++=.  
      .-=++++++++++++++++++++++++++++++++++++++++++++++=-.    
          .-++++++++++++++++++++++++++++++++++++++++-.        
        .-+***++#**#***********++***********#**#*+***+-.      
      :+*******+==-*%%%%%%%%%%#**#%%%%%%%%%%*-===*******+:    
    .+***********=-=#%%%%%%%%%*--+%%%%%%%%%#=-=***********+:  
    .-+**********=--=*%%%%%%%*=---*%%%%%%%#=--=**********+-.  
      .=********+----==++++=------=++++==----+********=:     
          :+******=--------------------------=******+:        
            .+*****=------------------------=******.          
            =*******+----------------------+*******+          
          =*********#+------------------+#*********+         
          =***********##*+=----------=+*##***********+        
        =**************##%##******##%##**************+       
        ..:--==+**********##%%%%%%##**********+==--::.       
                  ..::--=++***##***++==-::..                 
                              ....                       

    {cyan} [ - ] TurkHackTeam| Ar-Ge kulübü | SiberAtay Osint Tool [ - ] {reset}

  [1] İp bilgi toplama. {black}< python iposint.py >{reset} \t\t\t\t[6]  Web sitesi url toplayıcı {black}< python urlfinder.py >{reset}
  [2] Telefon numarası bilgi toplama. {black}< python phoneNoosint.py >{reset} \t[7]  Port tarayıcısı {black}<python app.py >{reset}
  [3] Domain bilgi toplama - urlvoid. {black}< python domaininfo.py >{reset} \t\t[8]  Kullanıcı adı kontrol edici {black}< python app.py>{reset}
  [4] Whois Sorgusu  {black}< python whoisQuery.py >{reset}\t\t\t\t[9]  Shodan {black}< python shodanOsint.py>{reset}
  [5] Link Kısaltma  {black}< python linkisaltma.py >{reset} \t\t\t\t[10] Hashtag gönderi toplayıcı {black}<python hashtag.py>{reset}
  """) 