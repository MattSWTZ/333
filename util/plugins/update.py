import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.commun import *

def search_for_updates():
    clear()
    setTitle("333 Updater is Checking For Updates...")
    r = requests.get("https://github.com/AstraaDev/Discord-All-Tools-In-One/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        setTitle("333 New Update Found!")
        print(f'''\n\n                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝\n'''.replace('█', f'{b}█{y}'))
        discserver()
        print(f'''{y}[{Fore.RED}!{y}]{w}Looks like this 333 {THIS_VERSION} is outdated...''')
        soup = BeautifulSoup(requests.get("https://github.com/MattSWTZ/333/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(f'{y}[{b}#{y}]{w} Update to the latest version (Y/N) ? ')

        if choice.lower() == 'y' or choice.lower() == 'yes':
            print(f"\n{y}[{b}#{y}]{w} Updating...")
            setTitle(f'333 Updating...')

            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("333.zip", 'wb')as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("333.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("333.zip")
                cwd = os.getcwd()+'\\333\\'
                shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                try:
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), '333.exe')
                except Exception:
                    pass
                shutil.copyfile(cwd+'README.md', 'README.md')                   
                shutil.rmtree('333')
                setTitle('333 Update Complete!')
                input(f"\n{y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!", end="")
                os.startfile("333.exe")
                os._exit(0)

            else:
                new_version_source = requests.get("https://github.com/MattSWTZ/333/archive/refs/heads/master.zip")
                with open("Discord-All-Tools-In-One-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Discord-All-Tools-In-One-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Discord-All-Tools-In-One-main.zip")
                cwd = os.getcwd()+'\\Discord-All-Tools-In-One-main'
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                setTitle('@TIO Update Complete!')
                input(f"\n{y}[{Fore.GREEN}!{y}]{w} Update Successfully Finished!")
                if os.path.exists(os.getcwd()+'setup.bat'):
                    os.startfile("setup.bat")
                elif os.path.exists(os.getcwd()+'start.bat'):
                    os.startfile("start.bat")
                os._exit(0)
