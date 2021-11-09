# Najboljsi-albumi-vseh-casov
Projektna naloga iz obdelave podatkov pri programiranju 1

## Podatki
Podatke bom zajemal iz strani [RateYourMusic](https://rateyourmusic.com/charts/top/album/all-time/), prek katere bom analiziral 
1000 "najvišje ocenjenih" (stran uporablja obtežene ocene) glasbenih albumov.

Za vsak album bom zajel:
* naslov in izvajalce,
* leto izida,
* primarne in sekundarne žanre,
* opis albuma,
* povprečno oceno,
* število ocen in kritik.

## Cilji
Vprašanja, na katera bom poskušal odgovoriti:
* kateri izvajalci se najpogosteje pojavljajo na seznamu,
* kako je povprečna ocena odvisna od števila ocen,
* kako je število ocen odvisno od števila kritik,
* kako se vrstni red albumov spreminja glede na obtežitev ocen.

## Vsebina
V mapi obdelani_podatki so naslednje datoteke:
* albumi.json, ki za vsak album vsebuje seznam z vsemi podatki, ki sem jih zajel (tj. id albuma, naslov, seznam izvajalcev, leto izida, povprečno oceno, 
število ocen, število kritik, seznam žanrov, seznam sekundarnih žanrov in niz, ki vsebuje opis)
* albumi.csv, ki za vsak album vsebuje njegov id, naslov, leto izida, povprečno oceno, število ocen, število kritik in niz z opisom
* opus.csv, ki vsebuje id albuma in enega izmed njegovih izvajalcev
* zanri.csv, ki vsebuje id albuma in enega izmed njegovih (sekundarnih) žanrov.

## Opomba
Stran RYM onemogoča avtomatičen zajem podatkov, zato sem jih moral na roko naložiti v datoteke "najboljsi-albumi-{i}.html" in šele nato zagnati "poberi_albume.py"
Sicer bi to naredil že moj program.
