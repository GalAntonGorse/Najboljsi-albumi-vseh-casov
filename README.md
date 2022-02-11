# Najboljsi-albumi-vseh-casov
Projektna naloga iz obdelave podatkov pri programiranju 1

## Podatki

Podatke sem zajel iz strani [RateYourMusic](https://rateyourmusic.com/charts/top/album/all-time/) (v nadaljevanj RYM), prek katere sem analiziral 
1000 najvišje ocenjenih glasbenih albumov. Za vsakega izmed teh albumov sem zajel naslov in izvajalce, leto izida, primarne in sekundarne žanre, 
opis albuma, povprečno oceno ter število ocen in kritik.

## Cilji

Z zajetimi podatki bom skušal odgovoriti na naslednja vprašanja.

* ### Prva točka: porazdelitev izvajalcev glede na število dobrih albumov
Moja hipoteza je, da ima skupina the Beatles največ albumov med najboljših 1000.

* ### Druga točka: povezava med številom ocen in povprečno oceno albuma ter med številom ocen in številom kritik

Menim, da je število kritik linearno odvisno od števila ocen, povprečna ocena pa pada obratno sorazmerno z njim. 

* ### Tretja točka: število dobrih albumov glede na desetletje

Tukaj bom testiral hipotezo, da so bila 80-ta zlato obdobje popularne glasbe in je od tedaj vse šlo le še navzdol.

* ### Četrta točka: pogostost žanrov med najboljšimi

Moja hipoteza je, da je rock žanr, ki se najpogosteje pojavlja med najboljšimi albumi.

* ### Peta točka: najboljši glasbeniki po desetletjih

Ogledal si bom izvajalce, ki so za vsako posamezno desetletje ustvarili največji doprinos (oziroma so naredili največ dobrih albumov).

* ### Šesta točka: napoved žanra glasbe glede na lastnosti albuma

Testiral bom na primer hipotezo, da je album z ženskimi vokali najverjetneje žanra pop, album, ki zveni jezno, pa najverjetneje žanra metal.

## Vsebina
V mapi obdelani_podatki so naslednje datoteke:
* albumi.json, ki za vsak album vsebuje seznam z vsemi podatki, ki sem jih zajel (tj. id albuma, naslov, seznam izvajalcev, leto izida, povprečno oceno, 
število ocen, število kritik, seznam žanrov, seznam sekundarnih žanrov in niz, ki vsebuje opis)
* albumi.csv, ki za vsak album vsebuje njegov id, naslov, leto izida, povprečno oceno, število ocen, število kritik in niz z opisom
* opus.csv, ki vsebuje id albuma in enega izmed njegovih izvajalcev
* zanri.csv, ki vsebuje id albuma in enega izmed njegovih (sekundarnih) žanrov.

Podatke sem analiziral v datoteki analiza_podatkov.ipynb.

## Opomba
Stran RYM onemogoča avtomatičen zajem podatkov, zato sem jih moral na roko naložiti v datoteke "najboljsi-albumi-{i}.html" in šele nato zagnati "poberi_albume.py".
Sicer bi to naredil že moj program.
