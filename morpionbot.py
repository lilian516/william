#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      llafin
#
# Created:     17/11/2022
# Copyright:   (c) llafin 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random


class morpion:

    def __init__(self):
        self.tableau = []


    # la fonction creer_tableau permet de creer le tableau qu'on va utiliser pour le morpion
    def creer_tableau(self):
        for i in range(3):
            ligne = []
            for j in range(3):
                ligne.append('-')
            self.tableau.append(ligne)

    def mettre_signe(self, ligne, colonne, player):
        if ligne>3 or colonne>3:
             ligne, colonne = list(
                map(int, input("Entrer la ligne et la colonne ").split()))
        else:

            self.tableau[ligne][colonne] = player



    # la fonction victoire_joueur permet de regarder si un joueur à aligné 3 symboles
    def victoire_joueur(self, player):
        win = None
        n = len(self.tableau)

        # on regarde les lignes
        for i in range(n):
            win = True
            for j in range(n):
                if self.tableau[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # on regarde les colonnes
        for i in range(n):
            win = True
            for j in range(n):
                if self.tableau[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # on regarde les diagonales
        win = True
        for i in range(n):
            if self.tableau[i][i] != player:
                win = False
                break
        if win:
            return win
        win = True

        for i in range(n):
            if self.tableau[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for ligne in self.tableau:
            for item in ligne:
                if item == '-':
                    return False
        return True


    # la fonction tableau_remplit permet de vérifier si le morpion est remplit
    def tableau_remplit(self):
        for ligne in self.tableau:
            for item in ligne:
                if item == '-':
                    return False
        return True


    # la fonction tour_joueur_suivant permet de passer au tour suivant
    def tour_joueur_suivant(self, player):
        return 'X' if player == 'O' else 'O'


    # la fonction afficher_tableau permet d'afficher le morpion
    def afficher_tableau(self):
        for ligne in self.tableau:
            for item in ligne:
                print(item, end=" ")
            print()


    # la fonction tour_bot qui définit où le joueur va jouer
    def tour_bot(self, ligne, colonne, player,tour):



        if tour == 1:
            if ligne == 2 and colonne == 2:
                self.tableau[0][2]= player

            else:
                self.tableau[1][1]= player




        if tour == 2:


            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[0][1]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[1][2]=player



            if ligne == 1 and colonne == 2:

                if self.tableau[0][0] == 'X':
                    self.tableau[0][2] = player

                if self.tableau[0][2]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[0][0]=player



            if ligne == 1 and colonne == 3:

                if self.tableau[0][0] == 'X':
                    self.tableau[0][1] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[2][2]=='X':
                    self.tableau[1][2]=player




            if ligne == 2 and colonne == 1:

                if self.tableau[0][0] == 'X':
                    self.tableau[2][0] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[2][2]=='X':
                    self.tableau[0][0]=player




            if ligne == 2 and colonne == 3:


                if self.tableau[0][0] == 'X':
                    self.tableau[2][2] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[1][0]=player

                if self.tableau[2][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[0][2]=player





            if ligne == 3 and colonne == 1:


                if self.tableau[0][0] == 'X':
                    self.tableau[1][0] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[2][1]=player



            if ligne == 3 and colonne == 2:


                if self.tableau[0][0] == 'X':
                    self.tableau[2][2] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[0][1]=player

                if self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[2][2]=player

                if self.tableau[2][2]=='X':
                    self.tableau[2][0]=player



            if ligne == 3 and colonne == 3:


                if self.tableau[0][0] == 'X':
                    self.tableau[1][2] = player

                if self.tableau[0][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X':
                    self.tableau[1][2]=player

                if self.tableau[1][0]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[2][0]=='X':
                    self.tableau[2][1]=player

                if self.tableau[2][1]=='X':
                    self.tableau[2][0]=player




        if tour == 3:

            if ligne == 1 and colonne == 1:



                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player




            if ligne == 1 and colonne == 2:


                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player


                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][2]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][0]=player


                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player



                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player



                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player




                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player



                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0]=player




                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player




            if ligne == 1 and colonne == 3:



                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][1]=player


                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][2]=player


                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2]=player





            if ligne == 2 and colonne == 1:




                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][2]=player



                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player



                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player



                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player



            if ligne == 2 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player


                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player



            if ligne == 3 and colonne == 1:


                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[1][0]=player


                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player




            if ligne == 3 and colonne == 2:


                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][1]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][2]=='X':
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player


                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player


            if ligne == 3 and colonne == 3:



                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X':
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X':
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X':
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X':
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][1]=='X':
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player


                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[1][2]=player


                if self.tableau[0][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][2]=player


                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player


                if self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player






        if tour == 4:
            if ligne == 1 and colonne == 1:

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player




            if ligne == 1 and colonne == 2:

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player








            if ligne == 1 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player


                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[1][0]=='X' and self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][1]=player










            if ligne == 2 and colonne == 1:

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X' and self.tableau[1][2]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][2]=='X' and self.tableau[1][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][2]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player





            if ligne == 2 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][0]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][0]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][0]=='X' and self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' and self.tableau[1][0]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][2]=player

                if self.tableau[0][1]=='X' and self.tableau[1][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player

                if self.tableau[0][1]=='X' and self.tableau[2][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][0]=='X' and self.tableau[2][0]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[1][0]=='X' and self.tableau[2][1]=='X' and self.tableau[2][2]=='X' :
                    self.tableau[0][2]=player
















            if ligne == 3 and colonne == 1:
                pass
            if ligne == 3 and colonne == 2:
                pass
            if ligne == 3 and colonne == 3:

                if self.tableau[0][0]=='X' and self.tableau[0][1]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[0][0]=='X' and self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[1][1]=player

                if self.tableau[0][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[2][1]=player

                if self.tableau[0][1]=='X' and self.tableau[0][2]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][0]=player

                if self.tableau[0][1]=='X' and self.tableau[1][2]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[0][1]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[0][2]=='X' and self.tableau[1][0]=='X' and self.tableau[2][1]=='X' :
                    self.tableau[1][2]=player

                if self.tableau[1][0]=='X' and self.tableau[1][2]=='X' and self.tableau[2][0]=='X' :
                    self.tableau[0][1]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player


                if self.tableau[1][2]=='X' and self.tableau[2][1]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

                if self.tableau[1][2]=='X' and self.tableau[2][0]=='X' and self.tableau[1][1]=='X' :
                    self.tableau[0][0]=player

















    def start(self):
        self.creer_tableau()
        tour=1

        # on tire au sort quel joueur va commencer à jouer
        player = 'X'
        while True:
            print(f"Tour du joueur {player} ")

            self.afficher_tableau()

            # demander au joueur la postion de son signe
            ligne, colonne = list(
                map(int, input("Entrer la ligne et la colonne ").split()))
            print()



            # mettre le signe aux bonnes coordonnées
            self.mettre_signe(ligne - 1, colonne - 1, player)

            # on regarde si un joueur a gagné
            if self.victoire_joueur(player):
                print(f"Joueur {player} à gagné le match!")
                break

            # on regarde si il y a match nul
            if self.tableau_remplit():
                print("Match nul!")
                break

            # passer au tour suivant
            player = self.tour_joueur_suivant(player)

            self.tour_bot(ligne,colonne,player,tour)
            tour=tour+1
            if self.victoire_joueur(player):
                print(f"Joueur {player} à gagné le match!")
                break

            # on regarde si il y a match nul
            if self.tableau_remplit():
                print("Match nul!")
                break

            player = self.tour_joueur_suivant(player)


        # on affiche le tableau à la fin du match
        print()
        self.afficher_tableau()


# on commence le match
morpion = morpion()
morpion.start()
