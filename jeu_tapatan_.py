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
from random import *

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
    
def commencement():
    '''cette fonction va permettre de remettre les compteurs à 0'''
    global coup,score,avertissement,previousChoix
    if coup!=0 and score != [0,0]:
        avertissement=True
        racineMessage('Attention! Le score va être perdu...')

def racineMessage(s): 
    '''fonction qui creer un bandeau d'avertissement pour prevenir la perte du score ''' 
    global band,message1,message2                           
    band = cadre.create_rectangle(5,75,298,325,width=3,fill='light yellow')    
    message1 = cadre.create_text(150,150,text=s,font="Britannic bold 12",fill='red')
    message2 = cadre.create_text(150,250,text='Cliquer ici pour valider ce choix'\
                            ,font="Britannic bold 11",fill='red')

def supprimerMessage(): 
    '''fonction va permettre d'effacer le bandeau d'avertissement et de faire 
    reapparaitre le plateau de jeu'''
    global coup, score,tour,band,message1,message2,avertissement
    score = [0,0]
    monScore.configure(text="0")
    ordiScore.configure(text="0")
    cadre.delete(band)
    cadre.delete(message1)
    cadre.delete(message2)
    avertissement=False
    rejouer()

def rejouer():
    '''fonction permet de démarrer une nouvelle partie '''
    global coup,resteAjouer,possible,start,detectionPion,choixPion,mesPlaces\
           ,ordiPlaces,tour,gagnant,avertissement,band,message1,message2,previousChoix
    for i in range(3):
        cadre.coords(pion0[i],i*100+50,50)
        cadre.coords(pion1[i],i*100+50,350)
    coup,resteAjouer,possible=0,[0,1,2],[]
    start,detectionPion,choixPion=True,False,-1
    mesPlaces,ordiPlaces,gagnant=[-1,-1,-1],[-1,-1,-1],-1
    if avertissement:
        cadre.delete(band)                                         
        cadre.delete(message1)
        cadre.delete(message2)
        choixDebut.set(previousChoix)
        avertissement=False
    previousChoix=choixDebut.get()
    for i in range(9):
         possible.append(True)
    if choixDebut.get()==0:
        tour=joueurDebut[0]
    elif choixDebut.get()==1:
        tour=joueurDebut[randint(0,2)]
    else:tour=joueurDebut[2]
    message.configure(text="à {} de jouer".format(tour))
    if tour=="l'ordi": 
        ordinateur()
    print('\nNouvelle partie')

def ordinateur():
    pass

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
joueurDebut=["l'ordi","aleatoire","l'humain"]
tour=joueurDebut[randint(0,2)]
for i in range(3):
    pion0.append(cadre.create_image(i*100+50,50, image = photo1))
    pion1.append(cadre.create_image(i*100+50,350, image = photo2))

pion0,pion1 = [], []
for i in range(3):
    pion0.append(cadre.create_image(i*100+50,50, image = photo1))
    pion1.append(cadre.create_image(i*100+50,350, image = photo2))

ordiScore=Label(racine,text="0")
ordiScore.grid(row=2,column=1)
message=Label(racine,text="à {} de jouer".format(tour))
message.grid(row=2,column=2)
monScore=Label(racine,text="0")
monScore.grid(row=2,column=3)
choixDebut=IntVar()
choixDebut.set(1)

for i in range(3): # Création des trois 'boutons radio' :
    bouton=Radiobutton(racine,text= joueurDebut[i],variable=choixDebut,
                       value=i,command=commencement)
    bouton.grid(row=3,column=i+1)

bouton=Button(racine,text="Rejouer")
bouton.grid(row=4,column=1,columnspan=3)

#initialisation des variables globales
start,detectionPion,avertissement=True,False,False
possible,coup,score,resteAjouer=[],0,[0,0],[0,1,2]
mesPlaces,ordiPlaces,choixPion=[-1,-1,-1],[-1,-1,-1],-1
xDeb,yDeb,gagnant,previousChoix=0,0,-1,1
band,message1,message2=None,None,None


for i in range(3):# Création des six pions :
    pion0.append(cadre.create_image(i*100+50,50,image=photo1))#ordi
    pion1.append(cadre.create_image(i*100+50,350,image=photo2))#humain
if tour == "l'ordi": 
    ordinateur()



racine.mainloop() #ferme une fenetre 


