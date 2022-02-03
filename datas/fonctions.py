# -*-coding:Latin-1 -*
""" Fichier regroupant toutes les fonctions utiles. """

import pygame
from datas.constantes import *
from pygame.locals import *
pygame.init()



def evenement(classe,board):
    for event in pygame.event.get():
        if event.type == QUIT:
            classe.end = True
        if event.type == MOUSEMOTION:
            classe.position = event.pos
        if event.type == MOUSEBUTTONDOWN:
            classe.clic = event.button
        if event.type == KEYDOWN:
            try:
                if classe.config_ip == True:
                    if event.key == K_ESCAPE:
                        classe.config_ip = False
                        classe.jouer = True
                    else:
                        classe.touche = event.unicode
                elif classe.jouer == True:
                    if event.key == K_ESCAPE:
                        classe.jouer = False
                        classe.acceuil = True
            except:
                if event.key == K_RIGHT:
                    board.touche = "\right"
                elif event.key == K_LEFT:
                    board.touche =  "\left"
                elif event.key == K_DELETE:
                    board.touche =  "\suppr"
                elif event.key == K_RETURN:
                    board.touche =  "\return"
                elif event.key == K_ESCAPE:
                    board.touche =  "\echap"
                else:
                    board.touche = event.unicode



def convertisseur(donnee):
    # On retranscrit tout dans une liste_finale
    phrase = False
    liste_finale = [""]
    mot = ""
    compteur = 0
    donnee = str(donnee)
    exception = False
    for cara in donnee:
            compteur += 1
            if phrase == False:
                if compteur != len(donnee):
                    if cara not in " []',":
                        mot += cara
                    else:
                        if mot in ["$message$","$historique$"]:
                            phrase = True
                        liste_finale[-1] += mot
                        if liste_finale[-1] != "":
                            liste_finale.append("")
                        mot = ""
                else:
                    if cara not in " []',":
                        mot += cara
                    liste_finale[-1] += mot

            else:
                if cara == "$" and exception == False:
                    exception = True
                elif cara == " " and exception == True:
                    exception = False
                    liste_finale[-1] += mot + cara
                    mot = ""
                if exception == False:
                    liste_finale[-1] += cara
                else:
                    mot += cara
                if compteur == len(donnee) and exception == True:
                    liste_finale[-1] += mot
                if mot in ["$historique$","$message$","$liste_pret$",
                           "$liste_ip$","$liste_pseudo$","$mon_tour$",
                           "$nb_tour$","$case$","$liste_argent$","$liste_loose$",
                           "$nb_commu$","$nb_chance$","$pret$","$fin_tour$",
                           "$liste_hypotheque$","$obligation$","$doit_payer$"]:
                    if mot not in ["$historique$","$message$"]:
                        phrase = False
                    liste_finale.append("")
                    liste_finale[-1] += mot
                    liste_finale.append("")
                    mot = ""      
    if liste_finale[-1] == "":
        del liste_finale[-1]
    # On modifie si possible le type d'objet en int ou bool
    for i in range(0,len(liste_finale)):
        if liste_finale[i] == "True":
            liste_finale[i] = True
        elif liste_finale[i] == "False":
            liste_finale[i] = False
        else:
            try:
                liste_finale[i] = int(liste_finale[i])
            except:
                pass
    return liste_finale



def envoyer(reseau, menu, nom, variable):
    donnee = (nom + str(variable))
    if menu.type_joueur == "hébergeur":
        for ip in reseau.liste_connexion_serv:
            if ip != "hébergeur":
                ip.send(donnee.encode())
    else:
        reseau.tunnel_serveur.send(donnee.encode())



def distrib_variable(jeu,board,carte):
    board.position = jeu.position
    board.clic = jeu.clic
    carte.position = jeu.position
    carte.clic = jeu.clic



def calcul_capital(num_joueur, liste_argent, pv, liste_hypotheque):
    capital = liste_argent[num_joueur]
    liste_case = case_simple + [case_gare] + [case_compagnie]
    for case in range(0,40):
        if pv[case][1] == num_joueur and case not in liste_hypotheque:
            compteur = -1
            continuer = 1
            while continuer:
                compteur += 1
                if compteur < 22:
                    if case == liste_case[compteur]:
                        continuer = 0
                else:
                    if case in liste_case[compteur]:
                        continuer = 0
            if pv[case][2] > 0:
                capital += int(liste_prixpropriete[compteur][-2]) * pv[case][2]
            capital += int(liste_prixpropriete[compteur][-1])
    return capital
    
