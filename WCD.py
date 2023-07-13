import requests
import os
from bs4 import BeautifulSoup

def download_file(url, folder_path):
    response = requests.get(url)
    file_path = os.path.join(folder_path, url.split('/')[-1])
    with open(file_path, 'wb') as file:
        file.write(response.content)

def download_website(url, folder_path):
    response = requests.get(url)
    html_content = response.text

    os.makedirs(folder_path, exist_ok=True)

    html_file_path = os.path.join(folder_path, 'index.html')
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    css_files = [link.get('href') for link in BeautifulSoup(html_content, 'html.parser').find_all('link', href=True)]
    js_files = [script.get('src') for script in BeautifulSoup(html_content, 'html.parser').find_all('script', src=True)]

    for css_file in css_files:
        if not css_file.startswith('http'):
            css_file = url + css_file
        download_file(css_file, folder_path)

    for js_file in js_files:
        if not js_file.startswith('http'):
            js_file = url + js_file
        download_file(js_file, folder_path)

url = 'https://rollbit.com/'
folder_path = r'C:\Users\ashab\OneDrive\Desktop\Neuer Ordner (4)'

download_website(url, folder_path)
