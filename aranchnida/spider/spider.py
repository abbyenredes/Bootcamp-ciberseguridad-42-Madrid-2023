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
    parser.add_argument('url', help='introduce la web a \'scrapear\'', type=str)
    parser.add_argument('-r', '--recursive', help='las imagenes se descargaran de forma recursiva', action='store_true')
    parser.add_argument('-l', '--depth', help='nivel de profundidad para la busqueda y descarga de imagenes', type=int, default=5)
    parser.add_argument('-p', '--path', help='carpeta donde se descargaran las imagenes',type=str, default='./data/')

    return parser.parse_args() #analiza los argumentos

#peticion web
def scraping(web_site, level):
	try:

		req = requests.get(web_site, timeout=5)

		#comprobar  la peticion de 200
		status_code = req.status.get(web_site)
		if status_code == 200:
			soup = bs(req.text, 'html.parser') #pasa el contenido HTML a un objeto BS
			links = soup.find_all('a')#recorro todas las entradas de la web para extraer las img
			for link in links:
				print(i)
	finally:
		print(error)
