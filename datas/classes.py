# -*-coding: utf-8 -*

import pygame
from pygame.locals import *
pygame.init()
from datas.constantes import *
import socket
import select
from random import *
from math import *
from time import sleep



class MENU:
    """ Classe permettant d'afficher les menus.
        Méthodes : aff_acceuil, aff_joueur, aff_ip, aff_salon """
    
    def __init__(self):
        """ Initilisation des variables utiles au menu. """
        self.position = (0,0)
        self.clic = 0
        self.end = False
        self.acceuil = True
        self.jouer = False
        self.config_ip = False
        self.type_joueur = ""
        self.touche = ""
        self.ip = "192.168.1.15"
        self.pseudo = "Fasory"
        self.ecrire = ""
        self.salon = False
        self.pret = False
        self.jeu = False



    def aff_acceuil(self):
        """ Affiche le menu d'acceuil qui permet de soit quitter, soit jouer en cliuqant sur des bouttons. """
        font = pygame.font.Font("datas/font/unispace_rg.ttf",70)
        color = (237, 27, 26)
        if self.position[0] > 561 and self.position[0] < 784 and self.position[1] > 505 and self.position[1] < 570:
            color = (248, 211, 3)
            if self.clic == 1:
                self.acceuil = False
                self.jouer = True
        else:
            color = (237, 27, 26)
        # Bouton jouer
        fen.blit(fond_menu,(0,0))
        text = font.render("Jouer", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],500))
        if self.position[0] > 522 and self.position[0] < 830 and self.position[1] > 620 and self.position[1] < 692:
            color = (248, 211, 3)
            if self.clic == 1:
                self.end = True
        else:
            color = (237, 27, 26)
        # Bouton quitter
        text = font.render("Quitter", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],620))
        pygame.display.flip()
        self.clic = 0
        self.touche = ""



    def aff_jouer(self):
        """ Affiche le menu qui permet de sélectionner si l'on est l'hébergeur ou le client. """
        font = pygame.font.Font("datas/font/unispace_rg.ttf",70)
        color = (237, 27, 26)
        if self.position[0] > 500 and self.position[0] < 840 and self.position[1] > 497 and self.position[1] < 563:
            color = (248, 211, 3)
            if self.clic == 1:
                self.type_joueur = "hébergeur"
                self.jouer = False
                self.config_ip = True
                
        else:  
            color = (237, 27, 26)
        # Bouton heberger
        fen.blit(fond_menu,(0,0))
        text = font.render("Heberger", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],500))
        if self.position[0] > 480 and self.position[0] < 860 and self.position[1] > 611 and self.position[1] < 686:
            color = (248, 211, 3)
            if self.clic == 1:
                self.type_joueur = "client"
                self.jouer = False
                self.config_ip = True
        else:
            color = (237, 27, 26)
        # Bouton rejoindre
        text = font.render("Rejoindre", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],620))
        pygame.display.flip()
        self.clic = 0
        self.touche = ""



    def aff_ip(self):
        """ Affiche le menu où l'on doit entrer un pseudo et une adresse IP. """
        if self.clic == 1:
            if self.position[0] > 425 and self.position[0] < 925 and self.position[1] > 215 and self.position[1] < 288:
                self.ecrire = "pseudo"
            elif self.position[0] > 425 and self.position[0] < 925 and self.position[1] > 515 and self.position[1] < 588:
                self.ecrire = "ip"
            else:
                self.ecrire = ""
        fen.blit(fond_menu,(0,0))
        fond = pygame.Surface((1350,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        # Paramètrage du pseudo
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        text = font.render("Entrez votre pseudo", 0, (237,27,26))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],130))
        pygame.draw.rect(fen, (0,0,0), (425,213,500,75))
        if self.ecrire == "pseudo":
            if len(self.pseudo)<15 and self.touche in "_-azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBNéèàêâïîùû0123456789":
                self.pseudo += self.touche
            elif len(self.pseudo)>0 and self.touche == "\b":
                self.pseudo = list(self.pseudo)
                del self.pseudo[-1]
                self.pseudo = "".join(self.pseudo)
            color = (247,240,0)
        else:
            color = (255,255,255)
        pygame.draw.rect(fen, color, (425,213,500,75), 2)
        self.pseudo = "".join(self.pseudo)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 30)
        text = font.render(self.pseudo, 0, (237,27,26))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],235))
        # Paramètrage de l'ip
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        if self.type_joueur == "hébergeur":
            commentaire = "Entrez votre adresse IP"
        else:
            commentaire = "Entrez l'adresse IP à rejoindre"
        text = font.render(commentaire, 0, (237,27,26))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],430))
        pygame.draw.rect(fen, (0,0,0), (425,513,500,75))
        if self.ecrire == "ip":
            if len(self.ip)<15 and self.touche in ".0123456789":
                self.ip += self.touche
            elif len(self.ip)>0 and self.touche == "\b":
                self.ip = list(self.ip)
                del self.ip[-1]
                self.ip = "".join(self.ip)
            color = (247,240,0)
        else:
            color = (255,255,255)
        pygame.draw.rect(fen, color, (425,513,500,75), 2)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 30)
        text = font.render(self.ip, 0, (237,27,26))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],535))
        # Bouton pour valider
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        pygame.draw.rect(fen, (0,0,0), (562.5,613,225,75))
        if self.position[0] > 562 and self.position[0] < 788 and self.position[1] > 615 and self.position[1] < 688:
            if self.clic == 1  and self.ip != "" and self.pseudo != "":
                self.config_ip = False
                self.salon = True
            color = (237,27,26)
        else:
            color = (255,255,255)
        pygame.draw.rect(fen, color, (562.5,613,225,75), 2)
        text = font.render("Valider", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],630))
        pygame.display.flip()
        self.clic = 0
        self.touche = ""



    def aff_salon(self,reseau):
        """ Affiche la totalité du salon des connexions. """
        color = (237,27,26)
        fen.blit(fond_menu,(0,0))
        fond = pygame.Surface((1350,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        for x in range(0,len(reseau.liste_pseudo)):
            pygame.draw.rect(fen, (0,0,0), (375,75+125*x,500,100))
            pygame.draw.rect(fen, (255,255,255), (375,75+125*x,500,100),3)
            pygame.draw.lines(fen, (255,255,255), False, [(377,125+125*x), (872,125+125*x)], 3)
            pygame.draw.rect(fen, (0,0,0), (875,75+125*x,100,100))
            pygame.draw.rect(fen, (255,255,255), (875,75+125*x,100,100),3)
            text2 = font1.render(reseau.hote, 0, color)
            fen.blit(text2, (384,135))
            if reseau.liste_pret[x] == True:
                color1 = (0, 176, 45)
            else:
                color1 = (237,27,26)
            pygame.draw.circle(fen, color1, (925,125+125*x), 15, 0)
            text = font1.render(reseau.liste_pseudo[x], 0, color)
            fen.blit(text, (384,85+125*x))
            if x > 0 and x < 5:
                text = font1.render("Client", 0, color)
                fen.blit(text, (765,87+125*x))
                try:
                    text1 = font1.render(reseau.liste_ip[x], 0, color)
                    fen.blit(text1, (384,135+125*x))
                except:
                    pass
        text = font1.render("Hébergeur", 0, color)
        fen.blit(text, (725,87))
        # Bouton prêt
        color = (237, 27, 36)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        pygame.draw.rect(fen, (0,0,0), (562.5,733,225,75))
        if self.position[0] > 560 and self.position[0] < 790 and self.position[1] > 730 and self.position[1] < 815 and self.clic == 1:
            self.pret = not self.pret
            if self.type_joueur != "hébergeur":
                reseau.tunnel_serveur.send((" $pret$ " + str(self.pret)).encode())
            else:
                reseau.liste_pret[0] = self.pret
                for ip in reseau.liste_connexion_serv:
                        ip.send((" $liste_pret$ "+str(reseau.liste_pret)).encode())
        elif self.pret == True:
            color = (0, 176, 45)
        else:
            color = (237,27,26)
        pygame.draw.rect(fen, color, (562.5,733,225,75), 2)
        text = font.render("Prêt", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0],750))
        pygame.display.flip()
        self.clic = 0
        if len(reseau.liste_pseudo) == reseau.liste_pret.count(True) and len(reseau.liste_pseudo) >= 1:
            self.salon = False
            self.jeu = True



class RESEAU:
    """ Classe permettant de gérer la relation serveur / client.
        Méthodes : serveur, clients """
    
    def __init__(self,menu,convertisseur):
        """ Initilisation des variables utiles au reseau. """
        self.raison_loose = False
        self.hote = menu.ip
        self.port = 34780
        self.liste_ip = []
        self.liste_connexion_serv = []
        self.liste_pret = [False]*5
        self.liste_pseudo = []
        if menu.type_joueur == "hébergeur":
            try:
                self.connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connexion_principale.bind((self.hote, self.port))
                self.connexion_principale.listen(5)
                self.liste_ip.append("hébergeur")
                self.liste_pseudo = [menu.pseudo]
            except:
                menu.salon = False
                menu.config_ip = True
        else:
            try:
                fen.blit(fond_menu,(0,0))
                fond = pygame.Surface((1350,900))
                fond.set_alpha(220)
                fond.fill((0,0,0))
                fen.blit(fond,(0,0))
                font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
                text = font.render("Tentative de connexion...", 0, (237,27,26))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                fen.blit(text, text_centre)
                pygame.display.flip()
                self.tunnel_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.tunnel_serveur.connect((self.hote, self.port))
                self.tunnel_serveur.send(menu.pseudo.encode())
            except:
                menu.salon = False
                menu.config_ip = True

            

    def serveur(self,menu,convertisseur):
        """ Méthode gérant les clients entrant. """
        # Regarde si un client essaye de se connecter
        try:
            demande_connexion = select.select([self.connexion_principale], [], [], 0)[0]
        except:
            pass
        if len(self.liste_ip) < 5:
            for info_ip in demande_connexion:
                connexion_serv, ip = info_ip.accept()
                self.liste_ip.append(ip[0])
                self.liste_connexion_serv.append(connexion_serv)
                pseudo = self.liste_connexion_serv[-1].recv(1024)
                self.liste_pseudo.append(pseudo.decode())
                for ip in self.liste_connexion_serv:
                    ip.send((" $liste_pseudo$ "+str(self.liste_pseudo)).encode())
                    ip.send((" $liste_pret$ "+str(self.liste_pret)).encode())
                    ip.send((" $liste_ip$ "+str(self.liste_ip)).encode())
        # Regarde si un client lui a envoyé une donnée
        client_a_lire = []
        try:
            client_a_lire, wlist, xlist = select.select(self.liste_connexion_serv,
                    [], [], 0)
        except:
            pass
        for client in client_a_lire:
            nb = 1
            while client != self.liste_connexion_serv[nb-1]:
                nb += 1
            donnee = client.recv(1024).decode().split()
            donnee = convertisseur(donnee)
            classeur = []
            for une_donnee in donnee:
                if une_donnee in ["$pret$"]:
                    classeur.append([une_donnee])
                else:
                    classeur[len(classeur)-1].append(une_donnee)
            for i in range(0,len(classeur)):
                if classeur[i][0] == "$pret$":
                    self.liste_pret[nb] = classeur[i][1]
                    for ip in self.liste_connexion_serv:
                        ip.send((" $liste_pret$ "+str(self.liste_pret)).encode())



    def clients(self,menu,convertisseur,jeu,board):
        """ Méthode récupérant les données envoyer par le serveur et ainsi
            actualise les variables concercées. """
        while menu.end == False:
            donnee = self.tunnel_serveur.recv(1024).decode()
            donnee = convertisseur(donnee)
            classeur = []
            for une_donnee in donnee:
                if une_donnee in ["$historique$","$message$","$liste_pret$",
                                  "$liste_ip$","$liste_pseudo$","$mon_tour$",
                                  "$nb_tour$","$case$","$liste_argent$","$obligation$",
                                  "$nb_commu$","$nb_chance$","$liste_loose$",
                                  "$liste_hypotheque$","$doit_payer$"]:
                    classeur.append([une_donnee])
                else:
                    classeur[-1].append(une_donnee)
            for i in range(0,len(classeur)):
                if classeur[i][0] == "$liste_pret$":
                    self.liste_pret = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$liste_pseudo$":
                    self.liste_pseudo = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$liste_ip$":
                    self.liste_ip = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$mon_tour$":
                    jeu.mon_tour = classeur[i][1]
                elif classeur[i][0] == "$nb_tour$":
                    jeu.nb_tour = classeur[i][1]
                elif classeur[i][0] == "$case$":
                    case = []
                    for info in classeur[i][2:len(classeur[i])]:
                        if str(info) in "pjm":
                            case.append([])
                        else:
                            case[-1].append(info)
                    if case[1] != []:
                        case[1] = case[1][0]
                    if case[2] != []:
                        case[2] = case[2][0]  
                    jeu.pv[classeur[i][1]] = case
                elif classeur[i][0] == "$liste_argent$":
                    jeu.liste_argent = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$nb_commu$":
                    if jeu.mon_tour == True:
                        jeu.nb_carte_commu = classeur[i][1]
                elif classeur[i][0] == "$nb_chance$":
                    if jeu.mon_tour == True:
                        jeu.nb_carte_chance = classeur[i][1]
                elif classeur[i][0] == "$message$":
                    message = ""
                    board.liste_msg.append(classeur[i][1])
                    if board.chat == False:
                        board.notif = True
                elif classeur[i][0] == "$historique$":
                    message = ""
                    board.liste_msg_h.append(classeur[i][1])
                elif classeur[i][0] == "$liste_loose$":
                    jeu.liste_loose = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$liste_hypotheque$":
                    jeu.liste_hypotheque = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$doit_payer$":
                    jeu.doit_payer = classeur[i][1:len(classeur[i])]
                elif classeur[i][0] == "$obligation$":
                    compteur = 0
                    while self.liste_pseudo[compteur] != menu.pseudo:
                        compteur += 1
                    if classeur[i][1] == "doit_loose":
                        if classeur[i][2] == compteur:
                            self.raison_loose = True
                    else:
                        if classeur[i][2] == compteur:
                            jeu.dette = [10, classeur[i][3]]
                            jeu.doit_hypothequer = True
                        



