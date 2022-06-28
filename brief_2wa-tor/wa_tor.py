from random import choice, randint
from time import sleep

nb_colonne=int(input("Nombre de colonne : "))
nb_ligne=int(input("Nombre de ligne : "))
temps_repro_poisson=int(input("Temps de repro des poissons : "))
temps_repro_requin=int(input("Temps de repro des requins :"))
energie_req=int(input("Energie requins :"))

class Planete:
    
    nombre_de_case=nb_colonne*nb_ligne
    temps=0
    class Poisson:

        nb_poisson=0
    
        def __init__(self,positionX,positionY):
            self.positionX= positionX
            self.positionY= positionY
            self.reproduction= temps_repro_poisson
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
        
        def choix_possible_poisson(poisson,monde):
            """
            Fonction qui renvoie les deplacement posible
            param poisson:(obj) le poisson qui doit se deplacer
            return: (list) Choix possible
            """
            liste_choix=[]

            if monde[(poisson.positionX + 1)%nb_ligne][(poisson.positionY)%nb_colonne] == "-":
                liste_choix.append([(poisson.positionX + 1)%nb_ligne,(poisson.positionY)%nb_colonne])

            if monde[(poisson.positionX - 1)%nb_ligne][(poisson.positionY)%nb_colonne] == "-":
                liste_choix.append([(poisson.positionX - 1)%nb_ligne,(poisson.positionY)%nb_colonne])

            if monde[(poisson.positionX)%nb_ligne][(poisson.positionY + 1)%nb_colonne] == "-":
                liste_choix.append([(poisson.positionX)%nb_ligne,(poisson.positionY + 1)%nb_colonne])

            if monde[(poisson.positionX)%nb_ligne][(poisson.positionY - 1)%nb_colonne] == "-":
                liste_choix.append([(poisson.positionX)%nb_ligne,(poisson.positionY - 1)%nb_colonne])

            return liste_choix

        def deplacement_poison(self,monde):
            """
            Fonction qui deplace le poisson
            param poisson:
            """
    
            liste_dep=self.choix_possible_poisson(monde)
    
            if len(liste_dep) !=0:
                dep_choisi=liste_dep[randint(0,len(liste_dep)-1)]
                if self.reproduction_poisson():
                    monde[self.positionX][self.positionY] = Planete.Poisson(self.positionX,self.positionY)
                else:
                    monde[self.positionX][self.positionY] = "-"

                self.positionX=dep_choisi[0]
                self.positionY=dep_choisi[1]
                monde[self.positionX][self.positionY] = self
            self.reproduction -= 1
        
            return monde,self

    class Requin:

        nb_requin=0
        
        def __init__(self,positionX,positionY):
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


        def manger(self,poisson,monde,liste):

            '''
            Fonction qui permet de simuler l'action du requin qui mange un poisson
            param: requin,poisson
            return: requin
            '''


            if self.positionX == poisson.positionX and self.positionXY == poisson.self.positionY :
                liste.remove(poisson)
                for ligne in monde:
                    liste.remove(poisson)
                self.energie += 2


        def choix_possible_requin(requin,monde):
            """
            Fonction qui renvoie les deplacement posible
            :param poisson:(obj) le requin qui doit se deplacer
            return: (list) choix possible
            """
            liste_choix=[]

            if monde[(requin.positionX + 1)%nb_ligne][(requin.positionY)%nb_colonne] == "-":
                liste_choix.append([(requin.positionX + 1)%nb_ligne,(requin.positionY)%nb_colonne])

            if monde[(requin.positionX - 1)%nb_ligne][(requin.positionY)%nb_colonne] == "-":
                liste_choix.append([(requin.positionX - 1)%nb_ligne,(requin.positionY)%nb_colonne])

            if monde[(requin.positionX)%nb_ligne][(requin.positionY + 1)%nb_colonne] == "-":
                liste_choix.append([(requin.positionX)%nb_ligne,(requin.positionY + 1)%nb_colonne])

            if monde[(requin.positionX)%nb_ligne][(requin.positionY - 1)%nb_colonne] == "-":
                liste_choix.append([(requin.positionX)%nb_ligne,(requin.positionY - 1)%nb_colonne])

            return liste_choix

        def deplacement_requin(self,monde):
            """
            Fonction qui deplace le requin
            :param monde:
            """
    
            liste_dep=self.choix_possible_requin(monde)
    
            if len(liste_dep) !=0:
                dep_choisi=liste_dep[randint(0,len(liste_dep)-1)]
                if self.reproduction_requin():
                    monde[self.positionX][self.positionY] = Planete.Requin(self.positionX,self.positionY)
                else:
                    monde[self.positionX][self.positionY] = "-"

                self.positionX=dep_choisi[0]
                self.positionY=dep_choisi[1]
                monde[self.positionX][self.positionY] = self
            self.reproduction -= 1
            self.energie -= 1
        
            return monde,self

        

Planete.monde= [[choice([Planete.Poisson(x,y),"-",Planete.Requin(x,y),"-","-","-","-","-","-","-","-","-","-"]) for y in range(nb_colonne)] for x in range(nb_ligne)]
for i in Planete.monde:
        for j in i:
            if not isinstance(j,Planete.Poisson):
                Planete.Poisson.nb_poisson -=1
            if not isinstance(j,Planete.Requin):
                Planete.Requin.nb_requin -=1


compteur=1
def afficher_monde(monde):
    for i in monde:
        for j in i:
            if isinstance(j,str):

                print(j+" "," | ",end="")
            elif isinstance(j,Planete.Poisson):
                print("P"," | ",end="")
            else:
                print("R"," | ",end="")
        print("\n")
    print("il y a :", Planete.Poisson.nb_poisson,"poisson")
    print("il y a :", Planete.Requin.nb_requin,"requin")


print("\n")
afficher_monde(Planete.monde)  
print("\n")


while compteur<10:
    print("Tour "+str(compteur),"\n")
    
    liste=[]
    for i in Planete.monde:
        for j in i:
            if j != "-":
                liste.append(j)
    for i in liste:
        if isinstance(i,Planete.Poisson):
            Planete.monde,i=i.deplacement_poison(Planete.monde)
        elif isinstance(i,Planete.Requin):
            Planete.monde,i=i.deplacement_requin(Planete.monde)

    afficher_monde(Planete.monde) 
    print("_____\n")
    
    compteur +=1
    sleep(1)


""""fill("#AF7AC5")
square(0,10,10)"""