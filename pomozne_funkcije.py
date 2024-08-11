import izlusci
import main_2


def zaokrozi(str):
    if '.' in str:
        i = str.index('.')
        str = str[:i]
    return str



def najvec_tock(filename, directory):
    sez = []
    for driver in izlusci.drivers_from_file(filename, directory):
        sez.append(int(driver['točke']))
    return max(sez)



def preberi_stevilo():
    max_tock = najvec_tock(main_2.frontpage_filename, main_2.drivers_directory)
    niz = input("\n> Vnesi najnižje število točk, ki jih morajo imeti vozniki, ki jih želite dodatno analizirati (priporočljivo: 500): ")
    if niz.isnumeric() and int(niz) <= max_tock:
        return preveri(int(niz))
    elif niz.isnumeric() and int(niz) >= max_tock:
        print(f'\nŽal mora biti število manjše od {max_tock}.')
        return preberi_stevilo()
    else:
        print(f'\nŽal "{niz}" ni pozitivno celo število, poskusi ponovno!')
        return preberi_stevilo()



def preveri(n):
    k = 0
    for driver in izlusci.drivers_from_file(main_2.frontpage_filename, main_2.drivers_directory):
        if int(driver['točke']) > n:
            k += 1
    niz2 = input(f'\n> Ustvarili boste {k} html datotek za dodatno analizo. Če želite nadaljevati vnesite "Da", sicer vnesite "Ne": ')
    if niz2.upper() == "DA":
        return n
    elif niz2.upper() == "NE":
        print('\nČe želite ustvariti manj html datotek za dodatno analzo vnesite višje število točk.')
        return preberi_stevilo()
    else:
        print(f'\nVaš vnos je bil "{niz2}". Prosim vnesite "Da" ali "Ne".')
        return preveri(n)