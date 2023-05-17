# from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
from random import choice
import time
# import os
# import sys 
# sys.path.append(os.path.abspath('../secondary_funcs'))
from main import random_headers as h
# python -m utils.toKnowYourAdress
# export PYTHONPATH=/home/kali/Desktop/IgorParser/Igor_parser/secondary_funcs:$PYTHONPATH


def proxy_reader():
    with open("./proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
        print(len(prLi))
    return prLi


def checkIP(): 
    # print(proxiess)  
    prLi = proxy_reader()
    # return
    # link = 'http://checkip.dyndns.org'
    link = 'https://api.ipify.org'
    
    
    # return

    for pr in prLi:
        proxy_item = {       
            "https": f"http://{pr}"          
        } 
        headers=h()
        print(headers)
        print(proxy_item)
        try:
            ip = requests.get(link, headers=headers, proxies=proxy_item, timeout=(3.15, 21.15))
            # ip = requests.get(link, headers=headers, timeout=(3.15, 21.15))
            print(ip.text)
        except Exception as ex:
            print(ex)


checkIP()

# python toKnowYourAdress.py

# python -m utils.toKnowYourAdress