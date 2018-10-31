from Film_details import *
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyqrcode
import os
import png
from PIL import Image


def toon_typescherm():
    beginscherm.pack_forget()
    typescherm.pack()

    btn1 = Button(master=typescherm, text='Beheer', bg='#c4ad5a')
    btn1.pack()

    btn2 = Button(master=typescherm, text='Gebruiker', bg='#45f442', command=toon_beginscherm)
    btn2.pack()


def toon_beginscherm():
    detailscherm.pack_forget()
    typescherm.pack_forget()
    beginscherm.pack()


def toon_beginscherm_beheer():
    detailscherm.pack_forget()
    beginscherm_beheer.pack()
    lbl111 = Label(master=beginscherm_beheer,
                   font=('Arial', 20),
                   text='Kies uw film naar keuze:',
                   fg='white',
                   bg="#330d05",
                   bd=5)
    lbl111.pack()
    titel_lbl11 = Label(master=beginscherm_beheer,
                        font=('Arial', 18, 'italic'),
                        text="Film 1: " + str(film_details(0)[0]) + " Jaar: " + str(film_details(0)[1]) +
                             " Genre: " + str(film_details(0)[2]) + " IMDB Rating: " + str(film_details(0)[4]),
                        bd=5,
                        fg='#c4ad5a',
                        bg='#330d05')

    titel_lbl11.pack(anchor='w')
    titel_lbl21 = Label(master=beginscherm_beheer,
                        font=('Arial', 18, 'italic'),
                        text="Film 2: " + str(film_details(1)[0]) + " Jaar: " + str(film_details(1)[1]) +
                             " Genre: " + str(film_details(1)[2]) + " IMDB Rating: " + str(film_details(1)[4]),
                        bd=5,
                        fg='#c4ad5a',
                        bg='#330d05')

    titel_lbl21.pack(anchor='w')
    titel_lbl31 = Label(master=beginscherm_beheer,
                        font=('Arial', 18, 'italic'),
                        text="Film 3: " + str(film_details(2)[0]) + " Jaar: " + str(film_details(2)[1]) +
                             " Genre: " + str(film_details(2)[2]) + " IMDB Rating: " + str(film_details(2)[4]),
                        bd=5,
                        fg='#c4ad5a',
                        bg='#330d05'
                        )

    titel_lbl31.pack(anchor='w')

    titel_lbl41 = Label(master=beginscherm_beheer,
                        font=('Arial', 18, 'italic'),
                        text="Film 4: " + str(film_details(3)[0]) + " Jaar: " + str(film_details(3)[1]) +
                             " Genre: " + str(film_details(3)[2]) + " IMDB Rating: " + str(film_details(3)[4]),
                        bd=5,
                        fg='#c4ad5a',
                        bg='#330d05'
                        )
    titel_lbl41.pack(anchor='w')

    titel_lbl51 = Label(master=beginscherm_beheer,
                        font=('Arial', 18, 'italic'),
                        text="Film 5: " + str(film_details(4)[0]) + " Jaar: " + str(film_details(4)[1]) +
                             " Genre: " + str(film_details(4)[2]) + " IMDB Rating: " + str(film_details(4)[4]),
                        bd=5,
                        fg='#c4ad5a',
                        bg='#330d05'
                        )

    titel_lbl51.pack(anchor='w')

    leeg_lbl1 = Label(master=beginscherm_beheer,
                      bg='#330d05')
    leeg_lbl1.pack()

    toevoeg_knop = Button(master=beginscherm_beheer,
                          text="Voeg film toe",
                          font=('Arial', 14, 'bold'),
                          bg='#c4ad5a',
                          command=ga_verder)

    toevoeg_knop.pack()


def toon_detailscherm():
    beginscherm.pack_forget()
    detailscherm.pack()
    uitleg = str(film_details(entryy())[7])
    if "." not in uitleg:
        uitleg_overzicht = uitleg.split(',')
    else:
        uitleg_overzicht = uitleg.split('.')

    if entryy() >= 0:

        totaal_tekst = "Titel: " + str(film_details(entryy())[0]) + "\n"
        totaal_tekst += "Jaar: " + str(film_details(entryy())[1]) + "\n"
        totaal_tekst += "Genre(s): " + str(film_details(entryy())[2]) + "\n"
        totaal_tekst += "Duur: " + str(film_details(entryy())[3]) + "\n"
        totaal_tekst += "IMDB_rating: " + str(film_details(entryy())[4]) + "\n"
        totaal_tekst += "Land: " + str(film_details(entryy())[5]) + "\n"
        totaal_tekst += "Regisseur: " + str(film_details(entryy())[6]) + "\n"
        totaal_tekst += "Zender: " + str(film_details(entryy())[8]) + "\n"

        totaal_tekst += "Uitleg: \n"
        for regel in uitleg_overzicht:
            totaal_tekst += regel + "\n"

        detail_lbl = Label(master=detailscherm,
                           font=('Arial', 14),
                           text=totaal_tekst,
                           bg='#330d05',
                           fg='#c4ad5a')
        detail_lbl.pack(anchor='w')
        betaalknop = Button(master=detailscherm,
                            text="Bevestig en ga naar betaalscherm",
                            font=('Arial', 14, 'bold'),
                            bg='#45f442',
                            command=betalen
                            )
        betaalknop.pack()
    else:
        messagebox.showinfo(message="Voer geldig filmnummer in.")
        toon_beginscherm()


def entryy():
    keuze_film_entry = int(entry.get()) - 1

    return keuze_film_entry


def ga_verder():
    toon_detailscherm()
    entryy()


def betalen():
    toon_bevestiging()


