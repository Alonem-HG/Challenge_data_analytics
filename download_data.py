#!pip install requests
#!pip install bs4

import datetime
import io
import os
import re
from urllib.error import HTTPError

import pandas as pd
import requests
from bs4 import BeautifulSoup

from loggin import logging_options

log = logging_options.setup_logger("dowload_data")


def get_list_urls_csv_from_website():
    '''
    Return: list of csv links and name of categories
    '''

    url_museos = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_4207def0-2ff7-41d5-9095-d42ae8207a5d"
    url_cines = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae"
    url_bibliotecas = "https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7"

    categorias = []
    urls = []

    for url in [url_museos, url_cines, url_bibliotecas]:
        try:
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', attrs={"class": "btn btn-green btn-block"}):
                url = link.get('href')
                urls.append(url)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

    categorias = [re.findall('([^\/]+)(?=\.\w+$)', urls[i])
                  for i in range(len(urls))]
    log.debug("Urls were saved...")
    return urls, categorias


# urls, categorias = get_urls()
# listaUrl = urls
# listaCategorias = categorias


def convert_links_to_dataframe(urls):
    '''
    Transform links of csv to dataframes and return a list of them.
    '''

    dataframes_list = []

    for u in range(len(urls)):
        response = requests.get(urls[u])
        file_object = io.StringIO(response.content.decode('utf-8'))
        temp_df = pd.read_csv(file_object, encoding='utf-8')
        dataframes_list.append(temp_df)

    log.debug("dataframes list were created...")

    return dataframes_list


def save_csv_localStorage (dataframes, categorias):
    '''
    Create a directory with the following structure:
    categoría\año-mes\categoria-dia-mes-año.csv
    Ex.: museos\2021-noviembre\museos-03-11-2021.csv 
    date: format used DD-MM-YYYY.
    Finally, save csv in local storage.
    '''

    s = '\\'
    folder_name = r'downloaded-files'
    time_ym = datetime.datetime.now().strftime("%Y-%m")
    time_dmy = datetime.datetime.now().strftime("%d-%m-%Y")

    folder_to_save_files = []
    for c in range(len(categorias)):
        categoria = str(categorias[c])[2:-2]
        path = categoria + s + time_ym + s  # categoria\\anio-mes\\
        folder_to_save_files.append(path)

    # IF no such folder exists, create one automatically
        if not os.path.exists(folder_to_save_files[c]):
            os.makedirs(folder_to_save_files[c], exist_ok=True)
            log.info(f"Directory... {folder_to_save_files[c]} was created")
            new_file = categoria + '-' + time_dmy+'.csv'
            
            dataframes[c].to_csv(folder_to_save_files[c] + categoria +
                                 '-' + time_dmy+'.csv', index=False, encoding='utf-8')

            log.info(f"{new_file} were saved...")

        else:
            log.debug(f"Directory... {folder_to_save_files[c]} already exists")
            new_file = categoria + '-' + time_dmy+'.csv'
            dataframes[c].to_csv(folder_to_save_files[c] + categoria +
                                 '-' + time_dmy+'.csv', index=False, encoding='utf-8')
            log.info(f"{new_file} were saved...")
