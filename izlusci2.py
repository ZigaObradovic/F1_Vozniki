import re
import os


def read_file_to_string(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, encoding='utf-8') as file_in:
        text = file_in.read()
    return text


def get_dict_from_driver_page(page):
    vzorec_ime = r"<td>Name</td><td>(.*?)</td>"
    vzorec_visina = r'<td>Height</td><td>(.*?) meter'
    vzorec_starost = r'<td>Date of Birth</td><td>(.*?)- (.*?) years old</td>'
    vzorec_povp_startno_mesto = r'<td>Avg. GP Grid</td><td>(.*?)</td>'
    vzorec_povp_koncna_pozicija = r'<td>Avg. GP Position</td><td>(.*?)</td>'
    vzorec_prevozeni_krogi = r'<td>Total GP Laps</td><td>(.*?)</td>'

    ime = re.search(vzorec_ime, page)
    visina = re.search(vzorec_visina, page)
    starost = re.search(vzorec_starost, page)
    povp_startno_mesto = re.search(vzorec_povp_startno_mesto, page)
    povp_koncno_mesto = re.search(vzorec_povp_koncna_pozicija, page)
    prevozeni_krogi = re.search(vzorec_prevozeni_krogi, page)
    
    if ime == None or visina == None or starost == None or povp_startno_mesto == None or povp_koncno_mesto == None or prevozeni_krogi == None:
        return None
    else:
        return {"ime": ime.group(1), "višina (m)": visina.group(1), "starost": starost.group(2), "povp. štartno mesto": povp_startno_mesto.group(1), "povp. končno mesto": povp_koncno_mesto.group(1), "prevoženi krogi": prevozeni_krogi.group(1)}
    
def drivers_from_file(filename, directory):
    page_content = read_file_to_string(directory, filename)
    return get_dict_from_driver_page(page_content)