def aanmaken():
    subject = StringVar()
    if True:
        global myQr
        myQr = pyqrcode.create(subject.get())
        myQr.png("QR_CODE_FILM.png", scale=6)
        qrImage = myQr.xbm(scale=6)
        global foto
        foto = BitmapImage(data=qrImage)
        messagebox.showinfo("Betaling geslaagd!", "U heeft betaald!")
        # als de betaling geslaagd is geeft hij dit aan.
    else:
        messagebox.showinfo("Error!", "Betaling mislukt! probeer het opnieuw!")
        # Als de box bij betalen niet wordt ingevuld print hij deze message.
    try:
        tooncode()
    except:
        pass


def tooncode():
    notificationLabel = Label(master=bevestigscherm)
    notificationLabel.pack()
    subLabel = Label(master=bevestigscherm, bg='#330d05', fg='#c4ad5a')
    subLabel.pack()

    global foto
    notificationLabel.config(image=foto)
    subLabel.config(text='Uw QR-code voor: ' + str(film_details(entryy())[0]))

# De QR code wordt weergeven.


def opslaan():
    keuze_film_entry = int(entry.get()) - 1
    txt = str(film_details(keuze_film_entry)[0])
    dir = os.getcwd() + "\\QR Codes/Users/donreijke/Desktop"

    if not os.path.exists(dir):
        os.makedirs(dir)
# Dit is het proces om de qr code op te slaan.


def toon_bevestiging():
    detailscherm.pack_forget()
    bevestigscherm.pack()
    subject = StringVar()
    lab1 = Label(master=bevestigscherm, text="Betaal voor uw QR-code", font=("Arial", 14, 'bold'),
                 bg='#330d05', fg='#c4ad5a')
    lab1.pack()

    # Balkje om de film in te voeren, sticky is er om de widget te vergroten.
    # Door dit toe te passen wordt deze tot alle kanten vergroot.

    maakQR = Button(master=bevestigscherm, text="Betaal", font=("Arial", 14), command=aanmaken, bg='#c4ad5a')
    maakQR.pack()

    showButton = Button(master=bevestigscherm, text="Uw QR code opslaan", font=("Arial", 14), command=opslaan,
                        bg='#c4ad5a')
    showButton.pack()


master_root = Tk()


beginscherm = Frame(master=master_root, bg='#330d05')
beginscherm.pack(fill='both', expand=True)

beginscherm_beheer = Frame(master=master_root, bg='#330d05')
beginscherm_beheer.pack(fill='both', expand=True)

lbl = Label(master=beginscherm,
            font=('Arial', 20),
            text='Kies uw film naar keuze:',
            fg='white',
            bg="#330d05",
            bd=5)
lbl.pack()
titel_lbl1 = Label(master=beginscherm,
                   font=('Arial', 18, 'italic'),
                   text="Film 1: " + str(film_details(0)[0]) + " Jaar: " + str(film_details(0)[1]) +
                        " Genre: " + str(film_details(0)[2]) + " IMDB Rating: " + str(film_details(0)[4]),
                   bd=5,
                   fg='#c4ad5a',
                   bg='#330d05')

titel_lbl1.pack(anchor='w')
titel_lbl2 = Label(master=beginscherm,
                   font=('Arial', 18, 'italic'),
                   text="Film 2: " + str(film_details(1)[0]) + " Jaar: " + str(film_details(1)[1]) +
                        " Genre: " + str(film_details(1)[2]) + " IMDB Rating: " + str(film_details(1)[4]),
                   bd=5,
                   fg='#c4ad5a',
                   bg='#330d05')

titel_lbl2.pack(anchor='w')
titel_lbl3 = Label(master=beginscherm,
                   font=('Arial', 18, 'italic'),
                   text="Film 3: " + str(film_details(2)[0]) + " Jaar: " + str(film_details(2)[1]) +
                        " Genre: " + str(film_details(2)[2]) + " IMDB Rating: " + str(film_details(2)[4]),
                   bd=5,
                   fg='#c4ad5a',
                   bg='#330d05'
                   )

titel_lbl3.pack(anchor='w')

titel_lbl4 = Label(master=beginscherm,
                   font=('Arial', 18, 'italic'),
                   text="Film 4: " + str(film_details(3)[0]) + " Jaar: " + str(film_details(3)[1]) +
                        " Genre: " + str(film_details(3)[2]) + " IMDB Rating: " + str(film_details(3)[4]),
                   bd=5,
                   fg='#c4ad5a',
                   bg='#330d05'
                   )
titel_lbl4.pack(anchor='w')

titel_lbl5 = Label(master=beginscherm,
                   font=('Arial', 18, 'italic'),
                   text="Film 5: " + str(film_details(4)[0]) + " Jaar: " + str(film_details(4)[1]) +
                        " Genre: " + str(film_details(4)[2]) + " IMDB Rating: " + str(film_details(4)[4]),
                   bd=5,
                   fg='#c4ad5a',
                   bg='#330d05'
                   )

titel_lbl5.pack(anchor='w')
entry = Entry(master=beginscherm,

              font=('Arial', 14, 'italic'),

              fg='black',
              text="\n")

entry.pack()

leeg_lbl = Label(master=beginscherm,
                 bg='#330d05')
leeg_lbl.pack()


volgende_knop = Button(master=beginscherm,
                       text="Ga verder",
                       font=('Arial', 14, 'bold'),
                       bg='#c4ad5a',
                       command=ga_verder)

volgende_knop.pack()

detailscherm = Frame(master=master_root, bg='#330d05')
detailscherm.pack(fill='both', expand=True)

bevestigscherm = Frame(master=master_root, bg='#330d05')
bevestigscherm.pack(fill='both', expand=True)

typescherm = Frame(master=master_root, bg='#330d05')
typescherm.pack(fill='both', expand=True)

toon_typescherm()
master_root.mainloop()
