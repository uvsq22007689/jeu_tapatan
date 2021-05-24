# jeu_tapatan

Un jeu simple à deux joueurs dont l'un des joueurs est l'ordinateur(IA) et qui
nécessite une forme d'intelligence de sa part : 

le jeu des neuf trous appelé aussi ' jeu du tapatan 'est une sorte de plateau de jeu formant
un Carrée de 3 sur 3, chaque joueur dispose de trois pions qu'il doit aligner sur le plateau. 
Au début, chacun à tour de rôle pose un pion, n'importe où sur le plateau. Une fois les six pions posés, chacun
peut déplacer un de ses pions d'une position, selon un des tracés figurés sur le plateau (le long des six
lignes ou des deux diagonales), si le nouvel emplacement est libre.
  

On dessine le plateau à l'aide d'un Canvas . Les pions sont créés à partir de deux
images photo1 et photo2 (au format gif) qui sont utilisées pour definir des variables pion0[0], pion0[1] et pion0[2] pour les trois pions de l'ordinateur (désigné par 0 pour ordinateur) et pion1[i] pour ceux de l'humain (i variant de 0 à 2 pour l'humain désigné par 1).
L'emplacement de ces pions est réglé par les coordonnées qui sont initialisées :
pion0.append(cadre.create_image(i*100+50,50,image=photo1))#ordinateur
pion1.append(cadre.create_image(i*100+50,350,image=photo2))#humain

Le mouvement des pions est lié aux mouvements de la souris en 3 étapes : 

 -le clic déclenche la fonction clic() qui détecte que le pion *choixPion* a été sélectionné (on ne s'intéresse qu'aux pions de l'humain car l'ordinateur bouge lui-même ses pions (automatiquement)) en acceptant un certain domaine de variation des coordonnées du clic (x.event et y.event) autour de coordonnées du pion.

 -le déplacement de la souris, bouton de gauche enfoncé, lance la fonction detection() qui redessine le pion lors de son déplacement

 -le relâchement de la souris lance la fonction lache() qui examine le nouvel emplacement, fixe le pion à cet
emplacement s'il est vide et s'il correspond à un placement valide

Le bouton « Rejouer » permet de rejouer une partie, ce qui repositionne les pions à l'extérieur du plateau et réinitialise les variables qui doivent l'être. 

On a crée une fonction racineMessage qui permet d'avertir que si on change le mode d'utilisation ( de jouer avec l'humain à jouer avec l'ordi)
alors les scores seront réinitialiser à 0 (car on n'utilise plus les mêmes règles) , celle ci va permettre de créer un bandeau d'avertissement.

Pour effacer le bandeau d'avertissement on a crée une nouvelle fonction supprimerMessage qui permet de l'effacer, et de faire reapparaitre le plateau de jeu.

Nous avons essayé de créer :

-une fonction IA() qui permet à l'ordinateur d'attaquer en premier lieu pour pouvoir gagner ou de se défendre si il se sent en position de défaite. Exemple : si l'humain met son pion au milieu l'ordinateur joue sur la diagonale.

-une fonction gagner() qui nous permettrai d'afficher les scores et de savoir qui des 2 joueurs auraient gagner.

-une fonction humain() pour parvenir à jouer avec un autre humain tout en calculant les cases disponibles, notre piste pour y parvenir était de créer une liste imbriquée : cases = [[0,0,0],[0,0,0],[0,0,0]] et d'utiliser des structures conditionnelles pour chaque case. 

-une fonction lache_du_pion() qui permet de détecter quand l'utilisateur lache le bouton gauche de la souris et à quelle coordonées pour placer le pion au niveau des cercles noirs prédéfinis.

-une fonction sauvegarde() qui doit présenter ces éléments :
fic = open("sauvegarde", "w")
fic.write("sauvegarde partie précédente ")
fic.close()

Mais nous n'avons pas réussi à faire ces fonctions par manque de connaissance.
