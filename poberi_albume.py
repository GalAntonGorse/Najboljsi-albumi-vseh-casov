import re
import orodja

#with open ("source.html", "r", encoding="utf-8") as dat:
#    vsebina = dat.read()

vzorec_bloka = re.compile(
    r'<div id="pos\d+".*?'
    r'<div id="linkfire_button_container_charts_\d+',
    flags=re.DOTALL
)

vzorec_albuma = re.compile(
    r'<div class="topcharts_item_title"><a href="/release/album/.*?/.*?/" class="release" title="\[Album(?P<id_album>\d+?)\]">(?P<naslov>.*?)</a></div>.*?'
    r'<div class="topcharts_item_artist_newmusicpage topcharts_item_artist">(?P<izvajalci>.*?)</div>.*?'
    r'<div class="topcharts_item_releasedate">\d*\s?\w*?\s*(?P<leto>\d{4}).*?'
    r'<span class="topcharts_stat topcharts_avg_rating_stat">(?P<ocena>.+?)</span>.*?'
    r'<span class="topcharts_stat topcharts_ratings_stat">(?P<st_ocen>.+?)</span>.*?'
    r'class="topcharts_stat topcharts_reviews_stat">(?P<st_kritik>.+?)</',
    flags=re.DOTALL
)

vzorec_izvajalca = re.compile(
    r'<a (title="\[Artist\d+?\]")?  href="/artist/.*?" class="artist">(?P<izvajalec>.*?)\s?<',
    flags=re.DOTALL
)

vzorec_zanra = re.compile(
    r'<span class=""><a class="genre topcharts_item_genres" href="/genre/.*?/">(?P<zanr>.+?)</a>,?\s*?</span>',
    flags=re.DOTALL
)

vzorec_sekundarnega_zanra = re.compile(
    r'<span class=""><a class="genre topcharts_item_secondarygenres" href="/genre/.*?/">(?P<sek_zanr>.+?)</a>,?\s*?</span>',
    flags=re.DOTALL
)

vzorec_opisa = re.compile(
    r'<span class="topcharts_item_descriptors">(?P<opis>.+?),?\s*?</span>',
    flags = re.DOTALL
)

def izloci_izvajalce(niz):
    izvajalci = []
    for izvajalec in vzorec_izvajalca.finditer(niz):
        izvajalci.append(izvajalec.groupdict()["izvajalec"].replace("&amp;", "&").replace("&#39;", "'"))
    return izvajalci

def izloci_zanre(niz):
    zanri = []
    for zanr in vzorec_zanra.finditer(niz):
        zanri.append(zanr.groupdict()['zanr'])
    return zanri

def izloci_sek_zanre(niz):
    sek_zanri = []
    for sek_zanr in vzorec_sekundarnega_zanra.finditer(niz):
        sek_zanri.append(sek_zanr.groupdict()['sek_zanr'])
    return sek_zanri

def izloci_opise(niz):
    opisi = []
    for opis in vzorec_opisa.finditer(niz):
        opisi.append(opis.groupdict()['opis'])
    return opisi
    
def izloci_podatke_albuma(blok):
    album = vzorec_albuma.search(blok).groupdict()
    album['id_album'] = int(album['id_album'])
    album['naslov'] = album['naslov'].replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
    album['izvajalci'] = izloci_izvajalce(album['izvajalci'])
    album['zanri'] = izloci_zanre(blok)
    album['sek_zanri'] = izloci_sek_zanre(blok)
    album['opisi'] = ", ".join(izloci_opise(blok))
    album['ocena'] = float(album['ocena'])
    album['st_ocen'] = int(album['st_ocen'].replace(',', ''))
    album['st_kritik'] = int(album['st_kritik'].replace(',', '')) if album['st_kritik'] != "-" else 0
    album['leto'] = int(album['leto'])
    return album

def albumi_na_strani(st_strani):
    url = (
        f'https://rateyourmusic.com/charts/top/album/all-time/{st_strani}/#results'
    )
    ime_datoteke = f'najboljsi-albumi-{st_strani}.html'
    orodja.shrani_spletno_stran(url, ime_datoteke)
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for blok in vzorec_bloka.finditer(vsebina):
        yield izloci_podatke_albuma(blok.group(0))

def izloci_gnezdene_podatke(albumi):
    opus, zanri = [], []
    videni_izvajalci = set()

    def dodaj_delo(album, izvajalec):
        if izvajalec not in videni_izvajalci:
            videni_izvajalci.add(izvajalec)
        opus.append({
            'album': album['id_album'],
            'izvajalec': izvajalec
        })


    for album in albumi:
        for zanr in album.pop('zanri'):
            zanri.append({'album': album['id_album'], 'zanr': zanr})
        for zanr in album.pop('sek_zanri'):
            zanri.append({'album': album['id_album'], 'zanr': zanr})
        for izvajalec in album.pop('izvajalci'):
            dodaj_delo(album, izvajalec)

    opus.sort(key=lambda delo: delo['album'])
    zanri.sort(key=lambda zanr: (zanr['album'], zanr['zanr']))

    return opus, zanri

albumi = []
for st_strani in range(1, 26):
    for album in albumi_na_strani(st_strani):
        albumi.append(album)

albumi.sort(key=lambda album: album['id_album'])
orodja.zapisi_json(albumi, 'obdelani-podatki/albumi.json')
opus, zanri = izloci_gnezdene_podatke(albumi)
orodja.zapisi_csv(
    albumi,
    ['id_album', 'naslov', 'leto', 'ocena', 'st_ocen', 'st_kritik', 'opisi'], 'obdelani-podatki/albumi.csv'
)
orodja.zapisi_csv(opus, ['album', 'izvajalec'], 'obdelani-podatki/opus.csv')
orodja.zapisi_csv(zanri, ['album', 'zanr'], 'obdelani-podatki/zanri.csv')

#count=0
#for album in vzorec_albuma.findall(vsebina):
#    print(count, album)
#    count += 1
