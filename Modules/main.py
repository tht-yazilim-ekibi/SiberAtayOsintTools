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

    {cyan} [ - ] TurkHackTeam| Ar-Ge kul??b?? | SiberAtay Osint Tool [ - ] {reset}

  [1] ??p bilgi toplama. {black}< python iposint.py >{reset} \t\t\t\t[6]  Web sitesi url toplay??c?? {black}< python urlfinder.py >{reset}
  [2] Telefon numaras?? bilgi toplama. {black}< python phoneNoosint.py >{reset} \t[7]  Port taray??c??s?? {black}<python app.py >{reset}
  [3] Domain bilgi toplama - urlvoid. {black}< python domaininfo.py >{reset} \t\t[8]  Kullan??c?? ad?? kontrol edici {black}< python app.py>{reset}
  [4] Whois Sorgusu  {black}< python whoisQuery.py >{reset}\t\t\t\t[9]  Shodan {black}< python shodanOsint.py>{reset}
  [5] Link K??saltma  {black}< python linkisaltma.py >{reset} \t\t\t\t[10] Hashtag g??nderi toplay??c?? {black}<python hashtag.py>{reset}
  """) 