class JEU:
    """ Classe gérant le déroulement du jeu ainsi que l'affichage de ce dernier.
        Méthodes :  debut_jeu, aff_plateau, aff_des, actualisation,
        aff_predeplacement, aff_deplacement, serveur_analyse, gestion_case,
        gestion_chance, gestion_caissedecommu, aff_win """

    def __init__(self):
        """ Initialisation des variables utiles au jeu. """
        self.end = False
        self.position = (0,0)
        self.clic = 0
        self.mon_tour = False
        self.nb_tour = 0
        self.nb_tour_prison = 0
        self.lance_de = False
        self.nb_lance = 1
        self.de1, self.de2 = 0, 0
        self.deplacement = False
        self.predeplacement = False
        # Liste pv représentant le palteau virtuel avec les cases de 0 à 40
        # avec la 40 ème qui représente la case prison
        # Chaque cases comportent 3 sous-litses :
        # - les pions qui sont présents sur cette case
        # - le joueur à qui appartient cette case
        # - les maisons / hôtels présent sur cette case
        self.pv = []
        for i in range(0,41):
            self.pv.append([])
            for j in range(0,3):
                if j != 2:
                    self.pv[i].append([])
                else:
                    self.pv[i].append(0)
        self.nb_double = 0
        self.total_de = 0
        self.localisation = 0
        self.repere = 0
        self.tour_prison = -1
        self.nb_libere_prison = 0
        self.nb_carte_commu = -1
        self.nb_carte_chance = -1
        self.new_case_ach = False
        self.liste_hypotheque = []
        # La dette est composé en [0] d'une somme, puis en [1] du destinataire :
        # -1 pour aucun destinataire
        # -2 pour prévenir de l'amende : sortir de prison
        self.dette = [0, -1]
        self.doit_hypothequer = False



    def debut_jeu(self,reseau,menu):
        """ Initialise un tour de table en mélangeant l'ordre des joueurs. """
        self.liste_loose = [False]*len(reseau.liste_pseudo)
        self.liste_argent = [1500]*len(reseau.liste_pseudo)
        if menu.type_joueur == "hébergeur" and len(reseau.liste_pseudo) > 1:
            # Mélange des cartes de chances et des caisses de communautés
            self.liste_chance = []
            for i in range (0,16):
                self.liste_chance.append(i)
            shuffle(self.liste_chance)
            self.liste_caisse_de_commu =[]
            for i in range (0,16):
                self.liste_caisse_de_commu.append(i)
            shuffle(self.liste_caisse_de_commu)
            # Introduction du l'hébergeur dans la liste des connections
            reseau.liste_connexion_serv.reverse()
            reseau.liste_connexion_serv.append("hébergeur")
            reseau.liste_connexion_serv.reverse()
            # Initialisation d'un tour de plateau / Mélange
            for i in range(0,randint(5,20)):
                nb = randint(0,len(reseau.liste_pseudo)-2)
                ech_pseudo = reseau.liste_pseudo[nb]
                ech_ip = reseau.liste_connexion_serv[nb]
                reseau.liste_pseudo[nb] = reseau.liste_pseudo[nb+1]
                reseau.liste_pseudo[nb+1] = ech_pseudo
                reseau.liste_connexion_serv[nb] = reseau.liste_connexion_serv[nb+1]
                reseau.liste_connexion_serv[nb+1] = ech_ip
            for ip in reseau.liste_connexion_serv:
                if ip != "hébergeur":
                    ip.send((" $liste_pseudo$ "+str(reseau.liste_pseudo)).encode())
            if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                self.mon_tour = True
            else:
                reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
            self.liste_connexion_serv = []
            for i in reseau.liste_connexion_serv:
                if i != "hébergeur":
                    self.liste_connexion_serv.append(i)
        for i in range(0,len(reseau.liste_pseudo)):
            self.pv[0][0].append(i)
        self.doit_payer = [False] * len(reseau.liste_pseudo)
        for pseudo in reseau.liste_pseudo:
            nb_meme_pseudo = reseau.liste_pseudo.count(pseudo) - 1
            # Si y a au moins 2 fois le même pseudo, on quite le jeu d'urgence puor éviter tout bug
            if nb_meme_pseudo > 0:
                 menu.end = True
                 self.end = True



    def aff_plateau(self,menu,reseau,envoyer,carte,board,calcul_capital):
        """ Méthode permettant d'afficher le plateau de jeu ainsi que les boutons
            de gestion : Tour suivant / Lancer les dés, en plus de gérer
            le tour du joueur concerné. """
        fen.blit(fond_plateau, (0,0))
        if self.lance_de == False and self.predeplacement == False:
            # Bouton mettre fin à son tour
            font = pygame.font.Font("datas/font/unispace_rg.ttf", 20)
            pygame.draw.rect(fen, (0,0,0), (125,730,320,45))
            if not((True in self.doit_payer and self.mon_tour == True)) and self.doit_hypothequer == False and self.liste_loose.count(False) != 1 and (board.secteur == -1 or (carte.carte_chance, carte.carte_caissedecommu, self.predeplacement, self.lance_de) != (False, False, False, False)) and carte.carte_chance == False and carte.carte_caissedecommu == False and self.nb_lance == 0 and self.mon_tour == True and self.deplacement == False:
                if self.position[0] > 125 and self.position[0] < 445 and self.position[1] > 730 and self.position[1] < 775:
                    color = (237,27,26)
                    if self.clic == 1:
                        # Reset les variables utiles pendant pendant mon_tour
                        self.mon_tour = False
                        self.nb_lance = 1
                        self.nb_double = 0
                        self.new_case_ach = False
                        # On passe au tour suivant
                        if menu.type_joueur == "hébergeur":
                            self.nb_tour += 1
                            if self.nb_tour == len(reseau.liste_pseudo):
                                self.nb_tour = 0
                            while self.liste_loose[self.nb_tour] == True:
                                self.nb_tour += 1
                                if self.nb_tour == len(reseau.liste_pseudo):
                                    self.nb_tour = 0
                            if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                                self.mon_tour = True
                            else:
                                reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
                            envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
                        else:
                            self.nb_tour = -1
                            envoyer(reseau,menu," $fin_tour$ ",1)
                else:
                    color = (255,255,255)
            else:
                color = (126.,126,126)
            pygame.draw.rect(fen, color, (125,730,320,45), 2)
            text = font.render("Tour suivant", 0, color)
            fen.blit(text, (215,740))
            # Bouton pour aller lancer les dés
            pygame.draw.rect(fen, (0,0,0), (455,730,320,45))
            if not((True in self.doit_payer and self.mon_tour == True)) and self.doit_hypothequer == False and self.liste_loose.count(False) != 1 and (board.secteur == -1 or (carte.carte_chance, carte.carte_caissedecommu, self.predeplacement, self.lance_de) != (False, False, False, False)) and carte.carte_chance == False and carte.carte_caissedecommu == False and self.nb_lance > 0 and self.mon_tour == True and self.tour_prison<3 and self.deplacement == False:
                if self.position[0] > 455 and self.position[0] < 775 and self.position[1] > 730 and self.position[1] < 775 and self.deplacement == False:
                    color = (237,27,26)
                    if self.clic == 1:
                        self.lance_de = True
                else:
                    color = (255,255,255)
            else:
                color = (126.,126,126)
            pygame.draw.rect(fen, color, (455,730,320,45), 2)
            text = font.render("Prendre les dés", 0, color)
            fen.blit(text, (530,740))
            # Bouton pour payer ou utiliser une carte chance si on est en prsion
            if self.doit_hypothequer == False and self.liste_loose.count(False) != 1 and (board.secteur == -1 or (carte.carte_chance, carte.carte_caissedecommu, self.predeplacement, self.lance_de) != (False, False, False, False)) and self.tour_prison >= 0:
                # Bouton des 80 M
                if self.mon_tour == True and self.tour_prison == 3:
                    capital = capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
                    if capital >= 80:
                        if self.liste_argent[self.nb_tour] < 80:
                            self.dette = [80, -2]
                            self.doit_hypothequer = True
                    else:
                        self.action_loose(reseau,menu,envoyer,board)
                pygame.draw.rect(fen, (0,0,0), (455,680,320,45))
                if self.liste_argent[self.nb_tour] >= 80 and self.nb_lance > 0 and self.mon_tour == True:
                    if self.position[0] > 455 and self.position[0] < 775 and self.position[1] > 680 and self.position[1] < 725 and self.deplacement == False:
                        color = (237,27,26)
                        if self.clic == 1:
                            self.liste_argent[self.nb_tour] -= 80
                            envoyer(reseau,menu," $liste_argent$ ",self.liste_argent)
                            self.pv[self.localisation][0].remove(self.nb_tour)
                            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                            envoyer(reseau, menu, " $case$ ", case_envoie)
                            self.localisation = 10
                            self.pv[self.localisation][0].append(self.nb_tour)
                            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                            envoyer(reseau, menu, " $case$ ", case_envoie)
                            self.tour_prison = -1
                            self.nb_lance = 1
                            message_h = str(menu.pseudo) + " paye 80M pour sortir de prison."
                            envoyer(reseau, menu, " $historique$ ", message_h)
                            if menu.type_joueur == "hébergeur":
                                board.liste_msg_h.append(message_h)
                    else:
                        color = (255,255,255)
                else:
                    color = (126,126,126)
                pygame.draw.rect(fen, color, (455,680,320,45), 2)
                text = font.render("Payer 80 M", 0, color)
                fen.blit(text, (560,690))
                # Bouton pour la carte libéré de prison
                pygame.draw.rect(fen, (0,0,0), (125,680,320,45))
                if self.doit_hypothequer == False and self.liste_loose.count(False) != 1 and (board.secteur == -1 or (carte.carte_chance, carte.carte_caissedecommu, self.predeplacement, self.lance_de) != (False, False, False, False)) and self.nb_lance > 0 and self.mon_tour == True and self.nb_libere_prison > 0:
                    if self.position[0] > 125 and self.position[0] < 445 and self.position[1] > 680 and self.position[1] < 725 and self.deplacement == False:
                        color = (237,27,26)
                        if self.clic == 1:
                            self.nb_libere_prison -= 1
                            self.pv[self.localisation][0].remove(self.nb_tour)
                            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                            envoyer(reseau, menu, " $case$ ", case_envoie)
                            self.localisation = 10
                            self.pv[self.localisation][0].append(self.nb_tour)
                            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                            envoyer(reseau, menu, " $case$ ", case_envoie)
                            self.tour_prison = -1
                            self.nb_lance = 1
                            message_h = str(menu.pseudo) + " utilise la carte : vous êtes libéré de prison."
                            envoyer(reseau, menu, " $historique$ ", message_h)
                            if menu.type_joueur == "hébergeur":
                                board.liste_msg_h.append(message_h)
                    else:
                        color = (255,255,255)
                else:
                    color = (126.,126,126)
                pygame.draw.rect(fen, color, (125,680,320,45), 2)
                text = font.render("Libéré de prison", 0, color)
                fen.blit(text, (190,690))



    def aff_des(self,envoyer,menu,reseau):
        """ Méthode permettant de lancer les dés. """
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        if self.nb_lance > 0:
            self.de1 = randint(0,5)
            self.de2 = randint(0,5)
        fen.blit(de[self.de1], (280,350))
        fen.blit(de[self.de2], (550,350))
        # Bouton lancer
        color = (237, 27, 36)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        pygame.draw.rect(fen, (0,0,0), (337.5,533,225,75))
        if self.nb_lance > 0:
            if self.position[0] > 337.5 and self.position[0] < 567.5 and self.position[1] > 530 and self.position[1] < 615:
                color = (237,27,26)
                if self.clic == 1:
                    self.nb_lance -= 1
                    self.predeplacement = True
                    self.lance_de = False
            else:
                color = (255,255,255)
        else:
            color = (126.,126,126)
        pygame.draw.rect(fen, color, (337.5,533,225,75), 2)
        text = font.render("Lancer", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,550))
        # Bouton retour
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        pygame.draw.rect(fen, (0,0,0), (337.5,633,225,75))
        if self.position[0] > 337.5 and self.position[0] < 567.5 and self.position[1] > 630 and self.position[1] < 715:
            color = (237,27,26)
            if self.clic == 1:
                self.lance_de = False
        else:
            color = (255,255,255)
        pygame.draw.rect(fen, color, (337.5,633,225,75), 2)
        text = font.render("Retour", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,650))



    def actualisation(self,reseau,menu):
        """ Méthode permettant d'actualiser l'affichage de la fenêtre. """
        pygame.display.flip()
        self.clic = 0
        # Gestion de mon_tour
        if self.nb_tour != -1:
            self.mon_tour = menu.pseudo == reseau.liste_pseudo[self.nb_tour]
        else:
            self.mon_tour = False



    def aff_predeplacement(self,reseau,menu,envoyer,board):
        """ Méthode permettant au joueur de voir son lancé avant d'avancer
            son pion. """
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        fen.blit(de[self.de1], (280,350))
        fen.blit(de[self.de2], (550,350))
        # Bouton avancer
        color = (237, 27, 36)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        pygame.draw.rect(fen, (0,0,0), (337.5,533,225,75))
        if self.position[0] > 337.5 and self.position[0] < 567.5 and self.position[1] > 530 and self.position[1] < 615:
            color = (237,27,26)
            if self.clic == 1:
                self.deplacement = True
                self.predeplacement = False
                if self.tour_prison == -1:
                    if self.de1 == self.de2:
                        self.nb_lance += 1
                        self.nb_double += 1
                        # Protocole pour aller en prison dû au triple doubles
                        if self.nb_double == 3:
                            self.deplacement = False
                            self.tour_prison = 0
                            self.pv[self.localisation][0].remove(self.nb_tour)
                            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                            envoyer(reseau, menu, " $case$ ", case_envoie)
                            self.localisation = 40
                            self.pv[self.localisation][0].append(self.nb_tour)
                            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                            envoyer(reseau, menu, " $case$ ", case_envoie)
                            # Reset les variables utiles pendant pendant mon_tour
                            self.mon_tour = False
                            self.nb_lance = 1
                            self.nb_double = 0
                            self.new_case_ach = False
                            # Envoie un message dans l'historique
                            message_h = reseau.liste_pseudo[self.nb_tour] + " va en prison, il a fait 3 doubles à la suite."
                            envoyer(reseau,menu," $historique$ ",message_h)
                            if menu.type_joueur == "hébergeur":
                                board.liste_msg_h.append(message_h)
                            # On passe au tour suivant
                            if menu.type_joueur == "hébergeur":
                                self.nb_tour += 1
                                if self.nb_tour == len(reseau.liste_pseudo):
                                    self.nb_tour = 0
                                if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                                    self.mon_tour = True
                                else:
                                    reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
                                envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
                            else:
                                self.nb_tour = -1
                                envoyer(reseau,menu," $fin_tour$ ",1)
                else:
                    self.deplacement = False
                    if self.de1 == self.de2:
                        self.nb_double += 1
                        self.nb_lance += 1
                        self.tour_prison = 0
                        self.liste_argent[self.nb_tour] -= 80
                        envoyer(reseau,menu," $liste_argent$ ",self.liste_argent)
                        self.pv[self.localisation][0].remove(self.nb_tour)
                        case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                        envoyer(reseau, menu, " $case$ ", case_envoie)
                        self.localisation = 10
                        self.pv[self.localisation][0].append(self.nb_tour)
                        case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
                        envoyer(reseau, menu, " $case$ ", case_envoie)
                        self.tour_prison = -1
                        self.nb_lance = 1
                        message_h = str(menu.pseudo) + " a fait un double et peut donc sortir de prison."
                        envoyer(reseau, menu, " $historique$ ", message_h)
                        if menu.type_joueur == "hébergeur":
                            board.liste_msg_h.append(message_h)
                    else:
                        self.tour_prison += 1
                        # Reset les variables utiles pendant pendant mon_tour
                        self.mon_tour = False
                        self.nb_lance = 1
                        self.nb_double = 0
                        self.new_case_ach = False
                        # On passe au tour suivant
                        if menu.type_joueur == "hébergeur":
                            self.nb_tour += 1
                            if self.nb_tour == len(reseau.liste_pseudo):
                                self.nb_tour = 0
                            if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                                self.mon_tour = True
                            else:
                                reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
                            envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
                        else:
                            self.nb_tour = -1
                            envoyer(reseau,menu," $fin_tour$ ",1)
        else:
            color = (255,255,255)
        pygame.draw.rect(fen, color, (337.5,533,225,75), 2)
        if self.tour_prison >= 0:
            mot = "Retour"
            self.deplacement = False
        else:
            mot = "Avancer"
        text = font.render(mot, 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,550))



    def aff_deplacement(self,reseau,menu,envoyer,carte,board,calcul_capital):
        """ Méthode permettant de déplacer le pion du joueur case par case. """
        self.total_de = self.de1 + self.de2 + 2
        self.pv[self.localisation][0].remove(self.nb_tour)
        case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
        envoyer(reseau, menu, " $case$ ", case_envoie)
        # Change le pion de position
        if self.total_de > 0:
            self.localisation += 1
        else:
            self.localisation -= 1
        # Compencement sur les bornes première / dernière cases
        if self.localisation == 40:
            self.localisation = 0
        elif self.localisation == -1:
            self.localisation = 39
        self.pv[self.localisation][0].append(self.nb_tour)
        case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
        envoyer(reseau, menu, " $case$ ", case_envoie)
        # Vérification du passage par la case départ
        if self.localisation == 0 and self.total_de > 0:
            self.liste_argent[self.nb_tour] += 200
            envoyer(reseau,menu," $liste_argent$ ",self.liste_argent)
        # Vérification de fin de déplacement ou non
        if self.total_de > 0:
            self.repere += 1
        else:
            self.repere -= 1
        if self.repere == self.total_de:
            self.gestion_case(reseau,menu,envoyer,carte,board,calcul_capital)
            self.deplacement = False
            self.repere = 0
            self.new_case_ach = True
        # Evite une attente inutile du premier deplacement sur la page des dés
        if self.repere != 1:
            sleep(0.25)



    def gestion_case(self,reseau,menu,envoyer,carte,board,calcul_capital):
        """ Gère les actions possible ou obligatoire lorsque le pion est arrivé
            à la case prévue par les dés. """
        if self.localisation == 30:
            # Case allez en prison
            self.tour_prison = 0
            self.pv[self.localisation][0].remove(self.nb_tour)
            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
            envoyer(reseau, menu, " $case$ ", case_envoie)
            self.localisation = 40
            self.pv[self.localisation][0].append(self.nb_tour)
            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
            envoyer(reseau, menu, " $case$ ", case_envoie)
            # Reset les variables utiles pendant pendant mon_tour
            self.mon_tour = False
            self.nb_lance = 1
            self.nb_double = 0
            self.new_case_ach = False
            # On passe au tour suivant
            message_h = str(menu.pseudo) + " va tout droit en prison."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
                self.nb_tour += 1
                if self.nb_tour == len(reseau.liste_pseudo):
                    self.nb_tour = 0
                if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                    self.mon_tour = True
                else:
                    reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
                envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
            else:
                self.nb_tour = -1
                envoyer(reseau,menu," $fin_tour$ ",1)
                
        elif self.localisation == 4:
            # Case impôts sur le revenu
            message_h = str(menu.pseudo) + " doit payer 200M pour ses impôts sur le revenu."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 200 >= 0:
                if self.liste_argent[self.nb_tour] - 200 >= 0:
                    self.liste_argent[self.nb_tour] -= 200
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = [200, -1]
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.localisation == 38:
            # Case taxe de luxe
            message_h = str(menu.pseudo) + " doit payer une taxe de 100M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 100 >= 0:
                if self.liste_argent[self.nb_tour] - 100 >= 0:
                    self.liste_argent[self.nb_tour] -= 100
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = [100, -1]
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer)
        elif self.localisation in [2,17,33]:
            # On est sur une case : caisse de communautée
            carte.carte_caissedecommu = True
            if menu.type_joueur == "hébergeur":
                self.nb_carte_commu = self.liste_caisse_de_commu[0]
                self.liste_caisse_de_commu.append(self.liste_caisse_de_commu[0])
                del self.liste_caisse_de_commu[0]
            else:
                envoyer(reseau, menu, " $nb_commu$ ", 0)
        elif self.localisation in [7,22,36]:
            # On est sur une case : chance
            carte.carte_chance = True
            if menu.type_joueur == "hébergeur":
                self.nb_carte_chance = self.liste_chance[0]
                self.liste_chance.append(self.liste_chance[0])
                del self.liste_chance[0]
            else:
                envoyer(reseau, menu, " $nb_chance$ ", 0)
        elif self.localisation in case_achetable and self.pv[self.localisation][1] != [] and self.pv[self.localisation][1] != self.nb_tour and self.localisation not in self.liste_hypotheque:
            # On tombe chez quelqu'un et donc on doit payer
            # On est sur une case simple : propriété de couleur
            if self.localisation in case_simple:
                for i in range(0,22):
                    if self.localisation == case_simple[i]:
                        paye = int(liste_prixpropriete[i][self.pv[self.localisation][2]])
                        # On vérifie si il faut doubler le terrain nu suite à un groupe complet
                        if self.pv[self.localisation][2] == 0:
                            compteur = 0
                            while self.localisation not in liste_secteur[compteur]:
                                compteur += 1
                            total_proprio = 0
                            for case in liste_secteur[compteur]:
                                if self.pv[case][1] == self.pv[self.localisation][1]:
                                    total_proprio += 1
                            if total_proprio == len(liste_secteur[compteur]):
                                paye *= 2
                        break
            # On est sur une gare
            elif self.localisation in case_gare:
                nb_gare_joueur = 0
                for repere in case_gare:
                    if self.pv[self.localisation][1] == self.pv[repere][1]:
                        nb_gare_joueur += 1
                paye = int(liste_prixpropriete[22][nb_gare_joueur-1])
            # On est alors sur une compagnie d'électricité / eaux
            else:
                nb_compagnie_joueur = 0
                for repere in case_compagnie:
                    if self.pv[self.localisation][1] == self.pv[repere][1]:
                        nb_compagnie_joueur += 1
                if nb_compagnie_joueur == 1:
                    paye = self.total_de * 4
                else:
                    paye = self.total_de * 10
            message_h = str(menu.pseudo) + " doit payer " + str(paye) + "M à " + str(reseau.liste_pseudo[self.pv[self.localisation][1]])
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - paye >= 0:
                if self.liste_argent[self.nb_tour] >= paye:
                    self.liste_argent[self.nb_tour] -= paye
                    self.liste_argent[self.pv[self.localisation][1]] += paye
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (paye, self.pv[self.localisation][1])
                    self.doit_hypothequer = True
            else:
                self.liste_argent[self.pv[self.localisation][1]] += capital
                envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                message_h = str(menu.pseudo) + " n'a qu'un capital de " + str(capital) + "M."
                envoyer(reseau, menu, " $historique$ ", message_h)
                if menu.type_joueur == "hébergeur":
                    board.liste_msg_h.append(message_h)
                self.action_loose(reseau,menu,envoyer,board)



    def serveur_analyse(self,reseau,convertisseur,envoyer,menu,board):
        """ Méthode permettant d'analyser les données reçues envoyer par
            les clients. """
        client_a_lire = []
        client_a_lire, wlist, xlist = select.select(self.liste_connexion_serv,
                    [], [], 0)
        for client in client_a_lire:
            nb = 1
            while client != reseau.liste_connexion_serv[nb-1]:
                nb += 1
            donnee = client.recv(1024).decode()
            donnee = convertisseur(donnee)
            classeur = []
            for une_donnee in donnee:
                if une_donnee in ["$historique$","$message$","$fin_tour$",
                                  "$case$","$liste_argent$","$nb_commu$",
                                  "$nb_chance$","$liste_loose$","$obligation$",
                                  "$liste_hypotheque$","$doit_payer$"]:
                    classeur.append([une_donnee])
                else:
                    classeur[len(classeur)-1].append(une_donnee)
            for i in range(0,len(classeur)):
                if classeur[i][0] == "$fin_tour$":
                    self.nb_tour += 1
                    if self.nb_tour == len(reseau.liste_pseudo):
                        self.nb_tour = 0
                    while self.liste_loose[self.nb_tour] == True:
                        self.nb_tour += 1
                        if self.nb_tour == len(reseau.liste_pseudo):
                            self.nb_tour = 0
                    if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                        self.mon_tour = True
                    else:
                        reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
                    envoyer(reseau, menu, " $nb_tour$ ", self.nb_tour)
                elif classeur[i][0] == "$case$":
                    case = []
                    for info in classeur[i][2:len(classeur[i])]:
                        if str(info) in "pjm":
                            case.append([])
                        else:
                            case[-1].append(info)
                    if case[1] != []:
                        case[1] = case[1][0]
                    if case[2] != []:
                        case[2] = case[2][0]
                    self.pv[classeur[i][1]] = case
                    case_envoie = [classeur[i][1], "p", self.pv[classeur[i][1]][0], "j", self.pv[classeur[i][1]][1], "m", self.pv[classeur[i][1]][2]]
                    envoyer(reseau, menu, " $case$ ", case_envoie)
                elif classeur[i][0] == "$liste_argent$":
                    self.liste_argent = classeur[i][1:len(classeur[i])]
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                elif classeur[i][0] == "$nb_commu$":
                    self.liste_caisse_de_commu.append(self.liste_caisse_de_commu[0])
                    envoyer(reseau, menu, " $nb_commu$ ", self.liste_caisse_de_commu[0])
                    del self.liste_caisse_de_commu[0]
                elif classeur[i][0] == "$nb_chance$":
                    self.liste_chance.append(self.liste_chance[0])
                    envoyer(reseau, menu, " $nb_chance$ ", self.liste_chance[0])
                    del self.liste_chance[0]
                elif classeur[i][0] == "$message$":
                    message = ""
                    board.liste_msg.append(classeur[i][1])
                    envoyer(reseau, menu, " $message$ ", classeur[i][1])
                    if board.chat == False:
                        board.notif = True
                elif classeur[i][0] == "$historique$":
                    message = ""
                    board.liste_msg_h.append(classeur[i][1])
                    envoyer(reseau, menu, " $historique$ ", classeur[i][1])
                elif classeur[i][0] == "$liste_loose$":
                    self.liste_loose = classeur[i][1:len(classeur[i])]
                    envoyer(reseau, menu, " $liste_loose$ ", self.liste_loose)
                elif classeur[i][0] == "$liste_hypotheque$":
                    self.liste_hypotheque = classeur[i][1:len(classeur[i])]
                    envoyer(reseau, menu, " $liste_hypotheque$ ", self.liste_hypotheque)
                elif classeur[i][0] == "$doit_payer$":
                    self.doit_payer = classeur[i][1:len(classeur[i])]
                    envoyer(reseau, menu, " $doit_payer$ ", self.doit_payer)
                elif classeur[i][0] == "$obligation$":
                    compteur = 0
                    while reseau.liste_pseudo[compteur] != menu.pseudo:
                        compteur += 1
                    if classeur[i][1] == "doit_loose":
                        if classeur[i][2] == compteur:
                            self.action_loose(reseau,menu,envoyer,board)
                        else:
                            envoyer(reseau, menu, " $obligation$ ", [classeur[i][1],classeur[i][2]])
                    else:
                        if classeur[i][2] == compteur:
                            self.dette = [10, classeur[i][3]]
                            self.doit_hypothequer = True
                        else:
                            envoyer(reseau, menu, " $obligation$ ", [classeur[i][1],classeur[i][2],classeur[i][3]])
                            


    def aff_complement(self):
        """ Méthode permettant d'afficher les pions / maisons / hôtels. """
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 10)
        for case in range(0,41):
            nb_pion = len(self.pv[case][0])
            nb = 0
            batiment = self.pv[case][2]
            if case == 0:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (821.5,821.5))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (795.33+52.33*i,821.5))
                elif nb_pion == 3:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (795.33+52.33*i,795.33))
                    fen.blit(pion[self.pv[case][0][2]], (821.5,847.66))
                elif nb_pion == 4:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (795.33+52.33*i,795.33+52.33*j))
                            nb += 1
                elif nb_pion == 5:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (795.33+52.33*i,795.33+52.33*j))
                            nb += 1
                    fen.blit(pion[self.pv[case][0][nb]], (821.5,821.5))
            elif case >= 1 and case <= 9:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (726-74*(case-1),840))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (714+24*i-74*(case-1),840))
                elif nb_pion == 3:
                    for i in range(0,3):
                        fen.blit(pion[self.pv[case][0][i]], (704+23*i-74*(case-1),840))
                elif nb_pion == 4:
                    for i in range(0,4):
                        fen.blit(pion[self.pv[case][0][i]], (704+15*i-74*(case-1),840))
                elif nb_pion == 5:
                    for i in range(0,5):
                        fen.blit(pion[self.pv[case][0][i]], (704+11.5*i-74*(case-1),840))
                if batiment > 0 and case in [1,3,6,8,9]:
                    if self.pv[case][2] != 5:
                        fen.blit(maison, (713-74*(case-1),787))
                        pygame.draw.circle(fen, (0,0,0), (748-74*(case-1),797), 11, 0)
                        text = font.render(str(self.pv[case][2]), 0, (255,255,255))
                        fen.blit(text, (745-74*(case-1),792))
                    else:
                        fen.blit(hotel, (713-74*(case-1),787))
            elif case == 10:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (-4,821.5))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (-4,793+55*i))
                elif nb_pion == 3:
                    for i in range(0,3):
                        fen.blit(pion[self.pv[case][0][i]], (-4,783+38*i))
                elif nb_pion == 4:
                    for i in range(0,4):
                        fen.blit(pion[self.pv[case][0][i]], (-4,783+25*i))
                elif nb_pion == 5:
                    for i in range(0,5):
                        fen.blit(pion[self.pv[case][0][i]], (-4,783+18.5*i))
            elif case >= 11 and case <= 19:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (18,726-74*(case-11)))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (7.5+22.5*i,726-74*(case-11)))
                elif nb_pion == 3:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (7.5+22.5*i,711-74*(case-11)))
                    fen.blit(pion[self.pv[case][0][2]], (18,738-74*(case-11)))
                elif nb_pion == 4:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (7.5+22.5*i,711+27*j-74*(case-11)))
                            nb += 1
                elif nb_pion == 5:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (7.5+22.5*i,711+27*j-74*(case-11)))
                            nb += 1
                    fen.blit(pion[self.pv[case][0][nb]], (18,726-74*(case-11)))
                if batiment > 0 and case in [11,13,14,16,18,19]:
                    if self.pv[case][2] != 5:
                        fen.blit(maison, (93,713-74*(case-11)))
                        pygame.draw.circle(fen, (0,0,0), (104,747-74*(case-11)), 11, 0)
                        text = font.render(str(self.pv[case][2]), 0, (255,255,255))
                        fen.blit(text, (101,741-74*(case-11)))
                    else:
                        fen.blit(hotel, (93.75,716-74*(case-11)))
            elif case == 20:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (38.5,38.5))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (12.33+52.33*i,38.5))
                elif nb_pion == 3:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (12.33+52.33*i,12.33))
                    fen.blit(pion[self.pv[case][0][2]], (38.5,64.66))
                elif nb_pion == 4:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (12.33+52.33*i,12.33+52.33*j))
                            nb += 1
                elif nb_pion == 5:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (12.33+52.33*i,12.33+52.33*j))
                            nb += 1
                    fen.blit(pion[self.pv[case][0][nb]], (38.5,38.5))
            elif case >= 21 and case <= 29:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (134+74*(case-21),20))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (146-24*i+74*(case-21),20))
                elif nb_pion == 3:
                    for i in range(0,3):
                        fen.blit(pion[self.pv[case][0][i]], (156-22*i+74*(case-21),20))
                elif nb_pion == 4:
                    for i in range(0,4):
                        fen.blit(pion[self.pv[case][0][i]], (156-14.5*i+74*(case-21),20))
                elif nb_pion == 5:
                    for i in range(0,5):
                        fen.blit(pion[self.pv[case][0][i]], (156-11*i+74*(case-21),20))
                if batiment > 0 and case in [21,23,24,26,27,29]:
                    if self.pv[case][2] != 5:
                        fen.blit(maison, (166+74*(case-21),94))
                        pygame.draw.circle(fen, (0,0,0), (153+74*(case-21),104), 11, 0)
                        text = font.render(str(self.pv[case][2]), 0, (255,255,255))
                        fen.blit(text, (150+74*(case-21),98))
                    else:
                        fen.blit(hotel, (166+74*(case-21),94))
            elif case == 30:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (821.5,38.5))
            elif case >= 31 and case <=39:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (842,132+74*(case-31)))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (831.5+22.5*i,132+74*(case-31)))
                elif nb_pion == 3:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (831.5+22.5*i,119+74*(case-31)))
                    fen.blit(pion[self.pv[case][0][2]], (842,146+74*(case-31)))
                elif nb_pion == 4:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (831.5+22.5*i,119+27*j+74*(case-31)))
                            nb += 1
                elif nb_pion == 5:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (831.5+22.5*i,119+27*j+74*(case-31)))
                            nb += 1
                    fen.blit(pion[self.pv[case][0][nb]], (842,132+74*(case-31)))
                if batiment > 0 and case in [31,32,34,37,39]:
                    if self.pv[case][2] != 5:
                        fen.blit(maison, (787,167.75+74*(case-31)))
                        pygame.draw.circle(fen, (0,0,0), (796,153+74*(case-31)), 11, 0)
                        text = font.render(str(self.pv[case][2]), 0, (255,255,255))
                        fen.blit(text, (793.5,148+74*(case-31)))
                    else:
                        fen.blit(hotel, (787,167.75+74*(case-31)))
            elif case == 40:
                if nb_pion == 1:
                    fen.blit(pion[self.pv[case][0][0]], (54.5,805.5))
                elif nb_pion == 2:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (34.5+40*i,805.5))
                elif nb_pion == 3:
                    for i in range(0,2):
                        fen.blit(pion[self.pv[case][0][i]], (34.5+40*i,785.5))
                    fen.blit(pion[self.pv[case][0][2]], (54.5,825.5))
                elif nb_pion == 4:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (34.5+40*i,785.5+40*j))
                            nb += 1
                elif nb_pion == 5:
                    for i in range(0,2):
                        for j in range(0,2):
                            fen.blit(pion[self.pv[case][0][nb]], (34.5+40*i,785.5+40*j))
                            nb += 1
                    fen.blit(pion[self.pv[case][0][nb]], (54.5,805.5))



    def gestion_chance(self,reseau,menu,envoyer,board,calcul_capital):
        """ Méthode permettant de gérer l'arrivée sur une case d'un pion."""
        if self.nb_carte_chance == 0:
            # Avancez jusqu'à la case départ
            message_h = str(menu.pseudo) + " doit se rendre à la case départ."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 40 - self.localisation
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_chance == 1:
            # Vous devez toucher 150M
            self.liste_argent[self.nb_tour] += 150
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
            message_h = str(menu.pseudo) + " reçoit 150M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
        elif self.nb_carte_chance == 2:
            # Rendez-vous à l'avenue Henri-Martin
            message_h = str(menu.pseudo) + " doit se rendre à l'Avenue Henri-Martin."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 24 - self.localisation
            if delta < 0:
                delta += 40
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_chance == 3:
            # La Banque vous verse un dividende de 50M
            message_h = str(menu.pseudo) + " reçoit 50M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 50
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_chance == 4:
            # Avancez au Boulevard de la Villette
            message_h = str(menu.pseudo) + " doit se rendre au Boulevard de la Villette."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 11 - self.localisation
            if delta < 0:
                delta += 40
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_chance == 5:
            # Reculez de trois cases
            message_h = str(menu.pseudo) + " recule de 3 cases."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.de1, self.de2 = 0, -5
            self.deplacement = True
        elif self.nb_carte_chance == 6:
            # Payez pour frais de scolarité 150M
            message_h = str(menu.pseudo) + " doit payer 150M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 150 >= 0:
                if self.liste_argent[self.nb_tour] - 150 >= 0:
                    self.liste_argent[self.nb_tour] -= 150
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (150, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_chance == 7:
            # 40M par maison et 115M par hôtel
            taxe = 0
            for case in range(0,40):
                if self.pv[case][1] == self.nb_tour and self.pv[case][2] != []:
                    if self.pv[case][2] > 0 and self.pv[case][2] < 5:
                        taxe += 40
                    elif self.pv[case][2] == 5:
                        taxe += 115
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - taxe >= 0:
                if self.liste_argent[self.nb_tour] - taxe >= 0:
                    self.liste_argent[self.nb_tour] -= taxe
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (taxe, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
            message_h = str(menu.pseudo) + " doit payer 40M par maisons et 115M par hôtels. Soit une taxe de " + str(taxe) + "M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
        elif self.nb_carte_chance == 8:
            # Amende pour excès de vitesse : 15M
            message_h = str(menu.pseudo) + " doit payer 15M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 15 >= 0:
                if self.liste_argent[self.nb_tour] - 15 >= 0:
                    self.liste_argent[self.nb_tour] -= 15
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (15, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_chance == 9:
            # Allez à la gare de Lyon
            message_h = str(menu.pseudo) + " doit se rendre à la Gare de Lyon."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 15 - self.localisation
            if delta < 0:
                delta += 40
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_chance == 10:
            # Rendez-vous à la Rue de la Paix
            message_h = str(menu.pseudo) + " doit se rendre à la Rue de la Paix."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 39 - self.localisation
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_chance == 11:
            # Vous avez gagnez le prix des mots croisés. Recevez 100M
            message_h = str(menu.pseudo) + " reçoit 100M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 100
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_chance == 12:
            # Avancez tout droit en prison
            message_h = str(menu.pseudo) + " se rend tout droit en prison."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.tour_prison = 0
            self.pv[self.localisation][0].remove(self.nb_tour)
            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
            envoyer(reseau, menu, " $case$ ", case_envoie)
            self.localisation = 40
            self.pv[self.localisation][0].append(self.nb_tour)
            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
            envoyer(reseau, menu, " $case$ ", case_envoie)
            # Reset les variables utiles pendant pendant mon_tour
            self.mon_tour = False
            self.nb_lance = 1
            self.nb_double = 0
            self.new_case_ach = False
            # On passe au tour suivant
            if menu.type_joueur == "hébergeur":
                self.nb_tour += 1
                if self.nb_tour == len(reseau.liste_pseudo):
                    self.nb_tour = 0
                if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                    self.mon_tour = True
                else:
                    reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
                envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
            else:
                self.nb_tour = -1
                envoyer(reseau,menu," $fin_tour$ ",1)
        elif self.nb_carte_chance == 13:
            # Versez pour chaque maison 25M et pour chaque hôtel 100M
            taxe = 0
            for case in range(0,40):
                if self.pv[case][1] == self.nb_tour and self.pv[case][2] != []:
                    if self.pv[case][2] > 0 and self.pv[case][2] < 5:
                        taxe += 25
                    elif self.pv[case][2] == 5:
                        taxe += 100
            message_h = str(menu.pseudo) + " doit payer 25M par maisons et 100M par hôtels. Soit une taxe de " + str(taxe) + "M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - taxe >= 0:
                if self.liste_argent[self.nb_tour] - taxe >= 0:
                    self.liste_argent[self.nb_tour] -= taxe
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (taxe, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_chance == 14:
            # Amende pour ivresse: 20M
            message_h = str(menu.pseudo) + " doit payer 20M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 20 >= 0:
                if self.liste_argent[self.nb_tour] - 20 >= 0:
                    self.liste_argent[self.nb_tour] -= 20
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (20, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_chance == 15:
            # Vous êtes libéré de prison
            message_h = str(menu.pseudo) + " obitent une carte : vous êtes libéré de prison."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.nb_libere_prison += 1
        self.nb_carte_chance = -1



    def gestion_caissedecommu(self,reseau,menu,envoyer,board,calcul_capital):
        """ Méthodes permetant de gérer l'arrivée sur une case caisse de commu. """
        if self.nb_carte_commu == 0:
            #Payez à l'hôpital 100M
            message_h = str(menu.pseudo) + " doit payer 100M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 100 >= 0:
                if self.liste_argent[self.nb_tour] - 100 >= 0:
                    self.liste_argent[self.nb_tour] -= 100
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (100, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_commu == 1:
            #Recevez votre intérêt sur l'emprunt à 7% : 25M
            message_h = str(menu.pseudo) + " reçoit 25M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 25
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_commu == 2:
            #C'est votre anniversaire chaque joueur vous verse 10M
            message_h = "Tous les joueurs versent 10M à " + str(menu.pseudo) + "."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            nb_joueur = len(self.liste_argent)
            self.doit_payer = [True] * nb_joueur
            a_envoyer = []
            for num_joueur in range(0,nb_joueur):
                if num_joueur == self.nb_tour or self.liste_loose[num_joueur] == True:
                    self.doit_payer[num_joueur] = False
                else:
                    capital = calcul_capital(num_joueur, self.liste_argent, self.pv, self.liste_hypotheque)
                    if capital < 10:
                        self.doit_payer[num_joueur] = False
                        self.liste_argent[self.nb_tour] += capital
                        a_envoyer.append(["doit_loose", num_joueur])
                    else:
                        if self.liste_argent[num_joueur] >= 10:
                            self.liste_argent[self.nb_tour] += 10
                            self.liste_argent[num_joueur] -= 10
                            self.doit_payer[num_joueur] = False
                        else:
                            a_envoyer.append(["doit_payer", num_joueur, self.nb_tour])
                            self.doit_payer
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
            envoyer(reseau, menu, " $doit_payer$ ", self.doit_payer)
            for message in a_envoyer:
                envoyer(reseau, menu, " $obligation$ ", message)
        elif self.nb_carte_commu == 3:
            #Les contributions vous remboursent la somme de 20M
            message_h = str(menu.pseudo) + " reçoit 20M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 20
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_commu == 4:
            #Erreur de la banque en votre faveur recevez 200M
            message_h = str(menu.pseudo) + " reçoit 200M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 200
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_commu == 5:
            #Payez la note du médecin 50M
            message_h = str(menu.pseudo) + " doit payer 50M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 50 >= 0:
                if self.liste_argent[self.nb_tour] - 50 >= 0:
                    self.liste_argent[self.nb_tour] -= 50
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (50, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_commu == 6:
            #Vous héritez de 100M
            message_h = str(menu.pseudo) + " reçoit 100M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 100
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_commu == 7:
            #Payez votre Police d'Assurance s'élevant à 50M
            message_h = str(menu.pseudo) + " doit payer 50M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            capital = calcul_capital(self.nb_tour, self.liste_argent, self.pv, self.liste_hypotheque)
            if capital - 50 >= 0:
                if self.liste_argent[self.nb_tour] - 50 >= 0:
                    self.liste_argent[self.nb_tour] -= 50
                    envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                else:
                    self.dette = (50, -1)
                    self.doit_hypothequer = True
            else:
                self.action_loose(reseau,menu,envoyer,board)
        elif self.nb_carte_commu == 8:
            #Recevez votre revenu annuel 100M
            message_h = str(menu.pseudo) + " reçoit 100M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 100
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_commu == 9:
            #Retournez à Belleville
            message_h = str(menu.pseudo) + " doit se rendre à Belleville."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 1 - self.localisation
            if delta < 0:
                delta += 40
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_commu == 10:
            #Allez à la case départ
            message_h = str(menu.pseudo) + " doit se rendre à la case départ."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            delta = 40 - self.localisation
            self.de1, self.de2 = 0, delta - 2
            self.deplacement = True
        elif self.nb_carte_commu == 11:
            #Vous êtes libéré de prison
            message_h = str(menu.pseudo) + " botient une carte : vous êtes libéré de prison."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.nb_libere_prison += 1
        elif self.nb_carte_commu == 12:
            # Allez en prison
            message_h = str(menu.pseudo) + " va tout droit en prison."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.tour_prison = 0
            self.pv[self.localisation][0].remove(self.nb_tour)
            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
            envoyer(reseau, menu, " $case$ ", case_envoie)
            self.localisation = 40
            self.pv[self.localisation][0].append(self.nb_tour)
            case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
            envoyer(reseau, menu, " $case$ ", case_envoie)
            # Reset les variables utiles pendant pendant mon_tour
            self.mon_tour = False
            self.nb_lance = 1
            self.nb_double = 0
            self.new_case_ach = False
            # On passe au tour suivant
            if menu.type_joueur == "hébergeur":
                self.nb_tour += 1
                if self.nb_tour == len(reseau.liste_pseudo):
                    self.nb_tour = 0
                if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                    self.mon_tour = True
                else:
                    reseau.liste_connexion_serv[self.nb_tour].send(("mon_tour True").encode())
                envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
            else:
                self.nb_tour = -1
                envoyer(reseau,menu," $fin_tour$ ",1)
        elif self.nb_carte_commu == 14:
            #Vous avez gagné le deuxième Prix de Beauté, Recevez 10M
            message_h = str(menu.pseudo) + " reçoit 10M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 10
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        elif self.nb_carte_commu == 15:
            #La vente de votre stock vous rapporte 50M
            message_h = str(menu.pseudo) + " reçoit 50M."
            envoyer(reseau, menu, " $historique$ ", message_h)
            if menu.type_joueur == "hébergeur":
                board.liste_msg_h.append(message_h)
            self.liste_argent[self.nb_tour] += 50
            envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)           
        self.nb_carte_commu = -1



    def aff_win(self,reseau):
        """ Affiche le gagnant de la partie sur l'écran du jeu. """
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        compteur = 0
        while self.liste_loose[compteur] != False:
            compteur +=1
        police = "datas/font/verdanab.ttf"
        font = pygame.font.Font(police, 75)
        text = font.render("FIN DE LA PARTIE", 0, (248, 211, 3))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,180))
        police = "datas/font/verdana.ttf"
        font = pygame.font.Font(police, 60)
        text = font.render(str(reseau.liste_pseudo[compteur]), 0, (255, 255, 255))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,525))
        text = font.render("a gagné.", 0, (255, 255, 255))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,600))



    def action_loose(self,reseau,menu,envoyer,board):
        compteur = 0
        while reseau.liste_pseudo[compteur] != menu.pseudo:
            compteur += 1
        self.liste_loose[compteur] = True
        self.liste_argent[compteur] = 0
        envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
        envoyer(reseau, menu, " $liste_loose$ ", self.liste_loose)
        for case in case_achetable:
            if self.pv[case][1] == compteur:
                if case in self.liste_hypotheque:
                    compteur2 = 0
                    while self.liste_hypotheque[compteur2] != case:
                        compteur2 += 1
                    del self.liste_hypotheque[compteur2]
                    envoyer(reseau,menu," $liste_hypotheque$ ", self.liste_hypotheque)
                self.pv[case][1] = []
                self.pv[case][2] = 0
                case_envoie = [case, "p", self.pv[case][0], "j", self.pv[case][1], "m", self.pv[case][2]]
                envoyer(reseau, menu, " $case$ ", case_envoie)
        i = 0
        while self.pv[self.localisation][0][i] != compteur:
            i += 1
        del self.pv[self.localisation][0][i]
        case_envoie = [self.localisation, "p", self.pv[self.localisation][0], "j", self.pv[self.localisation][1], "m", self.pv[self.localisation][2]]
        envoyer(reseau, menu, " $case$ ", case_envoie)
        message_h = str(menu.pseudo) + " a fait faillite !"
        envoyer(reseau, menu, " $historique$ ", message_h)
        if menu.type_joueur == "hébergeur":
            board.liste_msg_h.append(message_h)
        # On passe au tour suivant
        if menu.type_joueur == "hébergeur":
            board.liste_msg_h.append(message_h)
            self.nb_tour += 1
            if self.nb_tour == len(reseau.liste_pseudo):
                self.nb_tour = 0
            if reseau.liste_connexion_serv[self.nb_tour] == "hébergeur":
                self.mon_tour = True
            else:
                reseau.liste_connexion_serv[self.nb_tour].send((" $mon_tour$ True").encode())
            envoyer(reseau,menu," $nb_tour$ ",self.nb_tour)
        else:
            self.nb_tour = -1
            envoyer(reseau,menu," $fin_tour$ ",1)



    def aff_hypothequer(self,reseau,menu,envoyer,calcul_capital):
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        pygame.draw.rect(fen, (0,0,0), (100,150,700,450))
        pygame.draw.rect(fen, (237,27,26), (100,150,700,450),1)
        police = "datas/font/verdanab.ttf"
        font = pygame.font.Font(police, 40)
        text = font.render("ERREUR DE TRANSACTION", 0, (237,27,26))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,180))
        font = pygame.font.Font("datas/font/verdana.ttf", 35)
        compteur = 0
        while reseau.liste_pseudo[compteur] != menu.pseudo:
            compteur += 1
        message = ["Veuillez hypothéquer ou","vendre des bâtiments","afin de payer votre dette de",str(self.dette[0]) + "M.","","Votre argent : " + str(self.liste_argent[compteur]) + "M"]
        compteur2 = 0
        for ligne in message:
            text = font.render(message[compteur2], 0, (255,255,255))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,250+55*compteur2))
            compteur2 += 1
        # Boutron Payer la dette
        if self.dette[1] != -2:
            font = pygame.font.Font("datas/font/verdana.ttf", 40)
            pygame.draw.rect(fen, (0,0,0), (275,633,350,75))
            if self.liste_argent[compteur] >= self.dette[0]:
                if self.position[0] > 275 and self.position[0] < 625 and self.position[1] > 630 and self.position[1] < 715:
                    color = (237,27,26)
                    if self.clic == 1:
                        self.liste_argent[compteur] -= self.dette[0]
                        if self.dette[1] >= 0:
                            self.liste_argent[self.dette[1]] += self.dette[0]
                            if self.doit_payer[compteur] == True:
                                self.doit_payer[compteur] = False
                                envoyer(reseau, menu, " $doit_payer$ ", self.doit_payer)
                        envoyer(reseau, menu, " $liste_argent$ ", self.liste_argent)
                        self.doit_hypothequer = False
                        self.dette = [0, -1]
                else:
                    color = (255,255,255)
            else:
                color = (126,126,126)
            pygame.draw.rect(fen, color, (275,633,350,75), 2)
            text = font.render("Payer la dette", 0, color)
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,645))
        else:
            if self.liste_argent[compteur] >= self.dette[0]:
                self.doit_hypothequer = False
                self.dette = [0, -1]



    def aff_attente_payement(self):
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        pygame.draw.rect(fen, (0,0,0), (100,150,700,450))
        pygame.draw.rect(fen, (237,27,26), (100,150,700,450),1)
        police = "datas/font/verdanab.ttf"
        font = pygame.font.Font(police, 40)
        text = font.render("ATTENTE DE TRANSACTION", 0, (237,27,26))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,180))
        font = pygame.font.Font("datas/font/verdana.ttf", 35)
        message = ["Veuillez attendre que tous","les joueurs vous versent 10M."]
        compteur2 = 0
        for ligne in message:
            text = font.render(message[compteur2], 0, (255,255,255))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,350+55*compteur2))
            compteur2 += 1
        


