from random import choice, randint
from time import sleep

nb_colonne = int(input("Nombre de colonne : ") or 5)
nb_ligne = int(input("Nombre de ligne : ") or 5)
temps_repro_poisson = int(input("Temps de repro des poissons : ") or 4)
temps_repro_requin = int(input("Temps de repro des requins :") or 4)
energie_req = int(input("Energie requins :") or 2)
nb_poisson=int(input("Nombre de poisson :") or 20)
nb_requin=int(input("Nombre de requin :") or 20)


class Planete:

    nombre_de_case = nb_colonne*nb_ligne
    temps = 0

    class Poisson:

        nb_poisson = 0

        def __init__(self, positionX, positionY):
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

        def choix_possible_poisson(poisson, monde):
            """
            Fonction qui renvoie les deplacement posible
            param poisson:(obj) le poisson qui doit se deplacer
            return: (list) Choix possible
            """
            liste_choix = []

            if monde[(poisson.positionX + 1) % nb_ligne][(poisson.positionY) % nb_colonne] == "-":
                liste_choix.append([(poisson.positionX + 1) %
                                   nb_ligne, (poisson.positionY) % nb_colonne])

            if monde[(poisson.positionX - 1) % nb_ligne][(poisson.positionY) % nb_colonne] == "-":
                liste_choix.append([(poisson.positionX - 1) %
                                   nb_ligne, (poisson.positionY) % nb_colonne])

            if monde[(poisson.positionX) % nb_ligne][(poisson.positionY + 1) % nb_colonne] == "-":
                liste_choix.append(
                    [(poisson.positionX) % nb_ligne, (poisson.positionY + 1) % nb_colonne])

            if monde[(poisson.positionX) % nb_ligne][(poisson.positionY - 1) % nb_colonne] == "-":
                liste_choix.append(
                    [(poisson.positionX) % nb_ligne, (poisson.positionY - 1) % nb_colonne])

            return liste_choix

        def deplacement_poison(self, monde):
            """
            Fonction qui deplace le poisson
            param poisson:
            """

            liste_dep = self.choix_possible_poisson(monde)

            if len(liste_dep) != 0:
                dep_choisi = liste_dep[randint(0, len(liste_dep)-1)]
                if self.reproduction_poisson():
                    monde[self.positionX][self.positionY] = Planete.Poisson(
                        self.positionX, self.positionY)
                else:
                    monde[self.positionX][self.positionY] = "-"

                self.positionX = dep_choisi[0]
                self.positionY = dep_choisi[1]
                monde[self.positionX][self.positionY] = self
            self.reproduction -= 1

            return monde, self

    class Requin:

        nb_requin = 0

        def __init__(self, positionX, positionY):
            self.positionX = positionX
            self.positionY = positionY
            self.reproduction = temps_repro_requin
            self.energie = energie_req
            Planete.Requin.nb_requin += 1

        def reproduction_requin(self):
            '''
            Fonction qui permet de vérifier si le requin peut se reproduire
            param: requin
            return: requin
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
            Fonction qui renvoie les deplacement posible
            :param poisson:(obj) le requin qui doit se deplacer
            return: (list) choix possible
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
            :param monde:
            """

            liste_dep_opti, liste_case_vide_ou_requin = self.choix_possible_requin(
                monde)
            if self.is_dead():
                for ligne in monde:
                    if self in ligne:
                        ligne.insert(self.positionY, "-")
                        ligne.remove(self)
                        liste.remove(self)
                Planete.Requin.nb_requin -= 1

            elif len(liste_dep_opti) != 0:
                dep_choisi = liste_dep_opti[randint(0, len(liste_dep_opti)-1)]
                monde, liste = self.manger(monde[dep_choisi[0]][dep_choisi[1]], monde, liste)
                if self.reproduction_requin():
                    monde[self.positionX][self.positionY] = Planete.Requin(
                        self.positionX, self.positionY)

                else:
                    monde[self.positionX][self.positionY] = "-"

                self.positionX = dep_choisi[0]
                self.positionY = dep_choisi[1]
                monde[self.positionX][self.positionY] = self

            elif len(liste_case_vide_ou_requin) != 0:
                dep_choisi = liste_case_vide_ou_requin[randint(0, len(liste_case_vide_ou_requin)-1)]
                if self.reproduction_requin():
                    monde[self.positionX][self.positionY] = Planete.Requin(
                        self.positionX, self.positionY)
                else:
                    monde[self.positionX][self.positionY] = "-"

                self.positionX = dep_choisi[0]
                self.positionY = dep_choisi[1]
                monde[self.positionX][self.positionY] = self
            self.reproduction -= 1
            self.energie -= 1

            return monde, self,liste
'''Planete.monde = [["-" for y in range(nb_colonne)] for x in range(nb_ligne)]
def generation(monde,nb_poisson,nb_requin):
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
'''

Planete.monde= [[choice([Planete.Poisson(x,y),Planete.Poisson(x,y),Planete.Poisson(x,y),"-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-",Planete.Requin(x,y)]) for y in range(nb_colonne)] for x in range(nb_ligne)]

for i in Planete.monde:
        for j in i:
            if isinstance(j,Planete.Poisson):
                Planete.Poisson.nb_poisson -=2
            if not isinstance(j,Planete.Poisson):
                Planete.Poisson.nb_poisson -=3
            if not isinstance(j,Planete.Requin):
                Planete.Requin.nb_requin -=1


compteur = 1

#Planete.monde=generation(Planete.monde,nb_poisson,nb_requin)
def afficher_monde(monde):
    for i in monde:
        for j in i:
            if isinstance(j, str):

                print(j, " | ", end="")
            elif isinstance(j, Planete.Poisson):
                print("P", " | ", end="")
            elif isinstance(j, Planete.Requin):

                print("R", " | ", end="")
        print("\n")
    print("il y a :", Planete.Poisson.nb_poisson, "poisson")
    print("il y a :", Planete.Requin.nb_requin, "requin")


print("\n")
afficher_monde(Planete.monde)
print("\n")


while compteur < 30:
    print("Tour "+str(compteur), "\n")
    print("il y a :", Planete.Poisson.nb_poisson, "poisson")
    print("il y a :", Planete.Requin.nb_requin, "requin")
    liste_pop = []
    for i in Planete.monde:
        for j in i:
            if j != "-":
                liste_pop.append(j)
    for i in liste_pop:
        if isinstance(i, Planete.Poisson):
            Planete.monde, i = i.deplacement_poison(Planete.monde)
        elif isinstance(i, Planete.Requin):
            Planete.monde, i,liste_pop = i.deplacement_requin(Planete.monde, liste_pop)

    

    compteur += 1
    sleep(1)

print("_____\n")    
afficher_monde(Planete.monde)
