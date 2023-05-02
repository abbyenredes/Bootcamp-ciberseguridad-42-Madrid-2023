#!/usr/bin/env python3

#librerias
import requests
from bs4 import BeautifulSoup as bs
import os
import argparse
from urllib.parse import urlparse

#Variables

#Funcion para los argumentos
def argument():
    parser = argparse.ArgumentParser() #objeto de ArgumentParser
    #añade argumentos al objeto
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()
    args = parser.parse_args() #analiza los argumentos

#peticion web
req = requests.get(url)

#comprobar que la peticion de 200
status_code = req.status.get(url)
if status_code == 200:
    soup = bs(req.text, 'html.parser') #pasa el contenido HTML a un objeto BS
    #recorro todas las entradas de la web para extraer las img
    for i in soup.find_all('img'):
        print(i)




#def download_img(site)
