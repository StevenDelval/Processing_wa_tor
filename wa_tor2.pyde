from random import choice, randint
from time import sleep

# variables globales du programme

nb_colonne=50
nb_ligne=50
temps_repro_poisson=1
temps_repro_requin=20
energie_req= 4
#nb_poisson=1000
#nb_requin=300

# classe qui gere la grille (planete)

class Planete:
    monde=[]

    nombre_de_case = nb_colonne*nb_ligne
    temps = 0

# classe qui gere les poissons

    class Poisson:

        nb_poisson = 0

        def __init__(self, positionX, positionY):
            """
            methode qui donne les coordonnes des poisson
            :param position X et Y:
            """
            self.positionX = positionX
            self.positionY = positionY
            self.reproduction = temps_repro_poisson
            Planete.Poisson.nb_poisson += 1

        def reproduction_poisson(self):
            '''
            Fonction qui permet de vérifier si le poisson peut se reproduire
            param: poisson
            return: poisson
            '''
            if self.reproduction <= 0:
                self.reproduction = temps_repro_poisson
                return True

            return False

        def choix_possible_poisson(self, monde):
            """
            Fonction qui renvoie les deplacement posible
            :param poisson:(obj) le poisson qui doit se deplacer
            :param monde: (liste) carte du monde
            return: (list) Choix possible
            """
            liste_choix = []

            if monde[(self.positionX + 1) % nb_ligne][(self.positionY) % nb_colonne] == "-":
                liste_choix.append([(self.positionX + 1) %
                                   nb_ligne, (self.positionY) % nb_colonne])

            if monde[(self.positionX - 1) % nb_ligne][(self.positionY) % nb_colonne] == "-":
                liste_choix.append([(self.positionX - 1) %
                                   nb_ligne, (self.positionY) % nb_colonne])

            if monde[(self.positionX) % nb_ligne][(self.positionY + 1) % nb_colonne] == "-":
                liste_choix.append(
                    [(self.positionX) % nb_ligne, (self.positionY + 1) % nb_colonne])

            if monde[(self.positionX) % nb_ligne][(self.positionY - 1) % nb_colonne] == "-":
                liste_choix.append(
                    [(self.positionX) % nb_ligne, (self.positionY - 1) % nb_colonne])

            return liste_choix

        def deplacement_poison(self, monde):
            """
            Fonction qui deplace le poisson
            :param poisson: (objet) le poisson
            :param monde: (liste) la carte du monde
            return: le poisson avec ses nouvelles coordonnées
            return: la carte
            """

            liste_dep = self.choix_possible_poisson(monde)

            if len(liste_dep) != 0:
                dep_choisi = liste_dep[randint(0, len(liste_dep)-1)]
                if self.reproduction_poisson():
                    monde[self.positionX][self.positionY] = Planete.Poisson(
                        self.positionX, self.positionY)
                    fill("#F7DC6F")
                    square(self.positionX*10,self.positionY*10,10)
                    noFill()
                else:
                    monde[self.positionX][self.positionY] = "-"
                    stroke(0,255,255)
                    fill(0,255,255)
                    square(self.positionX*10,self.positionY*10,10)
                    noFill()
                    stroke(0,0,0)

                self.positionX = dep_choisi[0]
                self.positionY = dep_choisi[1]
                monde[self.positionX][self.positionY] = self
            self.reproduction -= 1
            fill("#F7DC6F")
            square(self.positionX*10,self.positionY*10,10)
            noFill()

            return monde, self
        
