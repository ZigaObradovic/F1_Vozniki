import uvozi
import izlusci
import write_csv
import os


drivers_directory = uvozi.drivers_directory
frontpage_filename = uvozi.frontpage_filename
drivers_page_url = uvozi.drivers_page_url
csv_filename = 'F1_drivers.csv'


def main(redownload=True, reparse=True):
    path = os.path.join(drivers_directory, frontpage_filename)
    if redownload or not os.path.exists(path):
        uvozi.save_frontpage(drivers_page_url, drivers_directory, frontpage_filename)
    else:
        print("datoteka html že obstaja")

    path = os.path.join(drivers_directory, csv_filename)
    if reparse or not os.path.exists(path):
        drivers = izlusci.drivers_from_file(frontpage_filename, drivers_directory)
        write_csv.write_drivers_to_csv(drivers, drivers_directory, csv_filename)
    else:
        print("Datoteka csv že obstaja")

if __name__ == '__main__':
    main(False, True)

print(izlusci.urls(frontpage_filename, drivers_directory))