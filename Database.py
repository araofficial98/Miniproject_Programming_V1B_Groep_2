import xmltodict
from urllib.request import urlopen
import datetime


def database():
    datum = datetime.datetime.now().date()

    datumvandaag = datum.strftime('%d-%m-%Y')

    a = urlopen(
        'http://api.filmtotaal.nl/filmsoptv.xml?apikey=i4ie557ulkaflgdscz6ecqmpie9tj9d8&dag='
        + datumvandaag + '&sorteer=0')

    with a as xml:
        content = xml.read()
        xmltotal = xmltodict.parse(content)
        return xmltotal


filmsoverzicht = database()

films = filmsoverzicht['filmsoptv']['film']
