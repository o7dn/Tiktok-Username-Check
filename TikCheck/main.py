import os
import requests
import json
import time
from vardxg import Colors, Write, Center
from colorama import init

init(autoreset=True)
os.system('cls')

vardxg = ("""
████████╗██╗██╗  ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
╚══██╔══╝██║██║ ██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
   ██║   ██║█████╔╝ ██║     ███████║█████╗  ██║     █████╔╝ 
   ██║   ██║██╔═██╗ ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
   ██║   ██║██║  ██╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                  Made with <3 by vardxg


""")
Write.Print(Center.XCenter(vardxg), Colors.red,interval=0)


username = Write.Input("\n [?] Enter Username >>> ", Colors.red, interval=0)
os.system('cls')


class TikScraper():
    
    def tikstatus(username: str) -> None:
        
        url = f"https://api.secretprojects.xyz/v1/tiktok/profile/?username={username}"
        
        headers = {
            
            "connection": "keep-alive",
            "content-type": "application/json",
            "content-encoding": "br",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
            
        }
        
        response = requests.get(url,headers=headers)
        
        data = json.loads(response.text)

        status = data['status']


while True:

    url = f"https://api.secretprojects.xyz/v1/tiktok/profile/?username={username}"

    headers = {
        
        "Host": "api.secretprojects.xyz",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        "content-application": "application/json",
    }

    response = requests.get(url, headers=headers).json()

    for _ in range(4):
        if response["status"] == True:
            Write.Print(f"\n Status >>> Found Account!", Colors.green, interval=0)
            time.sleep(2)
            os.system('cls')
        
        elif response["status"] == False:
            Write.Print("\n Status >>> Account Not Found!", Colors.red, interval=0)
            time.sleep(2)
            os.system('cls')
        
        else:
            Write.Print("\n Status >>> Account Private Or The Account Doesn't Exist!", Colors.orange, interval=0)
            time.sleep(3)
            exit

# made by @vardxg on telegram.