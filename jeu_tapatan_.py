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

#####################
# constantes
LARGEUR= 500
HAUTEUR= 500


#####################
# fonctions

#####################
# programme principal
racine = tk.Tk() #ouvre une fenetre 

canvas = tk.Canvas(racine, bg="pink", width= LARGEUR  , height= HAUTEUR )
canvas.grid(row=1 , column=1 )

canvas.create_line((250, 0),(250, 500), fill = "white") #ligne de l'axe vertical 
canvas.create_line((0, 250), (500, 250),  fill="white") #ligne de l'axe horizontale
canvas.create_line((0,0), (500, 500) , fill="white") #ligne gauche
canvas.create_line((0,500), (500, 0) , fill="white") #ligne droite
canvas.create_oval((0 , 0 ), (0 +20, 0 +20 ) , fill= "black") #point gauche
canvas.create_oval((500 , 0 ), (500 -20 , 0 +20  ) , fill= "red") #point droit
canvas1 =tk.Canvas(racine, bg="white", width=10 , height=500) #mur de gauche
canvas1.grid(row=1 , column=0)
canvas2 =tk.Canvas(racine, bg="white", width=500 , height=10) #mur du dessous du canvas
canvas2.grid(row=2 , column=1)
canvas3 =tk.Canvas(racine, bg="white", width=10 , height=500) #mur de droite
canvas3.grid(column=2, row=1 )
canvas4 =tk.Canvas(racine, bg="white", width=500 , height=10) #mur du dessous du canvas
canvas4.grid(row=0 , column=1)



racine.mainloop() #ferme une fenetre 


