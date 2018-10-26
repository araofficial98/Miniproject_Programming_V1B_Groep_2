from Film_details import *
from tkinter import *
import tkinter.messagebox as box

master_root = Tk()
root = Frame(master=master_root)
root.pack(side=LEFT)
root2 = Frame(master=master_root)
root2.pack(side=BOTTOM)


titel_lbl = Label(master=root,
                  font=('Arial', 18, 'italic'),
                  text="Film 1: " + str(film_details(0)[0]) + " Jaar: " + str(film_details(0)[1]) +
                       " Genre: " + str(film_details(0)[2]) + " Duur: " + str(film_details(0)[3]) +
                       " IMDB Rating: " + str(film_details(0)[4]) + "\n")

titel_lbl.grid(row=0, column=0, pady=4, padx=100)

filmnummer = 0
invoer = Entry(master=root)
invoer.focus_set()
invoer.get()



knop = Button(master=root,
              font=('Arial', 20, 'bold'),
              text='Kies Film')
knop.grid(pady=12)


root.mainloop()
