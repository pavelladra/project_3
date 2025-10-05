# Elections scraper
Projekt 3 pro Engeto Python Akademii

## Popis projektu
Cílem je extrahování výsledků parlamentních voleb v roce 2017 pro vybraný okres [z tohoto odkazu](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) (sloupec *Výběr obce*) a jejich uložení do csv souboru.

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru `requirements.txt`. Pro instalaci doporučuji použít nové
virtuální prostředí a s nainstalovaným manažerem spustit následovně:

$ pip3 --version                    # ověřím verzi manazeru
$ pip3 install -r requirements.txt  # nainstalujeme knihovny


## Spuštění projektu
Soubor main.py se spouští z příkazového řádku a požaduje dva argumenty.

> python main.py <odkaz_uzemniho_celku> <nazev_vystupniho_souboru>

Výstupem pak je soubor .csv s výsledky voleb.

## Ukázka projektu
Výsledky pro okrsek Praha:
> 1. argument -> https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
> 2. argument -> vysledky_Praha.csv


Spuštění programu:
>  python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100"
 "vysledky_Praha.csv"


Část běhu programu
> STAHUJI DATA Z URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
> 
> STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1&xobec=500054&xvyber=1100
> 
> STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1&xobec=500224&xvyber=1100
> 
> STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1&xobec=547034&xvyber=1100
> 
> ...
> 
> UKLÁDÁM DATA DO SOUBORU: vysledky_Praha.csv
> 
> UKONČUJI: main.py


Částečný výstup:
>Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Volte Pr.Blok www.cibulka.net,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",...

>500054,Praha 1,21 556,14 167,14 036,2 770,9,13,657,12,1,774,392,514,41,6,241,14,44,2 332,5,0,12,2 783,1 654,1,7,954,3,133,11,2,617,34

>500224,Praha 10,79 964,52 277,51 895,8 137,40,34,3 175,50,17,2 334,2 485,1 212,230,15,1 050,35,67,9 355,9,8,30,6 497,10 856,37,53,2 398,12,477,69,53,2 998,162

>547034,Praha 11,58 353,39 306,39 116,5 100,48,18,2 513,30,17,1 548,2 310,757,192,13,846,29,57,6 763,11,5,23,3 598,10 213,31,35,1 622,14,373,86,53,2 674,137
