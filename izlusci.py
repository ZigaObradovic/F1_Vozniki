import re
import os


def zaokrozi(str):
    if '.' in str:
        i = str.index('.')
        str = str[:i]
    return str

def read_file_to_string(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def page_to_drivers(page_content):
    return re.findall(r'<tr>.*?<th class=(.*?)</tr>', page_content, flags = re.DOTALL)

def get_dict_from_driver_block(block):
    vzorec_ime = r"F1 stats & info'>(.*?)</a></td>"
    vzorec_drzava = r'<img.*?alt="(.*?)" width=.*?></a>'
    vzorec_nastopi = r'<td class="msr_col3">(.*?)</td>'
    vzorec_prvo_mesto = r'<td class="msr_col4">(.*?)</td>'
    vzorec_drugo_mesto = r'<td class="msr_col5">(.*?)</td>'
    vzorec_tretje_mesto = r'<td class="msr_col6">(.*?)</td>'
    vzorec_stopnicke = r'<td class="msr_col7">(.*?)</td>'
    vzorec_starta_prvi = r'<td class="msr_col8">(.*?)</td>'
    vzorec_najhitrejsi_krog = r'<td class="msr_col9">(.*?)</td>'
    vzorec_naslovi = r'<td class="msr_col91">&nbsp;(.*?)</td>'
    vzorec_tocke = r'<td class="msr_col10">(.*?)</td>'
    vzorec_dodatni_url = r"></a> <a href='(.*?)' title="
    ime = re.search(vzorec_ime, block)
    drzava = re.search(vzorec_drzava, block)
    nastopi = re.search(vzorec_nastopi, block)
    prvo_mesto = re.search(vzorec_prvo_mesto, block)
    drugo_mesto = re.search(vzorec_drugo_mesto, block)
    tretje_mesto = re.search(vzorec_tretje_mesto, block)
    stopnicke = re.search(vzorec_stopnicke, block)
    starta_prvi = re.search(vzorec_starta_prvi, block)
    najhitrejsi_krog = re.search(vzorec_najhitrejsi_krog, block)
    naslovi = re.search(vzorec_naslovi, block)
    tocke = re.search(vzorec_tocke, block)
    dodatni_url = re.search(vzorec_dodatni_url, block)
    if ime == None or drzava == None or nastopi == None or prvo_mesto == None or drugo_mesto == None or tretje_mesto == None or stopnicke == None or starta_prvi == None or najhitrejsi_krog == None or naslovi == None or tocke == None or dodatni_url == None:
        return None
    else:
        return {"ime": ime.group(1), "država": drzava.group(1), "nastopi": nastopi.group(1), "prvo mesto": prvo_mesto.group(1), "drugo mesto": drugo_mesto.group(1), "tretje mesto": tretje_mesto.group(1), "stopničke": stopnicke.group(1), "začne s prve pozicije": starta_prvi.group(1), "najhitrejši krog": najhitrejsi_krog.group(1), "naslovi": naslovi.group(1), "točke": zaokrozi(tocke.group(1)), "dodatni url": dodatni_url.group(1)}

def drivers_from_file(filename, directory):
    page_content = read_file_to_string(directory, filename)
    blocks = page_to_drivers(page_content)
    drivers = [get_dict_from_driver_block(block) for block in blocks]
    return [driver for driver in drivers if driver != None]

def najvec_tock(filename, directory):
    sez = []
    for driver in drivers_from_file(filename, directory):
        sez.append(int(driver['točke']))
    return max(sez)
    