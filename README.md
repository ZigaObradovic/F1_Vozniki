# F1_Vozniki
V svoji nalogi sem analiziral in med seboj primerjal podatke vseh voznikov Formule 1, ki so kadarkoli tekmovali v tem  športu.
<br/>Osnovne podatke sem pridobil iz spletne strani https://www.f1-fansite.com/f1-results/all-time-f1-driver-rankings/, nato pa sem pridobil če nekaj dodatnih podatkov preko hitrih povezav na tej strani. 

### Navodila za uporabo: 
Najprej zaženite datoteko main.py, ki bo na podlagi spletne strani najprej ustvarila prvo csv datoteko. Nato vas vpraša za vnos števila točk, ki jih imajo vozniki, na podlagi katerih bo izbral voznike za dodatno analizo. Glede na vaš vnos se bo za vsakega voznika, ki ustreza danemu pogoju, ustvarila html datoteka. Za število le teh vas ne rabi skrbeti, saj boste v naslednjem koraku morali potrditi, da vam število na novo ustvarjenih html datotek ustreza. Če boste s svojo izbiro zadovoljni, se bo ustvarila še dodatna csv datoteka, sicer pa vas program vpraša po ponovnem vnosu števila točk za dodatno analizo.
<br/>S tem so vsi podatki pripravljeni. Potrebno je le še pognati zvezek analiza_voznikov.ipynb, kjer so podatki analizirani s pomočjo grafov in tabel.