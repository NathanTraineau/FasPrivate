#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import random


Resultats= [[1,23,30],[2,6,45],[1,52,45],[2,23,45],[1,23,45],[2,23,45],[1,23,58]]

def AffStatistiques(Resultats):
	 #Prend en paramètre une liste de tuple de résultats tel que chaque tuple
	 #soit composés d'un chiffre, une liste et un temps de pause en secondes
	 #1 pour pompe et 2 pour gainage
	 # le chiffre est un type d'exercice et donc selon le type la liste sera des répétitions en fonction d'un
	 # temps
	 #ou un nombre de fautes  en fonction temps tout court 
	 
	 #Cette fonction a pour but d'afficher le nombre de répétitions de pompe en fonction du temps
	 #
        
        # 1000 tirages entre 0 et 150
        seriesPompe=[]
        for i in Resultats :
            if i[0]==1:
                seriesPompe.append(i)
        seriesGainage=[]
        for i in Resultats :
            if i[0]==2:
                seriesGainage.append(i)
                
        AffichagePompes(seriesPompe)
        #AffichageGainage(serieGainage)
        return 0



def AffichagePompes(seriesPompes):
        l = seriesPompes
        NbPompes = []
        for i in l :
                NbPompes=NbPompes + [i[1]]
        m= max(NbPompes)
        print( m)
        print(NbPompes)
        n, bins, patches = plt.hist([NbPompes], len(l), normed=1, facecolor='b', alpha=1)
        plt.xlabel('Série')
        plt.ylabel('Pompes')
        plt.axis([0, len(l), 0, m])
        plt.grid(True)
        plt.show()
        return 0
                
def AffichageGainage(serieGainage):
        l = seriesGainage
        TempsGainage = []
        for i in l :
                TempsGainage= TempsGainage + [i[1]]
        m= max(TempsGainage)
        n, bins, patches = plt.hist(TempsGainage, len(l), normed=1, facecolor='b', alpha=0.5)
        plt.xlabel('Série')
        plt.ylabel('Gainage')
        plt.axis([0, len(l), 0, m])
        plt.grid(True)
        plt.show()
        return 0
AffStatistiques(Resultats)
                

