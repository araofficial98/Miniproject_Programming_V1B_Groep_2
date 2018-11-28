from Database import *


# Deze functie haalt een lijst op uit de database van de gekozen film met alle informatie over de film erin.
def film_details(keuze_film):
    titel1 = films[keuze_film]['titel']

    jaar1 = films[keuze_film]['jaar']

    genre1 = films[keuze_film]['genre']

    duur1 = films[keuze_film]['duur']

    land1 = films[keuze_film]['land']

    uitleg1 = films[keuze_film]['synopsis']

    regisseur1 = films[keuze_film]['regisseur']

    imdb_rating1 = films[keuze_film]['imdb_rating']

    zender1 = films[keuze_film]['zender']

    total = [titel1, jaar1, genre1, duur1, imdb_rating1, land1, regisseur1, uitleg1, zender1]

    return total

