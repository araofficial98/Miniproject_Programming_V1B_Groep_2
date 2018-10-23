import tkinter
from urllib.request import urlopen
import xmltodict
from tkinter import *
from Film_details import *


def film_kiezen():
    return film_details()


master_root = Tk()
root = Frame(master=master_root)
root.pack(side=TOP)


titel = Label(master = root,
                font = ('Arial', 18, 'italic'),
                text = 'Titel |')
titel.grid(row = 0, column = 0, pady = 4)


datum = Label(master = root,
                font = ('Arial', 18, 'italic'),
                text = 'Datum |')
datum.grid(row = 0, column = 1, pady= 4)

duur = Label(master = root,
                font = ('Arial', 18, 'italic'),
                text = 'Duur |')
duur.grid(row = 0, column = 2, pady= 4)

jaar = Label(master = root,
                font = ('Arial', 18, 'italic'),
                text = 'Jaar |')
jaar.grid(row = 0, column = 3, pady= 4)

genre = Label(master = root,
                font = ('Arial', 18, 'italic'),
                text = 'Genre |')
genre.grid(row = 0, column = 4, pady= 4)


locatie = Label(master = root,
                font = ('Arial', 18, 'italic'),
                text = 'Locatie')
locatie.grid(row = 0, column = 5, pady= 4)

knop = Button(master = root,
              font = ('Arial', 20, 'bold'),
              text = 'Kies Film',
              command = film_kiezen())
knop.grid(row = 0, column = 6, pady = 4)



root.mainloop()