class CARTE:
    """ Classe gérant les cartes chance,caisse de communauté.
        Méthodes : aff_carte_chance, aff_carte_caissedecommu,
        aff_carte_propriete """
    
    def __init__(self,jeu):
        self.carte_chance = False
        self.carte_caissedecommu = False
        self.position = jeu.position
        self.clic = jeu.clic


        
    def aff_carte_chance(self,jeu,reseau,menu,envoyer,board,calcul_capital):
        """ Affiche la carte chance demandé."""
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        pygame.draw.rect(fen, (255,255,255), (100,300,700,300))
        pygame.draw.rect(fen, (236,20,13), (100,300,700,300),3)
        pygame.draw.rect(fen, (236,20,13), (115,315,670,270),3)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 25)
        aff_texte=[]
        texte_decoupe=texte_chance[jeu.nb_carte_chance].split()
        while len(texte_decoupe)>=2:
            if len(texte_decoupe[0])+len(texte_decoupe[1])<30:
                texte_decoupe[0]+=" "+texte_decoupe[1]
                del texte_decoupe[1]
            else:
                aff_texte.append(texte_decoupe[0])
                del texte_decoupe[0]
        aff_texte.append(texte_decoupe[0])
        compteur = 0
        for ligne in aff_texte:
                text = font.render(ligne, 0, (0,0,0))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                if len(aff_texte) == 1:
                    y = 445+compteur*40
                elif len(aff_texte) == 2:
                    y = 430+compteur*40
                elif len(aff_texte) == 3:
                    y = 415+compteur*40
                else:
                    y = 400+compteur*40
                fen.blit(text, (text_centre[0]-225,y))
                compteur+=1
        font = pygame.font.Font("datas/font/unispace_bd.ttf", 30)
        text = font.render("Carte Chance", 0, (236,20,13))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,325))
        # Bouton Suivant
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
        pygame.draw.rect(fen, (0,0,0), (337.5,633,225,75))
        if self.position[0] > 337.5 and self.position[0] < 567.5 and self.position[1] > 630 and self.position[1] < 715:
            color = (237,27,26)
            if self.clic == 1:
                self.carte_chance = False
                jeu.gestion_chance(reseau,menu,envoyer,board,calcul_capital)
        else:
            color = (255,255,255)
        pygame.draw.rect(fen, color, (337.5,633,225,75), 2)
        text = font.render("Suivant", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,650))


        
    def aff_carte_caissedecommu(self,jeu,reseau,menu,envoyer,board,calcul_capital):
        """ Affiche la carte de caisse de communauté demandé."""
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        pygame.draw.rect(fen, (255,255,255), (100,300,700,300))
        pygame.draw.rect(fen, (40,144,209), (100,300,700,300),3)
        pygame.draw.rect(fen, (40,144,209), (115,315,670,270),3)
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 25)
        aff_texte=[]
        texte_decoupe=texte_caissedecommu[jeu.nb_carte_commu].split()
        while len(texte_decoupe)>=2:
            if len(texte_decoupe[0])+len(texte_decoupe[1])<30:
                texte_decoupe[0]+=" "+texte_decoupe[1]
                del texte_decoupe[1]
            else:
                aff_texte.append(texte_decoupe[0])
                del texte_decoupe[0]
        aff_texte.append(texte_decoupe[0])
        compteur = 0
        for ligne in aff_texte:
                text = font.render(ligne, 0, (0,0,0))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                if len(aff_texte) == 1:
                    y = 445+compteur*40
                    
                elif len(aff_texte) == 2:
                    y = 430+compteur*40
                    
                elif len(aff_texte) == 3:
                    y = 415+compteur*40
                else:
                    y = 400+compteur*40
                    
                fen.blit(text, (text_centre[0]-225,y))
                compteur+=1
        font = pygame.font.Font("datas/font/unispace_bd.ttf", 30)
        text = font.render("Carte Caisse de Communauté", 0, (40,144,209))
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-225,325))
        if jeu.nb_carte_commu != 13:
            # Bouton Suivant
            font = pygame.font.Font("datas/font/unispace_rg.ttf", 40)
            pygame.draw.rect(fen, (0,0,0), (337.5,633,225,75))
            if self.position[0] > 337.5 and self.position[0] < 567.5 and self.position[1] > 630 and self.position[1] < 715:
                color = (237,27,26)
                if self.clic == 1:
                    self.carte_caissedecommu = False
                    jeu.gestion_caissedecommu(reseau,menu,envoyer,board,calcul_capital)
            else:
                color = (255,255,255)
            pygame.draw.rect(fen, color, (337.5,633,225,75), 2)
            text = font.render("Suivant", 0, color)
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,650))
        else:
            #Bouton Payez 10M
            font = pygame.font.Font("datas/font/unispace_rg.ttf", 30)
            pygame.draw.rect(fen, (0,0,0), (237.5,633,425,70))
            if jeu.liste_argent[jeu.nb_tour] - 10 >= 10:
                if self.position[0] > 237.5 and self.position[0] < 662.5 and self.position[1] > 633 and self.position[1] < 708:
                    color = (237,27,26)
                    if self.clic == 1:
                        message_h = str(menu.pseudo) + " doit payer 10M."
                        envoyer(reseau, menu, " $historique$ ", message_h)
                        if menu.type_joueur == "hébergeur":
                            board.liste_msg_h.append(message_h)
                        jeu.liste_argent[jeu.nb_tour] -= 10
                        envoyer(reseau, menu, " $liste_argent$ ", jeu.liste_argent)
                        self.carte_caissedecommu = False
                else:
                    color = (255,255,255)
            else:
                color = (126.,126,126)
            pygame.draw.rect(fen, color, (237.5,633,425,70), 2)
            text = font.render("Payez 10M", 0, color)
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,655))
            #Bouton Tirez une carte chance
            font = pygame.font.Font("datas/font/unispace_rg.ttf", 30)
            pygame.draw.rect(fen, (0,0,0), (237.5,715,425,70))
            if self.position[0] > 237.5 and self.position[0] < 662.5 and self.position[1] > 715 and self.position[1] < 785:
                color = (237,27,26)       
                if self.clic == 1:
                    message_h = str(menu.pseudo) + " tire une carte chance."
                    envoyer(reseau, menu, " $historique$ ", message_h)
                    if menu.type_joueur == "hébergeur":
                        board.liste_msg_h.append(message_h)
                    self.carte_chance = True
                    if menu.type_joueur == "hébergeur":
                        jeu.nb_carte_chance = jeu.liste_chance[0]
                        jeu.liste_chance.append(jeu.liste_chance[0])
                        del jeu.liste_chance[0]
                    else:
                        envoyer(reseau, menu, " $nb_chance$ ", 0)
                    self.carte_caissedecommu = False     
            else:
                color = (255,255,255)
            pygame.draw.rect(fen, color, (237.5,715,425,70), 2)
            text = font.render("Tirez une carte chance", 0, color)
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,735))



    def aff_carte_propriete(self,board):
        police = "datas/font/verdana.ttf"
        font = pygame.font.Font(police, 25)
        fond = pygame.Surface((900,900))
        fond.set_alpha(220)
        fond.fill((0,0,0))
        fen.blit(fond,(0,0))
        if board.secteur == 8:
            pygame.draw.rect(fen, (255,255,255), (250,100,400,700))
            pygame.draw.rect(fen, (0,0,0), (250,100,400,700),3)
            pygame.draw.rect(fen, (0,0,0), (265,115,370,670),3)
            fen.blit(train2, (285,120))
            c=[]
            b=liste_propriete[board.secteur][board.num_ville].split()
            while len(b)>=2:
                if len(b[0])+len(b[1])<10:
                    b[0]+=" "+b[1]
                    del b[1]
                else:
                    c.append(b[0])
                    del b[0]
            c.append(b[0])
            compteur = 0
            for ligne in c:
                text = font.render(ligne, 0, (0,0,0))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                fen.blit(text, (text_centre[0]-225,400+compteur*40))
                compteur+=1
            font = pygame.font.Font(police, 20)
            text = font.render("LOYER  Avec 1 gare", 0, (0,0,0))
            fen.blit(text, (280,520))
            text = font.render("LOYER  Avec 2 gares", 0, (0,0,0))
            fen.blit(text, (280,570))
            text = font.render("LOYER  Avec 3 gares", 0, (0,0,0))
            fen.blit(text, (280,620))
            text = font.render("LOYER  Avec 4 gares", 0, (0,0,0))
            fen.blit(text, (280,670))
            for p in range(0,4):
                text = font.render(liste_prixpropriete[board.prix_propriete][0+1*p], 0, (0,0,0))
                fen.blit(text, (575,520+50*p))
            font2 = pygame.font.Font(police, 18)
            text = font2.render("Valeur Hypothécaire du terrain :", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,700))
            text = font2.render(str(liste_prixpropriete[22][4])+ " M", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,740))
        elif board.secteur == 9 and board.num_ville == 1:
            pygame.draw.rect(fen, (255,255,255), (250,100,400,700))
            pygame.draw.rect(fen, (0,0,0), (250,100,400,700),3)
            pygame.draw.rect(fen, (0,0,0), (265,115,370,670),3)
            fen.blit(Robinet, (285,120))
            c=[]
            b=liste_propriete[board.secteur][board.num_ville].split()
            while len(b)>=2:
                if len(b[0])+len(b[1])<10:
                    b[0]+=" "+b[1]
                    del b[1]
                else:
                    c.append(b[0])
                    del b[0]
            c.append(b[0])
            compteur = 0
            font = pygame.font.Font(police, 29)
            for ligne in c:
                text = font.render(ligne, 0, (0,0,0))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                fen.blit(text, (text_centre[0]-225,400+compteur*40))
                compteur+=1
            font = pygame.font.Font(police, 15)
            text = font.render("Si l'on possède UNE carte", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,490))
            text = font.render("de compagnie de service Public,", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,510))
            text = font.render("le loyer est 4 fois le montant", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,530))
            text = font.render("indiqué par les dés.", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,550))
            font = pygame.font.Font(police, 15)
            text = font.render("Si l'on possède les DEUX cartes", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,590))
            text = font.render("de compagnie de service Public,", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,610))
            text = font.render("le loyer est 10 fois le montant", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,630))
            text = font.render("indiqué par les dés.", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,650))
            font2 = pygame.font.Font(police, 18)
            text = font2.render("Valeur Hypothécaire du terrain :", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,680))
            text = font2.render(str(liste_prixpropriete[23][0])+ " M", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,720))
        elif board.secteur == 9 and board.num_ville == 0:
            pygame.draw.rect(fen, (255,255,255), (250,100,400,700))
            pygame.draw.rect(fen, (0,0,0), (250,100,400,700),3)
            pygame.draw.rect(fen, (0,0,0), (265,115,370,670),3)
            fen.blit(Ampoule2, (285,120))
            c=[]
            b=liste_propriete[board.secteur][board.num_ville].split()
            while len(b)>=2:
                if len(b[0])+len(b[1])<10:
                    b[0]+=" "+b[1]
                    del b[1]
                else:
                    c.append(b[0])
                    del b[0]
            c.append(b[0])
            compteur = 0
            font = pygame.font.Font(police, 29)
            for ligne in c:
                text = font.render(ligne, 0, (0,0,0))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                fen.blit(text, (text_centre[0]-225,400+compteur*40))
                compteur+=1
            font = pygame.font.Font(police, 15)
            text = font.render("Si l'on possède UNE carte", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,490))
            text = font.render("de compagnie de service Public,", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,510))
            text = font.render("le loyer est 4 fois le montant", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,530))
            text = font.render("indiqué par les dés.", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,550))
            font = pygame.font.Font(police, 15)
            text = font.render("Si l'on possède les DEUX cartes", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,590))
            text = font.render("de compagnie de service Public,", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,610))
            text = font.render("le loyer est 10 fois le montant", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,630))
            text = font.render("indiqué par les dés.", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,650))
            font2 = pygame.font.Font(police, 18)
            text = font2.render("Valeur Hypothécaire du terrain :", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,680))
            text = font2.render(str(liste_prixpropriete[23][0])+ " M", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,720))
        else:  
            pygame.draw.rect(fen, (255,255,255), (250,100,400,700))
            pygame.draw.rect(fen, (0,0,0), (250,100,400,700),3)
            pygame.draw.rect(fen, (0,0,0), (265,115,370,670),3)
            #Titre carte
            font = pygame.font.Font(police, 25)
            pygame.draw.rect(fen, couleurs[board.couleurs_ville], (275,125,350,125))
            pygame.draw.rect(fen, (0,0,0), (275,125,350,125),3)
            c=[]
            b=liste_propriete[board.secteur][board.num_ville].split()
            while len(b)>=2:
                if len(b[0])+len(b[1])<10:
                    b[0]+=" "+b[1]
                    del b[1]
                else:
                    c.append(b[0])
                    del b[0]
            c.append(b[0])
            compteur = 0
            font = pygame.font.Font(police, 29)
            for ligne in c:
                text = font.render(ligne, 0, (0,0,0))
                text_centre = text.get_rect()
                text_centre.center = fond_menu.get_rect().center
                if len(c) == 2:
                    y = 145+compteur*42
                else:
                    y = 135+compteur*32
                fen.blit(text, (text_centre[0]-225,y))
                compteur+=1
            font = pygame.font.Font(police, 25)
            font = pygame.font.Font(police, 20)
            text = font.render("M", 0, (0,0,0))
            fen.blit(text, (575,260))
            text = font.render("LOYER  Terrain nu", 0, (0,0,0))
            fen.blit(text, (280,290))
            text = font.render("LOYER  Avec 1 maison", 0, (0,0,0))
            fen.blit(text, (280,320))
            text = font.render("LOYER  Avec 2 maisons", 0, (0,0,0))
            fen.blit(text, (280,350))
            text = font.render("LOYER  Avec 3 maisons", 0, (0,0,0))
            fen.blit(text, (280,380))
            text = font.render("LOYER  Avec 4 maisons", 0, (0,0,0))
            fen.blit(text, (280,410))
            text = font.render("LOYER  Avec HÔTEL", 0, (0,0,0))
            fen.blit(text, (280,440))
            for p in range(0,6):
                text = font.render(liste_prixpropriete[board.prix_propriete][0+1*p], 0, (0,0,0))
                fen.blit(text, (575,290+30*p))
            pygame.draw.lines(fen, (0,0,0), False, [(270,480), (630,480)], 3)
            font = pygame.font.Font(police, 15)
            text = font.render("Si un joueur possède TOUS les", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,490))
            text = font.render("terrains d'un Groupe de Couleur", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,510))
            text = font.render("quelconque, le loyer des terrains nus", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,530))
            text = font.render("de ce groupe est doublé", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,550))
            pygame.draw.lines(fen, (0,0,0), False, [(270,575), (630,575)], 3)
            font = pygame.font.Font(police, 20)
            font2 = pygame.font.Font(police, 18)
            text = font.render("Prix des Maisons", 0, (0,0,0))
            fen.blit(text, (280,590))
            text = font.render("Prix d'un Hôtel", 0, (0,0,0))
            fen.blit(text, (280,630))
            text = font2.render("Valeur Hypothécaire du terrain :", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,680))
            for p in range(0,2):
                text = font.render(liste_prixpropriete[board.prix_propriete][6+1*p], 0, (0,0,0))
                fen.blit(text, (575,590+40*p))
            text = font2.render(str(liste_prixpropriete[board.prix_propriete][8])+ " M", 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]-225,720))



