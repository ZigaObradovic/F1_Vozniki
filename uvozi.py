import requests
import os


drivers_page_url = 'https://www.f1-fansite.com/f1-results/all-time-f1-driver-rankings/'

drivers_directory = 'F1_podatki'

frontpage_filename = 'F1_drivers.html'


def download_url_to_string(url):
    headers = {"User-Agent": "Chrome/124.0.6367.201", "Referer": 'https://www.google.com/'}
    page_content = requests.get(url, headers=headers)
    return page_content.text


def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


def save_frontpage(page, directory, filename):
    text = download_url_to_string(page)
    save_string_to_file(text, directory, filename)
    return text