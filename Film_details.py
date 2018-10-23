from tkinter import *
from urllib.request import urlopen
import xmltodict
from Database import *

keuze_film = 7

def film_details(keuze_film):
    database = open('database.csv', 'r', encoding='utf-8')

    if keuze_film == 7:

        for line in database.readlines(7):
            gegevens = line.split(";")

    url = gegevens[0]

    titel = gegevens[1]

    jaar = gegevens[2]

    regisseur = gegevens[3]

    cast = gegevens[4].split(':')

    genre = gegevens[5]

    land = gegevens[6]

    cover = gegevens[7]

    tagline = gegevens[8]

    synopsis = gegevens[9]

    duur = gegevens[10]

    rating = gegevens[11]

    return url, titel, jaar, regisseur, cast, genre, land, cover, tagline, synopsis, duur, rating
    database.close()


print(film_details(nummer_film))