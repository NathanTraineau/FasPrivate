#!/usr/bin/env python
#-*- coding: utf-8 -*- 
from grove.grovepi import *
from Bouton.Bouton import *
import time 



def chronometre():
	tZero=time.time() #Recuperation de tZero
	t=time.time() -tZero # Temps apres tZero
	a = BoutonStop()
	while not a : # temps total du chrono
	    t=time.time() -tZero
	        # Cree un temps en seconde 4.84287779592 (0=01/01/1970)
	 
	    tiTuple=time.gmtime(t)
	        # Conversion en tuple (1970, 1, 1, 0, 0, 4, 3, 1, 0) 
	 
	    reste=t-tiTuple[3]*3600.0-tiTuple[4]*60.0-tiTuple[5]*1.0
	        # Recupération du reste    
	 
	    resteS=("%.2f" % reste )[-2::]
	        #Affiche les dixièmes et centièmes de l'arrondi ex: 84
	 
	    tt=time.strftime("%H:%M:%S", tiTuple)+","+resteS
	    setText(tt)
	    time.sleep(0.01) #Attente en seconde
	return tt

print(chronometre())
 