# classe qui gere les requins

    class Requin:

        nb_requin = 0

        def __init__(self, positionX, positionY):
            """
            methode qui donne les coordonnes des poisson
            :param position X et Y:
            """
            self.positionX = positionX
            self.positionY = positionY
            self.reproduction = temps_repro_requin
            self.energie = energie_req
            Planete.Requin.nb_requin += 1

        def reproduction_requin(self):
            '''
            Fonction qui permet de vérifier si le requin peut se reproduire
            :param: requin
            return: boolean, Vrai si il peut se reproduire, Faux si il ne peut pas se repoduire
            '''
            if self.reproduction <= 0:
                self.reproduction = temps_repro_requin
                return True

            return False

        def is_dead(self):
            '''
            Fonction qui indique que le fait que le requin meurt au bout d'un certain nombre de tours lorsque son énergie est à 0.
            param (obj): requin
            return: (boolean): Vrai si le requin est mort. Faux sinon
            '''

            if self.energie == 0:
                return True

            return False

        def manger(self, poisson, monde, liste):
            '''
            Fonction qui permet de simuler l'action du requin qui mange un poisson
            param: requin,poisson
            return: requin
            '''
            if poisson in liste:
                liste.remove(poisson)
            for ligne in monde:
                if poisson in ligne:
                    ligne.insert(poisson.positionY, self)
                    ligne.remove(poisson)
            Planete.Poisson.nb_poisson -= 1
            self.energie += 2
            
            return monde, liste

        def choix_possible_requin(self, monde):
            """
            Fonction qui renvoie les deplacement posible des requins
            :param poisson:(obj) le requin qui doit se deplacer
            return: (list) choix possible avec les poissons
            return: liste sans poissons
            """
            liste_choix = []
            liste_poisson = []

            if monde[(self.positionX + 1) % nb_ligne][(self.positionY) % nb_colonne] == "-":
                liste_choix.append([(self.positionX + 1) %
                                   nb_ligne, (self.positionY) % nb_colonne])
            elif isinstance(monde[(self.positionX + 1) % nb_ligne][(self.positionY) % nb_colonne], Planete.Poisson):
                liste_poisson.append([(self.positionX + 1) %
                                      nb_ligne, (self.positionY) % nb_colonne])

            if monde[(self.positionX - 1) % nb_ligne][(self.positionY) % nb_colonne] == "-":
                liste_choix.append([(self.positionX - 1) %
                                   nb_ligne, (self.positionY) % nb_colonne])

            elif isinstance(monde[(self.positionX - 1) % nb_ligne][(self.positionY) % nb_colonne], Planete.Poisson):
                liste_poisson.append([(self.positionX - 1) %
                                      nb_ligne, (self.positionY) % nb_colonne])

            if monde[(self.positionX) % nb_ligne][(self.positionY + 1) % nb_colonne] == "-":
                liste_choix.append(
                    [(self.positionX) % nb_ligne, (self.positionY + 1) % nb_colonne])
            elif isinstance(monde[(self.positionX) % nb_ligne][(self.positionY + 1) % nb_colonne], Planete.Poisson):
                liste_poisson.append(
                    [(self.positionX) % nb_ligne, (self.positionY + 1) % nb_colonne])

            if monde[(self.positionX) % nb_ligne][(self.positionY - 1) % nb_colonne] == "-":
                liste_choix.append(
                    [(self.positionX) % nb_ligne, (self.positionY - 1) % nb_colonne])
            elif isinstance(monde[(self.positionX) % nb_ligne][(self.positionY - 1) % nb_colonne], Planete.Poisson):
                liste_poisson.append(
                    [(self.positionX) % nb_ligne, (self.positionY - 1) % nb_colonne])

            return liste_poisson, liste_choix

        def deplacement_requin(self, monde, liste):
            """
            Fonction qui deplace le requin
            :param monde:(liste) la carte du monde
            :param (liste) avec tous les poissons et tous les requins 
            """

            liste_dep_opti, liste_case_vide_ou_requin = self.choix_possible_requin(
                monde)
            if self.is_dead():
                for ligne in monde:
                    if self in ligne:
                        ligne.insert(self.positionY, "-")
                        ligne.remove(self)
                        liste.remove(self)
                        stroke(0,255,255)
                        fill(0,255,255)
                        square(self.positionX*10,self.positionY*10,10)
                        noFill()
                        stroke(0,0,0)
                Planete.Requin.nb_requin -= 1
                return monde, self,liste

            elif len(liste_dep_opti) != 0:
                dep_choisi = liste_dep_opti[randint(0, len(liste_dep_opti)-1)]
                monde, liste = self.manger(monde[dep_choisi[0]][dep_choisi[1]], monde, liste)
                if self.reproduction_requin():
                    monde[self.positionX][self.positionY] = Planete.Requin(
                        self.positionX, self.positionY)
                    fill("#AF7AC5")
                    square(self.positionX*10,self.positionY*10,10)
                    noFill()
                else:
                    monde[self.positionX][self.positionY] = "-"
                    stroke(0,255,255)
                    fill(0,255,255)
                    square(self.positionX*10,self.positionY*10,10)
                    noFill()
                    stroke(0,0,0)

                self.positionX = dep_choisi[0]
                self.positionY = dep_choisi[1]
                monde[self.positionX][self.positionY] = self

            elif len(liste_case_vide_ou_requin) != 0:
                dep_choisi = liste_case_vide_ou_requin[randint(0, len(liste_case_vide_ou_requin)-1)]
                if self.reproduction_requin():
                    monde[self.positionX][self.positionY] = Planete.Requin(
                        self.positionX, self.positionY)
                    fill("#AF7AC5")
                    square(self.positionX*10,self.positionY*10,10)
                    noFill()
                else:
                    monde[self.positionX][self.positionY] = "-"
                    fill(0,255,255)
                    stroke(0,255,255)
                    square(self.positionX*10,self.positionY*10,10)
                    noFill()
                    stroke(0,0,0)

                self.positionX = dep_choisi[0]
                self.positionY = dep_choisi[1]
                monde[self.positionX][self.positionY] = self
            self.reproduction -= 1
            self.energie -= 1
            fill("#AF7AC5")
            square(self.positionX*10,self.positionY*10,10)
            noFill()

            return monde, self,liste

