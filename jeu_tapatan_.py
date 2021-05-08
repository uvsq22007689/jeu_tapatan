########################################################
# Auteurs:
# Nabila Elaidoudi
# Marco Laurent De-Riemacker
# Gabriela Da Luz
# Abdul-Malik Suleiman
# Camelia Rili
# Groupe: BI 1
#https://github.com/uvsq22007689/jeu_tapatan.git
##########################################################

#####################
#import des modules
from tkinter import *

#####################
# constantes
LARGEUR= 300
HAUTEUR= 400


#####################
# fonctions

def tracePlateau():
    cadre.create_rectangle(50,100,250,300,width=5)
    cadre.create_line(50,100,250,300,width=5,fill="black")
    cadre.create_line(50,300,250,100,width=5,fill="black")
    cadre.create_line(50,200,250,200,width=5,fill="black")
    cadre.create_line(150,100,150,300,width=5,fill="black")
    for i in range (15) : 
        xt,yt=i%3*100+50, i//3*100 
        if i<3:yt+=50
        if i>11:yt-=50
        cadre.create_oval(xt-7, yt-7, xt+7, yt+7, width=5, fill="black")
        cadre.create_oval(xt-3, yt-3, xt+3, yt+3, width=0, fill="light yellow")

#####################
# programme principal
racine = Tk() #ouvre une fenetre 
racine.title('Jeu Tapatan')
cadre = Canvas(racine, bg="light yellow", width= LARGEUR  , height= HAUTEUR )
cadre.grid(row=1 , column=1,columnspan = 3)
tracePlateau()
photo1 = PhotoImage(file ='pion1.gif')
photo2 = PhotoImage(file = 'pion2.gif')
pion0,pion1 = [], []
for i in range(3):
    pion0.append(cadre.create_image(i*100+50,50, image = photo1))
    pion1.append(cadre.create_image(i*100+50,350, image = photo2))


racine.mainloop() #ferme une fenetre 


