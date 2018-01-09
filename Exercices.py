#!/usr/bin/env python
#-*- coding: utf-8 -*-


from grovepi import *
import time
from Affichage import *


ultrasonic_ranger = 4
buzzer = 7 #On met le buzzer sur le port D8

# DistancePompeValide = 150

def Pompe(Bas,Haut):
    #
    #detecte si une pompe se fait et renvoie True si elle est effectuee
    #Si l'util est suffisemment bas, bip, si après avoir été bas il est 
    #suffisemment haut par rapport à la mesure haut alors bip et compte une pompe
            nbPompe=0
    #distance pour laquelle on est suffisamment bas

            dist = ultrasonicRead(ultrasonic_ranger)
            if (dist<Bas) :
                    digitalWrite(buzzer,1)
                    time.sleep(0.6)
                    digitalWrite(buzzer,0)
                    #buzz qd pompe valide en bas 
                    
                    
                    #Valeur haut-40 à regler pour que ca soit adapté à une pompe
                    while True :
                        
                        #Si fait pas bien la pompe et remonte pas suffisemment
                        #alors la pompe ne sera pas comptee.
                        #si il redescend sans être allé sufissamment haut alors pas de bip
                        #et la pompe n'est pas comptée ( sort du while et renvoie False) 
                        
                     

                        dist = ultrasonicRead(ultrasonic_ranger)
                        if (dist > Haut and dist < Haut + 10) :
                            digitalWrite(buzzer,1)
                            time.sleep(0.5)
                            
                            #buzz qd pompe valide en haut
                            return True
                            #renvoie true si la pompe est validé donc si 
                            #l'utilisateur est allé suffisamment haut après
                            #être allé sufisamment bas
            digitalWrite(buzzer,0)        
                            
            
            #Après une pompe on attend 0 seconde pour en refaire une 

            return False
                        
        



def ControleGainage(DistanceValide):
    #Emet un bruit de 1 seconde lorsque l'utillisateur a une mauvaise position ce qui equivaut a etre en dehors de l'intervalle de 10cm autour de la valeur DitanceValide

    #Retourne le temps de gainage
    #qui correspond soit à 2 si il y a eu faute soit 1 sinon
   temps = 0     
   dist = ultrasonicRead(ultrasonic_ranger)
   if (dist > (DistanceValide + 2) or (dist < DistanceValide - 2) ):
     #regarder cb vaut 1 d'acard en cm
     digitalWrite(buzzer,1)
     Affichage("Mauvaise Position")
     time.sleep(2)
     digitalWrite(buzzer,0)
     temps = temps + 2

   else :
      digitalWrite(buzzer,0)
      Affichage("Bonne Position")
      time.sleep(0.5)
      temps = temps + 0.5

    #   except KeyboardInterrupt:
    # digitalWrite(buzzer, 0)
    #     break
    #   except DemandeUtil() != True:
    #       digitalWrite(buzzer, 0)
   return temps
        


def PriseDeMesure():
    #Prend une mesure en la renvoie
    # AffichageMesurePompe():
    #while ask != True :
        dist = ultrasonicRead(ultrasonic_ranger)
       
            # ask == BoutonUtil()
        return dist
    





