from Film_details import *
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyqrcode
import os
import png
import csv


def toon_loginscherm():
    beginscherm.pack_forget()
    beginscherm_beheer.pack_forget()
    loginscherm.pack()


def toon_beginscherm():
    detailscherm.forget
    detailscherm.pack_forget()
    loginscherm.pack_forget()
    beginscherm.pack()


def toon_toevoegscherm():
    detailscherm.pack_forget()
    beginscherm_beheer.pack_forget()
    loginscherm.pack_forget()
    toevoegscherm.pack()


def toon_beginscherm_beheer():
    detailscherm.pack_forget()
    beginscherm_beheer.pack()
    loginscherm.pack_forget()
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
                          text="Toon bezoekers",
                          font=('Arial', 14, 'bold'),
                          bg='#c4ad5a',
                          command=toon_gebruikers)

    toevoeg_knop.pack()

    terug_knop = Button(master=beginscherm_beheer,
                          text="Terug",
                          font=('Arial', 14, 'bold'),
                          bg='#c4ad5a',
                          command=toon_loginscherm)
    terug_knop.pack()


def toon_detailscherm():
    detailscherm.pack_forget()
    beginscherm.pack_forget()
    detailscherm.pack()
    loginscherm.pack_forget()
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
        detail_lbl.pack(anchor='w', expand=True, fill=BOTH)

        betaalknop = Button(master=detailscherm,
                            text="Bevestig en ga naar betaalscherm",
                            font=('Arial', 14, 'bold'),
                            bg='#45f442',
                            command=betalen
                            )
        betaalknop.pack()

        terug_knop2 = Button(master=detailscherm,
                            text="Terug",
                            font=('Arial', 14, 'bold'),
                            bg='#c4ad5a',
                            command=toon_beginscherm)
        terug_knop2.pack()
    else:
        messagebox.showinfo(message="Voer geldig filmnummer in.")
        toon_beginscherm()


def login():
    gebruikersnaam1 = gebruiker_1.get()
    mail1 = email_1.get()
    if gebruikersnaam1 and ' ' not in gebruikersnaam1 and '@' in mail1 and ' ' not in mail1 and '.' in mail1:
        box.showinfo('info', 'Welkom Gebruiker')
        toon_beginscherm()
    else:
        box.showinfo('info', 'Foutieve Login!')


def login_beheer():
    box.showinfo('info', 'Welkom Beheerder')
    toon_beginscherm_beheer()


def entryy():
    keuze_film_entry = int(entry.get()) - 1

    return keuze_film_entry


def writer():
    gebruikersnaam = gebruiker_1.get()
    mail = email_1.get()
    with open('database.csv', 'a', newline='') as myfile:
        writer = csv.writer(myfile, delimiter=';')
        writer.writerow((gebruikersnaam, mail, str(film_details(entryy())[0])))
        myfile.close()


def ga_verder():
    if entry.get() in "12345":

        try:
            toon_detailscherm()
            entryy()

        except:
            boxx = messagebox
            boxx.showinfo('Fout', 'Foute invoer, probeer opnieuw')
            toon_beginscherm()
    else:
        boxx = messagebox
        boxx.showinfo('Fout', 'Foute invoer, probeer opnieuw')
        toon_beginscherm()


def betalen():
    toon_bevestiging()
    writer()


def aanmaken():
    gebruikersnaam2 = gebruiker_1.get()
    global my_qr
    my_qr = pyqrcode.create("Bewijs: " + gebruikersnaam2)
    my_qr.png("QR_CODE_FILM.png", scale=6)
    qr_image = my_qr.xbm(scale=6)
    global foto
    foto = BitmapImage(data=qr_image)
    messagebox.showinfo("Betaling geslaagd!", "U heeft betaald!")
    tooncode()


def toon_gebruikers():
    file = open('database.csv', 'r')
    lines = file.read()
    q = lines.splitlines()

    box_gebruikers = messagebox
    box_gebruikers.showinfo("Gebruikers", q)
    file.close()


def tooncode():
    mail2 = email_1.get()
    gebruikersnaam2 = gebruiker_1.get()
    notification_label = Label(master=bevestigscherm)
    notification_label.pack()
    sublabel = Label(master=bevestigscherm, bg='#330d05', fg='#c4ad5a')
    sublabel.pack()

    global foto
    notification_label.config(image=foto, text="Naam: " + gebruikersnaam2 + " Mail: " + mail2)
    sublabel.config(text=gebruikersnaam2 +' zijn/haar QR-code voor: ' + str(film_details(entryy())[0]))

# De QR code wordt weergeven.


def opslaan():
    keuze_film_entry = int(entry.get()) - 1
    txt = str(film_details(keuze_film_entry)[0]) + ".png"
    my_qr.png(txt, scale=6)

# Dit is het proces om de qr code op te slaan.


def toon_bevestiging():
    detailscherm.pack_forget()
    bevestigscherm.pack()
    lab1 = Label(master=bevestigscherm, text="Betaal voor uw QR-code", font=("Arial", 14, 'bold'),
                 bg='#330d05', fg='#c4ad5a')
    lab1.pack()

    # Balkje om de film in te voeren, sticky is er om de widget te vergroten.
    # Door dit toe te passen wordt deze tot alle kanten vergroot.

    maak_qr = Button(master=bevestigscherm, text="Betaal", font=("Arial", 14), command=aanmaken, bg='#c4ad5a')
    maak_qr.pack()

    showbutton = Button(master=bevestigscherm, text="Uw QR code opslaan", font=("Arial", 14), command=opslaan,
                        bg='#c4ad5a')
    showbutton.pack()

    terug_knop3 = Button(master=bevestigscherm,
                         text="Terug",
                         font=('Arial', 14, 'bold'),
                         bg='#c4ad5a',
                         command=toon_detailscherm)
    terug_knop3.pack()


master_root = Tk()

box = messagebox

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

terug_knop1 = Button(master=beginscherm,
                     text="Terug",
                     font=('Arial', 14, 'bold'),
                     bg='#c4ad5a',
                     command=toon_loginscherm)
terug_knop1.pack()

detailscherm = Frame(master=master_root, bg='#330d05')
detailscherm.pack(fill='both', expand=True)

bevestigscherm = Frame(master=master_root, bg='#330d05')
bevestigscherm.pack(fill='both', expand=True)

toevoegscherm = Frame(master=master_root, bg='#330d05')
toevoegscherm.pack(fill='both', expand=True)


loginscherm = Frame(master=master_root, bg='#330d05')
loginscherm.pack(fill='both', expand=True)

Label1 = Label(master=loginscherm, text='Gebruiker:', fg='#c4ad5a', bg='#330d05', font=('Arial', 14))
Label1.pack(padx=15, pady=5)
gebruiker_1 = Entry(master=loginscherm, bd=5)
gebruiker_1.pack(padx=15, pady=5)

Label2 = Label(master=loginscherm, text='Email: ', fg='#c4ad5a', bg='#330d05', font=('Arial', 14))
Label2.pack(padx=15, pady=6)
email_1 = Entry(master=loginscherm, bd=5)
email_1.pack(padx=15, pady=7)


btn = Button(master=loginscherm, text='Login als gebruiker', command=login, bg='#c4ad5a', font=('Arial', 14, 'bold'))
btn.pack(padx=5)

btn_beheer = Button(master=loginscherm, text='Bent u aanbieder?', command=login_beheer,
                    bg='#c4ad5a', font=('Arial', 14, 'bold'))
btn_beheer.pack(padx=5)

toon_loginscherm()
master_root.mainloop()
