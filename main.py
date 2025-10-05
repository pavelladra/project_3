"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Pavel ladra
email: ladrapavel@email.cz
"""

import sys
import csv
import requests
import bs4


voters = []
attendance = []
valid_ones = []


def getr(link):
    """Uložení HTML z adresy v argumentu. Vrací třídu BeautifulSoup"""
    geter = requests.get(link)
    html = bs4.BeautifulSoup(geter.text, "html.parser")
    print("STAHUJI DATA Z URL:", link)
    return html


if len(sys.argv) == 3:
    hateemel = getr(sys.argv[1])  # uložení html do proměnné pro opakované využití
else:
    print('Zadal jsi nesprávný počet argumentů. Argumenty musí být 3. '
          'Název souboru, url adresa v uvozovkách a libovolný název výstupního .csv.')
    quit()


def get_towns() -> list:
    """Vrací seznam měst v daném okrese"""
    towns = []
    towns_search = hateemel.find_all("td", "overflow_name")
    for t in towns_search:
        towns.append(t.text)
    return towns


def get_links() -> list:
    """Vrací URL adresu k získání detailů jednotlivých obcí požadovaného okresu"""
    path = []
    link_search = hateemel.find_all("td", "cislo", "href")
    for link_town in link_search:
        link_town = link_town.a["href"]
        path.append(f"https://volby.cz/pls/ps2017nss/{link_town}")
    return path


def get_id() -> list:
    """Vrací identifikační čísla jednotlivých obcí"""
    town_id = []
    ids = hateemel.find_all("td", "cislo")
    for i in ids:
        town_id.append(i.text)
    return town_id


def collect_parties() -> list:
    """Vrací seznam kandidujících stran v daném okresu"""
    parties = []
    town_link = get_links()
    html = requests.get(town_link[0])
    html_villages = bs4.BeautifulSoup(html.text, "html.parser")
    party = html_villages.find_all("td", "overflow_name")
    for p in party:
        parties.append(p.text)
    return parties


def get_voters_sum() -> None:
    """Jde o nečistou funkci, která do proměných
    voters, attendance, correct přidává celkový počet registrovaných
    voličů, zúčastněných voličů a platných hlasů za jednotlivé obce."""
    path = get_links()
    for p in path:
        html_path = requests.get(p)
        html_village = bs4.BeautifulSoup(html_path.text, "html.parser")
        voter = html_village.find_all("td", headers="sa2")
        for v in voter:
            v = v.text
            voters.append(v.replace('\xa0', ' '))
        attend = html_village.find_all("td", headers="sa3")
        for a in attend:
            a = a.text
            attendance.append(a.replace('\xa0', ' '))
        correct = html_village.find_all("td", headers="sa6")
        for c in correct:
            c = c.text
            valid_ones.append(c.replace('\xa0', ' '))


def collect_votes() -> list:
    """Vrací list listů, kde je uveden počet hlasů pro každou stranu v každé obci."""
    links = get_links()
    votes = []
    for li in links:
        html = getr(li)
        # t1sb3 a t2sb3 obsahují POČTY hlasů, nikoli procenta
        votes_search = html.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])
        temporary = []
        for v in votes_search:
            # odstraní pevné mezery \xa0
            temporary.append(v.text.replace('\xa0', ' '))
        votes.append(temporary)
    return votes

def whiterows_creator() -> list:
    """Pomocná funkce pro tvorbu csv souboru vrací list listů, kdy v každém listu je chronologicky
    uvedeno ID konkrétní obce, její název, registrovaní voliči, zúčastnění voliči, platné hlasy a
    počty hlasů každé z kandidujících stran."""
    rows = []
    get_voters_sum()
    towns = get_towns()
    ids = get_id()
    votes = collect_votes()
    zipped = zip(ids, towns, voters, attendance, valid_ones)
    aux_var = []
    for i, t, v, a, vo in zipped:
        aux_var.append([i, t, v, a, vo])
    zip_all = zip(aux_var, votes)
    for av, vs in zip_all:
        rows.append(av + vs)
    return rows


def election2017(link, file) -> None:
    """Hlavní část funkce, která za pomoci výše uvedených funkcí vytváří csv soubor
    s volebními výsledky"""
    try:
        header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        content = whiterows_creator()
        parties = collect_parties()
        print("UKLÁDÁM DATA DO SOUBORU:", file)
        for party in parties:
            header.append(party)
        with open(file, 'w', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(header)
            f_writer.writerows(content)
        print("UKONČUJI:", sys.argv[0])
    except IndexError:
        print("Nastala chyba. Nejspíš máte špatný odkaz nebo jste jej zapomněli dát do uvozovek.")
        quit()


if __name__ == '__main__':
    address = sys.argv[1]
    file_name = sys.argv[2]
    election2017(address, file_name)
