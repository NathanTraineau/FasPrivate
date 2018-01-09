#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Entrainements.Entrainements import *
from tkinter import *
from statistiques.Statistiques import *


#Exemple de code tkinter : 
class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        
        canvas = Canvas(fenetre, width=550, height=620, background='grey')
        # Création de nos widgets
        label = Label(fenetre, text="Bienvenue sur votre entraineur sportif !")
        label.pack()
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_manuel = Button(self, text="Manuel D'utilisation", fg="red",
                command=self.Manuel)
        self.bouton_manuel.pack(padx=10, pady = 10)

        self.bouton_entrainement1 = Button(self, text="entrainement 1", fg="red",
                command=self.entrainement1)
        self.bouton_entrainement1.pack(padx=10, pady = 10)

        self.bouton_entrainement2 = Button(self, text="entrainement 2", fg="red",
                command=self.entrainement2)
        self.bouton_entrainement2.pack(padx=10, pady = 10)

        self.bouton_entrainement3 = Button(self, text="entrainement 3", fg="red",
                command=self.entrainement3)
        self.bouton_entrainement3.pack(padx=10, pady = 10)

    
    def Manuel(self):

        Manuel.txt
    def entrainement1(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        
        en = entrainement1()
        AffStatistiques(en)
        return 0

    def entrainement2(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        
        en = entrainement2()
        AffStatistiques(en)
        return 0

    def entrainement3(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        
        en = entrainement3()
        AffStatistiques(en)
        return 0
        


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()







