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
import tkinter as tk
from tkinter import *
from random import randint
import random as rd

#####################
# constantes
LARGEUR= 300
HAUTEUR= 400

#####################
# fonctions
def commencement():
    """cette fonction va permettre de remettre les compteurs à 0"""
    global coup,score,avertissement,previousChoix        
 
    if coup!=0 and score!=[0,0]:
        avertissement=True
        racineMessage('Attention! Le score va etre perdu...')

def racineMessage(s):
    """fonction qui créer un bandeau d'avertissement pour prevenir la perte du score """
    global band,message1,message2                            
    band=canvas.create_rectangle(5,75,298,325,width=3,fill='light yellow')    
    message1=canvas.create_text(150,150,text=s,font="Britannic bold 12",fill='red')
    message2=canvas.create_text(150,250,text='Cliquer ici pour valider ce choix'\
                            ,font="Britannic bold 11",fill='red')

def supprimerMessage():
    """fonction va permettre d'effacer le bandeau d'avertissement et 
    de faire reapparaitre le plateau de jeu"""
    global coup,score,tour,band,message1,message2,avertissement   
    score=[0,0]
    monScore.configure(text="0")
    ordiScore.configure(text="0")
    canvas.delete(band)
    canvas.delete(message1)
    canvas.delete(message2)
    avertissement=False
    rejouer()

def rejouer():
    """fonction permet de démarrer une nouvelle partie"""
    global coup,resteAjouer,possible,start,detectionPion,choixPion,mesPlaces\
           ,ordiPlaces,tour,gagnant,avertissement,band,message1,message2,previousChoix
    for i in range(3):
        canvas.coords(pion0[i],i*100+50,50)
        canvas.coords(pion1[i],i*100+50,350)
    coup,resteAjouer,possible=0,[0,1,2],[]
    start,detectionPion,choixPion=True,False,-1
    mesPlaces,ordiPlaces,gagnant=[-1,-1,-1],[-1,-1,-1],-1
    if avertissement:
        canvas.delete(band)                                          
        canvas.delete(message1)
        canvas.delete(message2)
        choixDebut.set(previousChoix)
        avertissement=False
    previousChoix=choixDebut.get()
    for i in range(9):
         possible.append(True)
    if choixDebut.get()==0:
        tour=joueurDebut[0]
    elif choixDebut.get()==1:
        tour=joueurDebut[randint(0,1)]
    else:tour=joueurDebut[2]
    message.configure(text="à {} de jouer".format(tour))

def IA(): 
    pass

def clic(event):
    """fonction qui permet de detecter que le pion a ete selctionner
     pour le deplacement"""
    global detectionPion,choixPion,xDeb,yDeb,gagnant,avertissement
    x1,y1,detectionPion=event.x,event.y,False
    if avertissement and 0<x1<300 and 70<y1<330: supprimerMessage()         
    if tour=="l'humain" and gagnant==-1:
        for i in range(3):
            [xDeb,yDeb]=canvas.coords(pion1[i])
            if (x1-xDeb)**2+(y1-yDeb)**2<400:#estimation du rayon du pion à 20
                choixPion=i
                if start and resteAjouer.count(choixPion)==0 :
                    choixPion=-1
                    break
                detectionPion=True
                break

def detection(event):
    """fonction que redessine le deplacement du pion entre autre la detection 
    de son deplacement"""
    x1,y1=event.x,event.y
    if detectionPion:
        if x1<0:x1=0
        if x1>300:x1=300                      
        if y1<50:y1=50
        if y1>350:x1=350
        canvas.coords(pion1[choixPion],x1,y1)

def lache_du_pion(event):
    pass

def humain():
    pass

def gagner():
    pass

# programme principal
racine = tk.Tk() #ouvre une fenetre 
racine.title('Jeu Tapatan')
joueurDebut=["IA","l'humain"]
tour=joueurDebut[randint(0,1)]
canvas = tk.Canvas(racine, bg="pink", width= LARGEUR  , height= HAUTEUR )
canvas.grid(row=1,column=1,columnspan=3)
canvas.bind("<Button-1>",clic)
canvas.bind("<B1-Motion>",detection)

canvas.create_line(50,100,250,300, fill = "white") #ligne de l'axe vertical 
canvas.create_line(50,300,250,100,  fill="white") #ligne de l'axe horizontale
canvas.create_line(50,200,250,200 , fill="white") #ligne gauche
canvas.create_line(150,100,150,300 , fill="white") #ligne droite

for i in range(15):
        xt,yt=i%3*100+50,i//3*100
        if i<3:yt+=50
        if i>11:yt-=50
        
        canvas.create_oval(xt-7,yt-7,xt+7,yt+7,width=5,fill='black')
        canvas.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='pink')
ordiScore=Label(racine,text="0")
ordiScore.grid(row=2,column=1)
message=Label(racine,text="à {} de jouer".format(tour))
message.grid(row=2,column=2)
monScore=Label(racine,text="0")
monScore.grid(row=2,column=3)
choixDebut=IntVar()
choixDebut.set(1)

for i in range(2): # Création des trois 'boutons radio' :
    bouton=Radiobutton(racine,text=joueurDebut[i],variable=choixDebut,
                       value=i,command=commencement)
    bouton.grid(row=3,column=i+1)
bouton=Button(racine,text="Rejouer", command=rejouer)
bouton.grid(row=4,column=1,columnspan=3)
photo1 = PhotoImage(file ='pion1.gif')
photo2 = PhotoImage(file = 'pion2.gif')
pion0,pion1 = [], []

for i in range(3):# Création des six pions :
    pion0.append(canvas.create_image(i*100+50,50,image=photo1))#IA
    pion1.append(canvas.create_image(i*100+50,350,image=photo2))#humain
  
#initialisations des variables globales
start,detectionPion,avertissement=True,False,False
possible,coup,score,resteAjouer=[],0,[0,0],[0,1,2]
mesPlaces,ordiPlaces,choixPion=[-1,-1,-1],[-1,-1,-1],-1
xDeb,yDeb,gagnant,previousChoix=0,0,-1,1
band,message1,message2=None,None,None

racine.mainloop()


