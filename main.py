import uvozi
import izlusci
import write_csv
import os
import izlusci2



drivers_directory = uvozi.drivers_directory
frontpage_filename = uvozi.frontpage_filename
drivers_page_url = uvozi.drivers_page_url
csv_filename = 'F1_drivers.csv'
sez = []





def main(redownload=True, reparse=True):
    path = os.path.join(drivers_directory, frontpage_filename)
    if redownload or not os.path.exists(path):
        uvozi.save_frontpage(drivers_page_url, drivers_directory, frontpage_filename)
    else:
        print(f"datoteka {frontpage_filename} že obstaja")

    path = os.path.join(drivers_directory, csv_filename)
    if reparse or not os.path.exists(path):
        drivers = izlusci.drivers_from_file(frontpage_filename, drivers_directory)
        write_csv.write_drivers_to_csv(drivers, drivers_directory, csv_filename)
    else:
        print("Datoteka csv že obstaja")


if __name__ == '__main__':
    main(False, True)


def preberi_stevilo():
    max_tock = izlusci.najvec_tock(frontpage_filename, drivers_directory)
    niz = input("> Vnesi najnižje število točk, ki jih morajo imeti vozniki, ki jih želite dodatno analizirati: ")
    if niz.isnumeric() and int(niz) < max_tock or niz[1:].isnumeric() and niz[0] == "-":
        return int(niz)
    elif niz.isnumeric() and int(niz) >= max_tock or niz[1:].isnumeric() and niz[0] == "-":
        print(f'Žal mora biti število manjše od {max_tock}')
        return preberi_stevilo()
    else:
        print(f'Žal "{niz}" ni celo število, poskusi ponovno!')
        return preberi_stevilo()



def main(redownload=True, reparse=True):
    i = 1
    j = preberi_stevilo()
    for driver in izlusci.drivers_from_file(frontpage_filename, drivers_directory):
        if int(driver['točke']) > j:
            drivers_page_url = driver['dodatni url']
            frontpage_filename2 = f'driver{i}.html'
        
            path = os.path.join(drivers_directory, frontpage_filename2)
            if redownload or not os.path.exists(path):
                uvozi.save_frontpage(drivers_page_url, drivers_directory, frontpage_filename2)
            else:
                print(f"datoteka {frontpage_filename2} že obstaja")
        
            sez.append(izlusci2.drivers_from_file(frontpage_filename2, drivers_directory))
            i += 1

    path = os.path.join(drivers_directory, csv_filename)
    if reparse or not os.path.exists(path):
        write_csv.write_drivers_to_csv(sez, drivers_directory, 'F1_drivers_dodatno.csv')
    else:
        print("Datoteka csv že obstaja")

if __name__ == '__main__':
    main(False, True)