class BOARD:
    """ Classe permettant d'afficher le score board à droite en jeu.
        Méthodes : aff_board, aff_chat, aff_argent, aff_propriete, aff_historique """

    def __init__(self,jeu):
        self.argent = True
        self.historique = False
        self.propriete = False
        self.chat = False
        # Variables pour les proprietées
        self.sourlignage = False
        self.coord_sourlignage = [0,0]
        self.nb = 0
        self.secteur = -1
        self.position = jeu.position
        self.clic = jeu.clic
        self.ecrire = False
        self.touche = ""
        self.message = ""
        self.cursor = 0
        self.num_ville = 0
        self.couleurs_ville = 0
        self.prix_propriete = 0
        # Variables pour le chat
        self.liste_msg = []
        self.scroll = 0
        self.focus = True
        # Variables pour l'historique
        self.liste_msg_h = []
        self.scroll_h = 0
        self.focus_h = True
        self.notif = False

        

    def aff_board(self):
        """ Méthode permettant d'afficher et de gérer le scoreboard à droite
            de l'écran de jeu. """
        pygame.draw.rect(fen, (19,19,19), (900,0,450,900))
        pygame.draw.rect(fen, (0,0,0), (1235,872,30,30))
        pygame.draw.rect(fen, (70,142,201), (1235,872,30,30),3)
        fen.blit(chat, (1237.75, 874.5))
        pygame.draw.rect(fen, (0,0,0), (1264,872,30,30))
        pygame.draw.rect(fen, (70,142,201), (1264,872,30,30),3)
        fen.blit(dollar, (1270.5, 878))
        pygame.draw.rect(fen, (0,0,0), (1322,872,30,30))
        pygame.draw.rect(fen, (70,142,201), (1322,872,30,30),3)
        fen.blit(historique, (1326, 876))
        pygame.draw.rect(fen, (0,0,0), (1293,872,30,30))
        pygame.draw.rect(fen, (70,142,201), (1293,872,30,30),3)
        fen.blit(maison_menu, (1301, 879))
        if self.position[0] > 1264 and self.position[0] < 1294 and self.position[1] > 870 and self.position[1] < 900 and self.clic == 1:
            self.historique = False
            self.propriete = False
            self.chat = False
            self.argent = True
            self.secteur = -1
            self.sourlignage = False
        elif self.position[0] > 1326 and self.position[0] < 1350 and self.position[1] > 870 and self.position[1] < 900 and self.clic == 1:
            self.historique = True
            self.propriete = False
            self.chat = False
            self.argent = False
            self.secteur = -1
            self.sourlignage = False
        elif self.position[0] > 1295 and self.position[0] < 1325 and self.position[1] > 870 and self.position[1] < 900 and self.clic == 1:
            self.historique = False
            self.propriete = True
            self.chat = False
            self.argent = False
        elif self.position[0] > 1233 and self.position[0] < 1363 and self.position[1] > 870 and self.position[1] < 900 and self.clic == 1:
            self.historique = False
            self.propriete = False
            self.chat = True
            self.argent = False
            self.notif = False
            self.secteur = -1
            self.sourlignage = False
        if self.notif == True:
            pygame.draw.circle(fen, (237,27,26), (1238,875), 6, 0)
            police = "datas/font/verdana.ttf"
            font = pygame.font.Font(police, 9)
            text = font.render("1", 0, (255,255,255))
            fen.blit(text, (1234,868.5))


        
    def aff_argent(self,reseau,jeu):
        """ Méthode permettant d'afficher l'argent des joueur dans le scoreboard. """
        police = "datas/font/verdana.ttf"
        font = pygame.font.Font(police, 25)
        for x in range(0,len(reseau.liste_pseudo)):
            if x == jeu.nb_tour:
                color = (247,240,0)
            elif jeu.liste_loose[x] == True:
                color = (126.,126,126)
            else:
                color = (70,142,201)
            pygame.draw.rect(fen, (0,0,0), (975,75+160*x,300,100))
            pygame.draw.rect(fen, color, (975,75+160*x,300,100),3)
            pygame.draw.lines(fen, (255,255,255), False, [(977,125+160*x), (1272,125+160*x)], 3)
            text = font.render(reseau.liste_pseudo[x], 0, (255,255,255))
            fen.blit(text, (985,84+160*x))
            text = font.render("J"+str(x+1), 0, (255,255,255))
            fen.blit(text, (1235,84+160*x))
            
            text = font.render(str(jeu.liste_argent[x])+" M", 0, (255,255,255))
            fen.blit(text, (985,136+160*x))
            fen.blit(pion[x], (1232.5,130+160*x))



    def aff_propriete(self,jeu,reseau):
        """ """
        police = "datas/font/verdana.ttf"
        font = pygame.font.Font(police, 20)
        fen.blit(train, (1267,6))
        fen.blit(ampoule, (1312,6))
        #affichage des carrés des secteurs
        for i in range(0,8):
            pygame.draw.rect(fen, couleurs[0+i], (907+i*45,6,30,30))
        #définition des differentes variable de chaque secteur
        if self.position[0] > 907 and self.position[0] < 937 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(907,45), (937,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 907
                self.coord_sourlignage[1] = 937
                self.secteur = 0
                self.nb_ville = 2
                self.couleurs_ville = 0
                self.prix_propriete = 0
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 952 and self.position[0] < 982 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(952,45), (982,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 952
                self.coord_sourlignage[1] = 982
                self.secteur = 1
                self.nb_ville = 3
                self.couleurs_ville = 1
                self.prix_propriete = 2
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 997 and self.position[0] < 1027 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(997,45), (1027,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 997
                self.coord_sourlignage[1] = 1027
                self.secteur = 2
                self.nb_ville = 3
                self.couleurs_ville = 2
                self.prix_propriete = 5
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1042 and self.position[0] < 1072 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1042,45), (1072,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1042
                self.coord_sourlignage[1] = 1072
                self.secteur = 3
                self.nb_ville = 3
                self.couleurs_ville = 3
                self.prix_propriete = 8
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1087 and self.position[0] < 1117 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1087,45), (1117,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1087
                self.coord_sourlignage[1] = 1117
                self.secteur = 4
                self.nb_ville = 3
                self.couleurs_ville = 4
                self.prix_propriete = 11
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1132 and self.position[0] < 1162 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1132,45), (1162,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1132
                self.coord_sourlignage[1] = 1162
                self.secteur = 5
                self.nb_ville = 3
                self.couleurs_ville = 5
                self.prix_propriete = 14
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1177 and self.position[0] < 1207 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1177,45), (1207,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1177
                self.coord_sourlignage[1] = 1207
                self.secteur = 6
                self.nb_ville = 3
                self.couleurs_ville = 6
                self.prix_propriete = 17
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1222 and self.position[0] < 1252 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1222,45), (1252,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1222
                self.coord_sourlignage[1] = 1252
                self.secteur = 7
                self.nb_ville = 2
                self.couleurs_ville = 7
                self.prix_propriete = 20
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1267 and self.position[0] < 1297 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1267,45), (1297,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1267
                self.coord_sourlignage[1] = 1297
                self.secteur = 8
                self.nb_ville = 4
                self.couleurs_ville = 8
                self.prix_propriete = 22
                self.num_ville = 0
                self.sourlignage = True
        elif self.position[0] > 1312 and self.position[0] < 1342 and self.position[1] > 6 and self.position[1] < 36:
            pygame.draw.lines(fen, (255,0,0), False, [(1312,45), (1342,45)], 3)
            if self.clic == 1:
                self.coord_sourlignage[0] = 1312
                self.coord_sourlignage[1] = 1342
                self.secteur = 9
                self.nb_ville = 2
                self.couleurs_ville = 9
                self.prix_propriete = 26
                self.num_ville = 0
                self.sourlignage = True
        elif self.clic == 1 and (self.position[0] > 0 and self.position[0] < 900 and self.position[1] > 0 and self.position[1] < 900):
            self.secteur = -1
            self.sourlignage = False
        #définition des variable perméttant la création des cartes
        if self.sourlignage == True:
            pygame.draw.lines(fen, (255,0,0), False, [(self.coord_sourlignage[0],45), (self.coord_sourlignage[1],45)], 3)
            for c in range(0,self.nb_ville):
                    text = font.render(liste_propriete[self.secteur][0+c], 0,(255,255,255))
                    fen.blit(text, (960,100+c*80))
                    pygame.draw.rect(fen, couleurs[self.secteur], (915,98+c*80,30,30))
            #__________Premier Secteur__________
            if self.secteur == 0 and self.position[0] > 914 and self.position[0] < 1236 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 0
                    self.prix_propriete = 0
            elif self.secteur == 0 and self.position[0] > 914 and self.position[0] < 1104 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 0
                    self.prix_propriete = 1
            #__________Second Secteur__________
            if self.secteur == 1 and self.position[0] > 914 and self.position[0] < 1151 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 1
                    self.prix_propriete = 2
            elif self.secteur == 1 and self.position[0] > 914 and self.position[0] < 1163 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 1
                    self.prix_propriete = 3
            elif self.secteur == 1 and self.position[0] > 914 and self.position[0] < 1235 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 1
                    self.prix_propriete = 4
            #__________Troisième Secteur__________
            if self.secteur == 2 and self.position[0] > 914 and self.position[0] < 1247 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 2
                    self.prix_propriete = 5
            elif self.secteur == 2 and self.position[0] > 914 and self.position[0] < 1167 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 2
                    self.prix_propriete = 6
            elif self.secteur == 2 and self.position[0] > 914 and self.position[0] < 1129 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 2
                    self.prix_propriete = 7
            #__________Quatrième Secteur__________
            if self.secteur == 3 and self.position[0] > 914 and self.position[0] < 1150 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 3
                    self.prix_propriete = 8
            elif self.secteur == 3 and self.position[0] > 914 and self.position[0] < 1222 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 3
                    self.prix_propriete = 9
            elif self.secteur == 3 and self.position[0] > 914 and self.position[0] < 1116 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 3
                    self.prix_propriete = 10
            #__________Cinquième Secteur__________
            if self.secteur == 4 and self.position[0] > 914 and self.position[0] < 1140 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 4
                    self.prix_propriete = 11
            elif self.secteur == 4 and self.position[0] > 914 and self.position[0] < 1212 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 4
                    self.prix_propriete = 12
            elif self.secteur == 4 and self.position[0] > 914 and self.position[0] < 1188 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 4
                    self.prix_propriete = 13
            #__________Sixième Secteur__________
            if self.secteur == 5 and self.position[0] > 914 and self.position[0] < 1212 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 5
                    self.prix_propriete = 14
            elif self.secteur == 5 and self.position[0] > 914 and self.position[0] < 1176 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 5
                    self.prix_propriete = 15
            elif self.secteur == 5 and self.position[0] > 914 and self.position[0] < 1128 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 5
                    self.prix_propriete = 16
            #__________Septième Secteur__________
            if self.secteur == 6 and self.position[0] > 914 and self.position[0] < 1176 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 6
                    self.prix_propriete = 17
            elif self.secteur == 6 and self.position[0] > 914 and self.position[0] < 1092 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 6
                    self.prix_propriete = 18
            elif self.secteur == 6 and self.position[0] > 914 and self.position[0] < 1236 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 6
                    self.prix_propriete = 19
            #__________Huitième Secteur__________
            if self.secteur == 7 and self.position[0] > 914 and self.position[0] < 1260 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 7
                    self.prix_propriete = 20
            elif self.secteur == 7 and self.position[0] > 914 and self.position[0] < 1128 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 7
                    self.prix_propriete = 21
            #__________Gare Secteur__________
            if self.secteur == 8 and self.position[0] > 914 and self.position[0] < 1162 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 8
                    self.prix_propriete = 22
            elif self.secteur == 8 and self.position[0] > 914 and self.position[0] < 1104 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 8
                    self.prix_propriete = 22
            elif self.secteur == 8 and self.position[0] > 914 and self.position[0] < 1104 and self.position[1] > 258 and self.position[1] < 290:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
                if self.clic ==1:
                    self.num_ville = 2
                    self.secteur = 8
                    self.prix_propriete = 22
            elif self.secteur == 8 and self.position[0] > 914 and self.position[0] < 1164 and self.position[1] > 338 and self.position[1] < 368:
                pygame.draw.rect(fen, (19,19,19), (920,343,20,20))
                if self.clic ==1:
                    self.num_ville = 3
                    self.secteur = 8
                    self.prix_propriete = 22
            #__________Compagnie Secteur__________
            if self.secteur == 9 and self.position[0] > 914 and self.position[0] < 1234 and self.position[1] > 99 and self.position[1] < 131:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
                if self.clic ==1:
                    self.num_ville = 0
                    self.secteur = 9
                    self.prix_propriete = 23
            elif self.secteur == 9 and self.position[0] > 914 and self.position[0] < 1176 and self.position[1] > 179 and self.position[1] < 207:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
                if self.clic ==1:
                    self.num_ville = 1
                    self.secteur = 9
                    self.prix_propriete = 23
            # Affichage le propriétaire de chaque ville par secteur
            font = pygame.font.Font("datas/font/verdanai.ttf", 16)
            compteur = 0
            for nom_ville in liste_propriete[self.secteur]:
                for i in range(0,28):
                    if nom_ville  == liste_nom_ville[i]:
                        case = case_achetable[i]
                        if  jeu.pv[case][1] == []:
                            text = font.render("Propriété libre", 0, (150,150,150))
                            fen.blit(text, (960,130+compteur*80))
                        else:
                            if case not in jeu.liste_hypotheque:
                                text1 = font.render("Acheter par " + str(reseau.liste_pseudo[jeu.pv[case][1]]), 0, (150,150,150))
                            else:
                                text1 = font.render("Hypothéquer par " + str(reseau.liste_pseudo[jeu.pv[case][1]]), 0, (150,150,150))
                            fen.blit(text1, (960,130+compteur*80))
                        break
                compteur += 1
            # Affiche petit carré en continu
            if self.num_ville == 0:
                pygame.draw.rect(fen, (19,19,19), (920,103,20,20))
            elif self.num_ville == 1:
                pygame.draw.rect(fen, (19,19,19), (920,183,20,20))
            elif self.num_ville == 2:
                pygame.draw.rect(fen, (19,19,19), (920,263,20,20))
            elif self.num_ville == 3:
                pygame.draw.rect(fen, (19,19,19), (920,343,20,20))



    def aff_complement_propriete(self,jeu,reseau,menu,envoyer,board):
        font = pygame.font.Font("datas/font/unispace_rg.ttf", 20)
        # Bouton pour acheter une ville
        pygame.draw.rect(fen, (0,0,0), (950.5,800,350,45))
        for i in range(0,28):
            if jeu.localisation == case_achetable[i]:
                cout = liste_cout_propriete[i]
                break
        if jeu.localisation in case_achetable and jeu.pv[jeu.localisation][1] == [] and jeu.mon_tour == True and jeu.deplacement == False and jeu.liste_argent[jeu.nb_tour] - cout >= 0 and jeu.new_case_ach == True:
            if self.position[0] > 950 and self.position[0] < 1300 and self.position[1] > 800 and self.position[1] < 845:
                color = (237,27,26)
                if self.clic == 1:
                    jeu.liste_argent[jeu.nb_tour] -= cout
                    envoyer(reseau, menu, " $liste_argent$ ", jeu.liste_argent)
                    jeu.pv[jeu.localisation][1] = jeu.nb_tour
                    case_envoie = [jeu.localisation, "p", jeu.pv[jeu.localisation][0], "j", jeu.pv[jeu.localisation][1], "m", jeu.pv[jeu.localisation][2]]
                    envoyer(reseau, menu, " $case$ ", case_envoie)
                    liste_num_ville = case_simple + case_gare + case_compagnie
                    for num_ville in range(0,28):
                        if case_achetable[num_ville] == jeu.localisation:
                            message_h = str(menu.pseudo) + " vient d'acheter " + str(liste_nom_ville[num_ville]) + "."
                            break
                    envoyer(reseau, menu, " $historique$ ", message_h)
                    if menu.type_joueur == "hébergeur":
                        board.liste_msg_h.append(message_h)
            else:
                color = (255,255,255)
        else:
            color = (126,126,126)
        pygame.draw.rect(fen, color, (950.5,800,350,45), 2)
        text = font.render("Acheter la propriété", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-450+900,810))
        # Bouton pour hypothéquer la ville selectionner dans le board
        pygame.draw.rect(fen, (0,0,0), (950.5,730,350,45))
        # On vérifie la possibilité de l'hypothèque
        verite = False
        compteur = 0
        msg_add = ""
        while reseau.liste_pseudo[compteur] != menu.pseudo:
            compteur +=1
        if self.secteur != -1 and (jeu.mon_tour == True or jeu.doit_payer[compteur] == True):
            nom_ville = liste_propriete[self.secteur][self.num_ville]
            for i in range(0,28):
                if nom_ville  == liste_nom_ville[i]:
                    case = case_achetable[i]
                    # Si on peut hypothéquer
                    if jeu.pv[case][1] == compteur and case not in jeu.liste_hypotheque and jeu.pv[case][2] == 0:
                        if case in case_compagnie:
                            valeur_hypo = int(liste_prixpropriete[23][-1])
                        elif case in case_gare:
                            valeur_hypo = int(liste_prixpropriete[22][-1])
                        else:
                            compteur2 = 0
                            while case != case_simple[compteur2]:
                                compteur2 += 1
                            valeur_hypo = int(liste_prixpropriete[compteur2][-1])
                        verite = True
                    break
        if verite:
            msg_add = " : " + str(valeur_hypo) + "M"
            if self.position[0] > 950 and self.position[0] < 1300 and self.position[1] > 730 and self.position[1] < 775:
                color = (237,27,26)
                if self.clic == 1:
                    message_h = str(menu.pseudo) + " vient d'hypothéquer " + liste_propriete[self.secteur][self.num_ville] + " pour " + str(valeur_hypo) + "M."
                    envoyer(reseau, menu, " $historique$ ", message_h)
                    if menu.type_joueur == "hébergeur":
                        board.liste_msg_h.append(message_h)
                    jeu.liste_argent[compteur] += valeur_hypo
                    envoyer(reseau, menu, " $liste_argent$ ", jeu.liste_argent)
                    jeu.liste_hypotheque.append(case)
                    envoyer(reseau,menu," $liste_hypotheque$ ", jeu.liste_hypotheque)
            else:
                color = (255,255,255)
        else:
            color = (126,126,126)
        pygame.draw.rect(fen, color, (950.5,730,350,45), 2)
        text = font.render("Hypothéquer" + msg_add, 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-450+900,740))
        # Bouton pour racheter une hypothèque
        pygame.draw.rect(fen, (0,0,0), (950.5,660,350,45))
        # On vérifie la possibilité du rachat de l'hypothèque
        verite = False
        if self.secteur != -1 and jeu.mon_tour == True:
            compteur = 0
            while reseau.liste_pseudo[compteur] != menu.pseudo:
                compteur +=1
            nom_ville = liste_propriete[self.secteur][self.num_ville]
            for i in range(0,28):
                if nom_ville  == liste_nom_ville[i]:
                    case = case_achetable[i]
                    # Si on peut racheter
                    if jeu.pv[case][1] == compteur and case in jeu.liste_hypotheque:
                        if case in case_compagnie:
                            cout = int(int(liste_prixpropriete[23][-1])*1.1)
                        elif case in case_gare:
                            cout = int(int(liste_prixpropriete[22][-1])*1.1)
                        else:
                            compteur2 = 0
                            while case != case_simple[compteur2]:
                                compteur2 += 1
                            cout = int(int(liste_prixpropriete[compteur2][-1])*1.1)
                        if jeu.liste_argent[compteur] - cout >= 0:
                            verite = True
                    break
        if verite:
            if self.position[0] > 950 and self.position[0] < 1300 and self.position[1] > 660 and self.position[1] < 705:
                color = (237,27,26)
                if self.clic == 1:
                    message_h = str(menu.pseudo) + " vient de racheter " + liste_propriete[self.secteur][self.num_ville] + " pour " + str(cout) + "M."
                    envoyer(reseau, menu, " $historique$ ", message_h)
                    if menu.type_joueur == "hébergeur":
                        board.liste_msg_h.append(message_h)
                    jeu.liste_argent[compteur] -= cout
                    envoyer(reseau, menu, " $liste_argent$ ", jeu.liste_argent)
                    compteur = 0
                    while jeu.liste_hypotheque[compteur] != case:
                        compteur += 1
                    del jeu.liste_hypotheque[compteur]
                    envoyer(reseau,menu," $liste_hypotheque$ ", jeu.liste_hypotheque)
            else:
                color = (255,255,255)
        else:
            color = (126,126,126)
        pygame.draw.rect(fen, color, (950.5,660,350,45), 2)
        text = font.render("Lever l'hypothèque", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-450+900,670))
        # Bouton pour vendre un bâtiment
        pygame.draw.rect(fen, (0,0,0), (950.5,590,350,45))
        # On vérifie la possibilité de vendre un bâtiment
        verite = False
        compteur = 0
        msg_add = ""
        while reseau.liste_pseudo[compteur] != menu.pseudo:
            compteur +=1
        if self.secteur != -1 and (jeu.mon_tour == True or jeu.doit_payer[compteur] == True):
            nom_ville = liste_propriete[self.secteur][self.num_ville]
            for i in range(0,28):
                if nom_ville  == liste_nom_ville[i]:
                    case = case_achetable[i]
                    # Si on peut vendre un bâtiment
                    if jeu.pv[case][1] == compteur and jeu.pv[case][2] > 0 and case in case_simple:
                        verite = True
                    break
        if verite:
            compteur2 = 0
            while case != case_simple[compteur2]:
                compteur2 += 1
            vente_bat = int(liste_prixpropriete[compteur2][-2])
            msg_add = " : " + str(vente_bat) + "M"
            if self.position[0] > 950 and self.position[0] < 1300 and self.position[1] > 590 and self.position[1] < 635:
                color = (237,27,26)
                if self.clic == 1:
                    message_h = str(menu.pseudo) + " vient de vendre un bâtiment sur " + liste_propriete[self.secteur][self.num_ville] + " pour " + str(vente_bat) + "M."
                    envoyer(reseau, menu, " $historique$ ", message_h)
                    if menu.type_joueur == "hébergeur":
                        board.liste_msg_h.append(message_h)
                    jeu.liste_argent[compteur] += vente_bat
                    envoyer(reseau, menu, " $liste_argent$ ", jeu.liste_argent)
                    jeu.pv[case][2] -= 1
                    case_envoie = [case, "p", jeu.pv[case][0], "j", jeu.pv[case][1], "m", jeu.pv[case][2]]
                    envoyer(reseau, menu, " $case$ ", case_envoie)
            else:
                color = (255,255,255)
        else:
            color = (126,126,126)
        pygame.draw.rect(fen, color, (950.5,590,350,45), 2)
        text = font.render("Vendre un bâtiment" + msg_add, 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-450+900,600))
        # Bouton pour acheter un bâtiment
        pygame.draw.rect(fen, (0,0,0), (950.5,520,350,45))
        # On vérifie la possibilité d'acheter un bâtiment
        verite = False
        if self.secteur != -1 and jeu.mon_tour == True:
            compteur = 0
            while reseau.liste_pseudo[compteur] != menu.pseudo:
                compteur +=1
            nom_ville = liste_propriete[self.secteur][self.num_ville]
            for i in range(0,28):
                if nom_ville  == liste_nom_ville[i]:
                    case = case_achetable[i]
                    # Si on peut acheter un bâtiment
                    if jeu.pv[case][1] == compteur and jeu.pv[case][2] < 5 and case in case_simple:
                        if jeu.pv[case][2] == 4:
                            compteur2 = 0
                            while case not in liste_secteur[compteur2]:
                                compteur2 += 1
                            total_proprio = 0
                            for case2 in liste_secteur[compteur2]:
                                if jeu.pv[case2][1] == jeu.pv[case][1]:
                                    total_proprio += 1
                            if total_proprio == len(liste_secteur[compteur2]):
                                compteur2 = 0
                                while case != case_simple[compteur2]:
                                    compteur2 += 1
                                cout = int(liste_prixpropriete[compteur2][-2])
                                if jeu.liste_argent[compteur] - cout >= 0:
                                    verite = True
                        else:
                            verite = True
                    break
        if verite:
            if self.position[0] > 950 and self.position[0] < 1300 and self.position[1] > 520 and self.position[1] < 565:
                color = (237,27,26)
                if self.clic == 1:
                    message_h = str(menu.pseudo) + " vient d'acheter un bâtiment sur " + liste_propriete[self.secteur][self.num_ville] + " pour " + str(cout) + "M."
                    envoyer(reseau, menu, " $historique$ ", message_h)
                    if menu.type_joueur == "hébergeur":
                        board.liste_msg_h.append(message_h)
                    jeu.liste_argent[compteur] -= cout
                    envoyer(reseau, menu, " $liste_argent$ ", jeu.liste_argent)
                    jeu.pv[case][2] += 1
                    case_envoie = [case, "p", jeu.pv[case][0], "j", jeu.pv[case][1], "m", jeu.pv[case][2]]
                    envoyer(reseau, menu, " $case$ ", case_envoie)
            else:
                color = (255,255,255)
        else:
            color = (126,126,126)
        pygame.draw.rect(fen, color, (950.5,520,350,45), 2)
        text = font.render("Acheter un bâtiment", 0, color)
        text_centre = text.get_rect()
        text_centre.center = fond_menu.get_rect().center
        fen.blit(text, (text_centre[0]-450+900,530))



    def aff_historique(self):
        font = pygame.font.Font("datas/font/times.ttf",18)
        # Prépare l'affichage des messages envoyés
        liste_ligne = [""]
        compteur_g = 0
        for msg in self.liste_msg_h:
            msg = list(msg)
            compteur = 0
            if len(msg) > 1:
                while compteur != len(msg)-1:
                    if msg[compteur] != " " and msg[compteur+1] != " ":
                        msg[compteur] += msg[compteur+1]
                        del msg[compteur+1]
                    else:
                        compteur += 1
            phrase = msg
            for mot in phrase:
                test1 = font.render(liste_ligne[compteur_g], 0, (0,0,0))
                test1 = test1.get_rect()
                test1 = test1[2]
                test2 = font.render(mot, 0, (0,0,0))
                test2 = test2.get_rect()
                test2 = test2[2]
                if test2 > 400:
                    mot_decoupe = list(mot)
                    for cara in mot_decoupe:
                        test1 = font.render(liste_ligne[compteur_g], 0, (0,0,0))
                        test1 = test1.get_rect()
                        test1 = test1[2]
                        test3 = font.render(cara, 0, (0,0,0))
                        test3 = test3.get_rect()
                        test3 = test3[2]
                        if test1 + test3 > 400:
                            compteur_g += 1
                            liste_ligne.append(cara)
                        else:
                            liste_ligne[compteur_g] += cara
                elif test1 + test2 > 400:
                    compteur_g += 1
                    liste_ligne.append(mot)
                else:
                    liste_ligne[compteur_g] += mot
            compteur_g += 2
            liste_ligne.append("")
            liste_ligne.append("")
        del liste_ligne[-2:len(liste_ligne)]
        # Sélectionne les lignes à afficher en fonction du scroll de la souris
        if len(liste_ligne) > 40:
            aff_liste_ligne = []
            for i in range(self.scroll_h, self.scroll_h+37):
                aff_liste_ligne.append(liste_ligne[i])
        else:
            aff_liste_ligne = liste_ligne
        # Affiche les messages envoyés
        compteur = 0
        for ligne_aff in aff_liste_ligne:
            text = font.render(ligne_aff, 0, (255,255,255))
            fen.blit(text, (925,25+20*compteur))
            compteur += 1
        # Gère le scroll de la souris
        if self.position[0] > 900 and self.position[0] < 1350 and self.position[1] < 900 and self.position[1] > 0:
            if self.clic == 4 and self.scroll_h > 0:
                self.scroll_h -= 1
                self.focus_h = False
            elif self.clic == 5:
                if self.scroll_h < len(liste_ligne)-40:
                    self.scroll_h += 1
                else:
                    self.focus_h = True
        # Gestion du scroll automatique
        if len(liste_ligne)-40-self.scroll_h > 0 and self.focus_h == True:
            self.scroll_h = len(liste_ligne)-37



    def aff_chat(self,menu,envoyer,reseau):
        # Créer le texte
        font = pygame.font.Font("datas/font/times.ttf",18)
        msg_def = self.message[0:self.cursor]+"|"+self.message[self.cursor:len(self.message)+1]
        if self.ecrire == True:
            text = font.render(msg_def, 0, (0,0,0))
            phrase = list(msg_def)
        else:
            text = font.render(self.message, 0, (0,0,0))
            phrase = list(self.message)
        text_centre = text.get_rect()
        longueur_txt = text_centre[2]
        # Gestion de la zone de texte
        if self.ecrire == True:
            color = (237,27,26)
            if longueur_txt < 4440 and self.touche in """ \"&²~#'{([|`ç^@$)]=}°£¤€!µ:;.?,§%<>_-*/+âêîôäëïüöÿazertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBNéèàêâïîùû0123456789 """ and self.touche != "":
                self.message = list(self.message)
                self.message.append("")
                for i in range(0,len(self.message)-self.cursor-1):
                    self.message[-(i+1)] = self.message[-(i+2)]
                self.message[self.cursor] = self.touche
                self.message = "".join(self.message)
                self.cursor += 1                    
            elif self.cursor>0 and self.touche == "\b":
                self.message = list(self.message)
                del self.message[self.cursor-1]
                self.message = "".join(self.message)
                self.cursor -= 1
            elif self.cursor < len(self.message) and self.touche == "\suppr":
                self.message = list(self.message)
                del self.message[self.cursor]
                self.message = "".join(self.message)
            elif self.cursor > 0 and self.touche == "\left":
                self.cursor -= 1
            elif self.cursor < len(self.message) and self.touche == "\right":
                self.cursor += 1
            elif self.touche == "\echap":
                self.message = ""
                self.cursor = 0
            elif self.touche == "\return" and self.message != "" and len(self.message) != self.message.count(" "):
                envoyer(reseau, menu, " $message$ ", str(menu.pseudo) + " : "+ str(self.message))
                if menu.type_joueur == "hébergeur":
                    self.liste_msg.append(str(menu.pseudo) + " : "+ str(self.message))
                self.message = ""
                self.cursor = 0
                self.focus = True
        else:
            color = (126.,126,126)
        # Préparation à l'affichage
        self.touche = ""
        ligne = [""]
        compteur = 0
        if len(phrase) > 1:
            while compteur != len(phrase)-1:
                if phrase[compteur] != " " and phrase[compteur+1] != " ":
                    phrase[compteur] += phrase[compteur+1]
                    del phrase[compteur+1]
                else:
                    compteur += 1
        compteur = 0
        for mot in phrase:
            test1 = font.render(ligne[compteur], 0, (0,0,0))
            test1 = test1.get_rect()
            test1 = test1[2]
            test2 = font.render(mot, 0, (0,0,0))
            test2 = test2.get_rect()
            test2 = test2[2]
            if test2 > 350:
                mot_decoupe = list(mot)
                for cara in mot_decoupe:
                    test1 = font.render(ligne[compteur], 0, (0,0,0))
                    test1 = test1.get_rect()
                    test1 = test1[2]
                    test3 = font.render(cara, 0, (0,0,0))
                    test3 = test3.get_rect()
                    test3 = test3[2]
                    if test1 + test3 > 350:
                        compteur += 1
                        ligne.append(cara)
                    else:
                        ligne[compteur] += cara
            elif test1 + test2 > 350:
                compteur += 1
                ligne.append(mot)
            else:
                ligne[compteur] += mot
        nb_ligne = len(ligne)-1
        # Prépare l'affichage des messages envoyés
        self.liste_ligne = [""]
        compteur_g = 0
        for msg in self.liste_msg:
            msg = list(msg)
            compteur = 0
            if len(msg) > 1:
                while compteur != len(msg)-1:
                    if msg[compteur] != " " and msg[compteur+1] != " ":
                        msg[compteur] += msg[compteur+1]
                        del msg[compteur+1]
                    else:
                        compteur += 1
            phrase = msg
            for mot in phrase:
                test1 = font.render(self.liste_ligne[compteur_g], 0, (0,0,0))
                test1 = test1.get_rect()
                test1 = test1[2]
                test2 = font.render(mot, 0, (0,0,0))
                test2 = test2.get_rect()
                test2 = test2[2]
                if test2 > 400:
                    mot_decoupe = list(mot)
                    for cara in mot_decoupe:
                        test1 = font.render(self.liste_ligne[compteur_g], 0, (0,0,0))
                        test1 = test1.get_rect()
                        test1 = test1[2]
                        test3 = font.render(cara, 0, (0,0,0))
                        test3 = test3.get_rect()
                        test3 = test3[2]
                        if test1 + test3 > 400:
                            compteur_g += 1
                            self.liste_ligne.append(cara)
                        else:
                            self.liste_ligne[compteur_g] += cara
                elif test1 + test2 > 400:
                    compteur_g += 1
                    self.liste_ligne.append(mot)
                else:
                    self.liste_ligne[compteur_g] += mot
            compteur_g += 2
            self.liste_ligne.append("")
            self.liste_ligne.append("")
        del self.liste_ligne[-2:len(self.liste_ligne)]
        # Sélectionne les lignes à afficher en fonction du scroll de la souris
        if len(self.liste_ligne) > 37:
            aff_liste_ligne = []
            for i in range(self.scroll, self.scroll+37):
                aff_liste_ligne.append(self.liste_ligne[i])
        else:
            aff_liste_ligne = self.liste_ligne
        # Affiche les messages envoyés
        compteur = 0
        for ligne_aff in aff_liste_ligne:
            text = font.render(ligne_aff, 0, (255,255,255))
            fen.blit(text, (925,25+20*compteur))
            compteur += 1
        # Gère le scroll de la souris
        if self.position[0] > 900 and self.position[0] < 1350 and self.position[1] < 800-30*nb_ligne and self.position[1] > 0:
            if self.clic == 4 and self.scroll > 0:
                self.scroll -= 1
                self.focus = False
            elif self.clic == 5:
                if self.scroll < len(self.liste_ligne)-37:
                    self.scroll += 1
                else:
                    self.focus = True
        # Rectangle cache fond
        pygame.draw.rect(fen, (19,19,19), (900,778-30*nb_ligne,450,74+30*nb_ligne))
        # Tracer des lignes
        pygame.draw.circle(fen, color, (950,815-30*nb_ligne), 17)
        pygame.draw.circle(fen, color, (1301,815-30*nb_ligne), 17)
        pygame.draw.circle(fen, color, (950,815), 17)
        pygame.draw.circle(fen, color, (1301,815), 17)
        pygame.draw.rect(fen, color, (950,798-30*nb_ligne,350,34+30*nb_ligne))
        pygame.draw.rect(fen, color, (933,813-30*nb_ligne,385,30*nb_ligne))
        # Tracer des formes
        pygame.draw.circle(fen, (255,255,255), (950,815), 15)
        pygame.draw.circle(fen, (255,255,255), (1300,815), 15)
        pygame.draw.circle(fen, (255,255,255), (950,815-30*nb_ligne), 15)
        pygame.draw.circle(fen, (255,255,255), (1300,815-30*nb_ligne), 15)
        pygame.draw.rect(fen, (255,255,255), (950,800-30*nb_ligne,350,30+30*nb_ligne))
        pygame.draw.rect(fen, (255,255,255), (935,813-30*nb_ligne,380,30*nb_ligne))
        for i in range(0,len(ligne)):
            text = font.render(ligne[-(i+1)], 0, (0,0,0))
            text_centre = text.get_rect()
            text_centre.center = fond_menu.get_rect().center
            fen.blit(text, (text_centre[0]+450,805-30*i))
        # Gestion de la création d'un message dans la zone de texte
        if self.clic == 1:
            if self.position[0] > 935 and self.position[0] < 1315 and self.position[1] > 800-30*nb_ligne and self.position[1] < 830:
                self.ecrire = True
            else:
                self.ecrire = False
        if len(self.liste_ligne)-37-self.scroll > 0 and self.focus == True:
            self.scroll = len(self.liste_ligne)-37