# creation plateau

Planete.monde= [[choice([Planete.Poisson(x,y),Planete.Poisson(x,y),Planete.Poisson(x,y),"-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",Planete.Requin(x,y)]) for y in range(nb_colonne)] for x in range(nb_ligne)]

# recalcule le nombre des poisson et des requins

for i in Planete.monde:
        for j in i:
            if isinstance(j,Planete.Poisson):
                Planete.Poisson.nb_poisson -=2
            if not isinstance(j,Planete.Poisson):
                Planete.Poisson.nb_poisson -=3
            if not isinstance(j,Planete.Requin):
                Planete.Requin.nb_requin -=1
"""def generation(monde,nb_poisson,nb_requin):
    global nb_ligne
    global nb_colonne
    while nb_poisson != 0 and nb_requin !=0:
        for ligne in range(nb_ligne):
            for colonne in range(nb_colonne):
                if monde[ligne][colonne] == "-":
                    monde[ligne][colonne]=choice([ Planete.Poisson(ligne,colonne),"-", Planete.Requin(ligne,colonne)])
                    if isinstance(monde[ligne][colonne], Planete.Poisson) and nb_poisson !=0:
                        Planete.Requin.nb_requin -= 1
                        nb_poisson -=1
                    elif isinstance(monde[ligne][colonne], Planete.Requin) and nb_requin !=0:
                        Planete.Poisson.nb_poisson -= 1
                        nb_requin -=1
                    else:
                        monde[ligne][colonne]="-"
                        Planete.Poisson.nb_poisson -= 1
                        Planete.Requin.nb_requin -= 1
    return monde
"""

# PROCESSING
# initialisation du monde        

def setup():
    global nb_ligne
    global nb_colonne
    global nb_poisson
    global nb_requin
    size(nb_colonne *10+5 ,nb_ligne *10+5)
    background(0,255,255)
    
    #Planete.monde=generation(Planete.monde,nb_poisson,nb_requin)
    print("il ya :",Planete.Poisson.nb_poisson,"Poisson","il ya :",Planete.Requin.nb_requin ,"Requin" )

    # creation visuel des poissons et des requins

    liste=[]
    for i in Planete.monde:
        for j in i:
            if j != "-":
                liste.append(j)
    for i in liste:
        if isinstance(i,Planete.Poisson):
            fill("#F7DC6F")
            square(i.positionX*10,i.positionY*10,10)
            noFill()
        elif isinstance(i,Planete.Requin):
            fill("#AF7AC5")
            square(i.positionX*10,i.positionY*10,10)
            noFill()
    sleep(5)
        
compteur = 1

# affichage de chaque tour

def draw():
    global compteur
    background(0,255,255)
    liste_pop = []
    for i in Planete.monde:
        for j in i:
            if j != "-":
                liste_pop.append(j)  
    if len(liste_pop) ==0:
        noLoop()
    for i in liste_pop:
        if isinstance(i, Planete.Poisson):
            Planete.monde, i = i.deplacement_poison(Planete.monde)
            
        elif isinstance(i, Planete.Requin):
            Planete.monde, i,liste_pop = i.deplacement_requin(Planete.monde, liste_pop) 
    

    print("fin tour n ",compteur, "il ya :",Planete.Poisson.nb_poisson,"Poisson","il ya :",Planete.Requin.nb_requin ,"Requin" )
    compteur +=1
