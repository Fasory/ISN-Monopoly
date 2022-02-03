# -*-coding:Latin-1 -*

"""
Jeu : Monopoly
Réalisé par Clément BOUQUET, Julien BAZIN et Axel CHANCEREL courant 2019.
"""

import pygame
from pygame.locals import *
from datas.constantes import *
from datas.fonctions import *
from datas.classes import *
pygame.init()
from threading import Thread


menu = MENU()
jeu = JEU()
board = BOARD(jeu)
carte = CARTE(jeu)
pygame.key.set_repeat(400, 20)
while  menu.end == False and jeu.end == False:
    # Menu d'acceuil
    while menu.end == False and menu.acceuil == True:
        evenement(menu,board)
        menu.aff_acceuil()
        while menu.end == False and menu.jouer == True:
            evenement(menu,board)
            menu.aff_jouer()
            while menu.end == False and menu.config_ip == True:
                evenement(menu,board)
                menu.aff_ip()
                if menu.salon == True:
                    reseau = RESEAU(menu,convertisseur)
                    if menu.salon == True and menu.type_joueur != "hébergeur":
                        # Lancement d'une fonction en parallèle pour recevoir les données du serveur
                        parallele = Thread(target=reseau.clients,args=(menu,convertisseur,jeu,board))
                        parallele.start()
                    while menu.end == False and menu.salon == True:
                        evenement(menu,board)
                        if menu.type_joueur == "hébergeur":
                            reseau.serveur(menu,convertisseur)
                        menu.aff_salon(reseau)

    # Une fois en jeu
    if menu.jeu == True:
        jeu.debut_jeu(reseau,menu)
    while menu.end == False and jeu.end == False and menu.jeu == True:
        # Gestion des données entrantes pour le serveur
        if menu.type_joueur == "hébergeur" and len(reseau.liste_pseudo) > 1:
            jeu.serveur_analyse(reseau,convertisseur,envoyer,menu,board)
        elif reseau.raison_loose == True:
            reseau.raison_loose = False
            jeu.action_loose(reseau,menu,envoyer,board)
        # Gestions des événements
        evenement(jeu,board)
        # Transmission des évènements aux classes différentes de JEU
        distrib_variable(jeu,board,carte)
        # Gestion des déplacements PRIORITAIRE durant un tour
        if jeu.mon_tour == True:
            if jeu.deplacement == True:
                jeu.aff_deplacement(reseau,menu,envoyer,carte,board,calcul_capital)
        # Affichage du plateau de jeu
        jeu.aff_plateau(menu,reseau,envoyer,carte,board,calcul_capital)
        jeu.aff_complement()
        # Gestion du reste du tour SECONDAIRE
        if jeu.mon_tour == True:
            if jeu.predeplacement == True:
                jeu.aff_predeplacement(reseau,menu,envoyer,board)
            elif jeu.lance_de == True:
                jeu.aff_des(envoyer,menu,reseau)
            # Afficher les cartes bonus à l'écran
            if carte.carte_chance == True:
                carte.aff_carte_chance(jeu,reseau,menu,envoyer,board,calcul_capital)
            elif carte.carte_caissedecommu == True:
                carte.aff_carte_caissedecommu(jeu,reseau,menu,envoyer,board,calcul_capital)
        # Affichage du board droit
        board.aff_board()
        if board.argent == True:
            board.aff_argent(reseau,jeu)
        elif board.chat == True:
            board.aff_chat(menu,envoyer,reseau)
        elif board.propriete == True:
            board.aff_propriete(jeu,reseau)
            if not((True in jeu.doit_payer and jeu.mon_tour == True)) and jeu.doit_hypothequer == False and board.secteur != -1 and jeu.liste_loose.count(False) != 1 and (carte.carte_chance, carte.carte_caissedecommu, jeu.predeplacement, jeu.lance_de) == (False, False, False, False):
                carte.aff_carte_propriete(board)
            board.aff_complement_propriete(jeu,reseau,menu,envoyer,board)
        else:
            board.aff_historique()
        # Vérifie si il n'y a pas un gagnant ou si la personne doit hypothéquer / vendre
        if jeu.liste_loose.count(False) == 1 and 2 ==3:
            jeu.aff_win(reseau)
        elif jeu.doit_hypothequer == True:
            jeu.aff_hypothequer(reseau,menu,envoyer,calcul_capital)
        elif True in jeu.doit_payer and jeu.mon_tour == True:
            jeu.aff_attente_payement()
        # Actualisation de l'écran et la remise à 0 du clic
        jeu.actualisation(reseau,menu)

pygame.quit()

