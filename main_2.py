import uvozi
import izlusci
import write_csv
import os
import izlusci2
import pomozne_funkcije



drivers_directory = uvozi.drivers_directory
frontpage_filename = uvozi.frontpage_filename
drivers_page_url = uvozi.drivers_page_url
csv_filename = 'F1_drivers.csv'
sez = []
        


def main(redownload=True, reparse=True):
    i = 1
    j = pomozne_funkcije.preberi_stevilo()
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

