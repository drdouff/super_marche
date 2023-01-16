from cProfile import label
from tkinter import *
from tkinter import messagebox, ttk
import tempfile
import random
from time import strftime
from PIL import ImageTk, Image
import os


class SuperMarche:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Marche")
        self.root.geometry("1920x1040+0+0")

        title = Label(self.root, text="Super Marche Arnold Djoko", font=("Algerian", 45), bg="cyan", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            heur = strftime("%H:%M:%S")
            lbheure.config(text=heur)
            lbheure.after(1000, heure)

        lbheure = Label(self.root, text="HH:MM:SS", font=("times new roman", 15, "bold"), bg="cyan", fg="black")
        lbheure.place(x=0, y=25, width=120, height=45)

        heure()

        Main_frame = Frame(self.root, bd=2, relief=GROOVE, bg='white')
        Main_frame.place(x=10, y=100, width=1890, height=920)

        #client
        client_frame = LabelFrame(Main_frame, text="Client", font=("times new roman", 15), bg="white")
        client_frame.place(x=10, y=5, width=450, height=150)

        self.lbl_contact = Label(client_frame, text='Contact', font=("times new roman", 15, "bold"), bg="white")
        self.lbl_contact.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_nomclient = Label(client_frame, text='Nom Client', font=("times new roman", 15, "bold"), bg="white")
        self.lbl_nomclient.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_email = Label(client_frame, text='Email', font=("times new roman", 15, "bold"), bg="white")
        self.lbl_email.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_contact = ttk.Entry(client_frame, font=("times new roman", 15))
        self.txt_contact.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.txt_nomclient = ttk.Entry(client_frame, font=("times new roman", 15))
        self.txt_nomclient.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.txt_email = ttk.Entry(client_frame, font=("times new roman", 15))
        self.txt_email.grid(row=2, column=1, sticky=W, padx=5, pady=2)


if __name__ == "__main__":
    root = Tk()
    obj = SuperMarche(root)
    root.mainloop()
