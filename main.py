import random, requests, sys, os, time, datetime, configparser
from requests import get
from colorama import Fore
from requests import Session, exceptions
from fake_useragent import UserAgent
from discord_webhook import DiscordWebhook
config = configparser.ConfigParser()
config.read("config.ini")

def main():
    print()
    print(
        f'{Fore.WHITE}-----------------------------------------------\n{Fore.YELLOW} Генерация начинается, время - {Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime("%H:%M:%S")}{Fore.WHITE}...\n-----------------------------------------------')
    print()
    char = 'ABCDEFGHIJKLMNOPQRSTUVNWXYZabcdefghijklmnopqrsntuvwxyz1234567890'
    while True:
        try:
            ua = UserAgent()
            header = {'User-Agent': str(ua.chrome)}
            code = charn = ''.join((random.choice(char) for i in range(5)))
            url = f'https://clck.ru/{code}'
            r = requests.get(url, headers=header)
            if r.status_code == 200:
                webhook = DiscordWebhook(url=config.get("Webhook", "url"), content=url)
                print(f'{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime("%H:%M:%S")} |{Fore.LIGHTGREEN_EX}| {url}')
                webhook.execute()
            elif r.status_code == 404:
                pass
        except:
            pass


main()
