# -*-coding: utf-8 -*

import pygame
from pygame.locals import *
import os
pygame.init()


# Récupération des données de l'écran
info = pygame.display.Info()
milieuX = int(info.current_w/2-1350/2)
position = str(milieuX) + ",26"
os.environ['SDL_VIDEO_WINDOW_POS'] = position


# Créeation et configuration de la fenêtre de jeu
fen = pygame.display.set_mode((1350,900))
icone = pygame.image.load("ressources/icone.jpg")
pygame.display.set_icon(icone)
pygame.display.set_caption("Monopoly")


# Importation des images
fond_menu = pygame.image.load("ressources/Fond_Menu.jpg").convert()
fond_plateau = pygame.image.load("ressources/Plateau.jpg").convert()
dollar = pygame.image.load("ressources/dollar.png").convert_alpha()
maison_menu = pygame.image.load("ressources/i_maison.png").convert_alpha()
historique = pygame.image.load("ressources/historique.png").convert_alpha()
chat = pygame.image.load("ressources/chat.png").convert_alpha()
train = pygame.image.load("ressources/train.png").convert()
train2 = pygame.image.load("ressources/train2.png").convert_alpha()
ampoule = pygame.image.load("ressources/ampoule.png").convert()
Robinet = pygame.image.load("ressources/Robinet.jpg").convert_alpha()
Ampoule2 = pygame.image.load("ressources/Ampoule2.jpg").convert_alpha()
de = []
for i in range(0,6):
    de.append(pygame.image.load("ressources/de"+str(i+1)+".png").convert_alpha())
pion = []
for i in range(0,5):
    pion.append(pygame.image.load("ressources/p"+str(i+1)+".png").convert_alpha())
maison = pygame.image.load("ressources/maison.png").convert_alpha()
hotel = pygame.image.load("ressources/hotel.png").convert_alpha()


# Importations des fonts
font1 = pygame.font.Font("datas/font/unispace_rg.ttf", 25)


# Listes regroupant les propiétés / cartes chances / caisse de communotées
texte_chance = ["Avancez jusqu'à la case départ.","Votre immeuble et votre prêt rapportent. Vous devez toucher 150M.","Rendez-vous à l'avenue Henri-Martin. Si vous passez par la case départ recevez 200M.",
                "La Banque vous verse un dividende de 50M.","Avancez au Boulevard de la Villette. Si vous passez par la case départ recevez 200M.","Reculez de trois cases.","Payez pour frais de scolarité 150M.",
                "Vous êtes imposé pour réparations de voirie à raison de : 40M par maison et 115M par hôtel.","Amende pour excès de vitesse : 15M.","Allez à la gare de Lyon. Si vous passez par la case départ recevez 200€M.",
                "Rendez-vous à la Rue de la Paix.","Vous avez gagnez le prix des mots croisés. Recevez 100M.","Avancez tout droit en prison. Ne passez pas par la case départ. Ne recevez pas 200M.","Faites des réparations dans toutes vos maisons. Versez pour chaque maison 25M et pour chaque hôtel 100M.",
                "Amende pour ivresse: 20M.","Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue."]
texte_caissedecommu = ["Payez à l'Hôpital 100M.","Recevez votre intérêt sur l'emprunt à 7%. 25M.","C'est  votre anniversaire : chaque joueur doit vous donner 10M.","Les Contributions vous remboursent la somme de 20M.",
                       "Erreur de la Banque en votre faveur. Recevez 200M.","Payez la note du Médecin 50M.","Vous héritez 100M.","Payez votre Police d'Assurance s'élevant à 50M.","Recevez votre revenu annuel 100M.",
                       "Retournez à Belleville.","Avancez jusqu'à la case départ.","Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.","Allez en prison. Avancez tout droit en prison. Ne passez pas par la case départ. Ne recevez pas 200M.",
                       "Payez une amende de 10M ou bien tirez une carte 'CHANCE'.","Vous avez gagné le deuxième Prix de Beauté. Recevez 10M.","La vente de votre stock vous rapporte 50M."]
liste_propriete = [["Boulevard de Belleville","Rue Lecourbe"],
                   ["Rue de Vaugirard","Rue de Courcelles","Avenue de la République"],
                   ["Boulevard de la Villette","Avenue de Neuilly","Rue de Paradis"],
                   ["Avenue de Mozart","Boulevard Saint-Michel","Place Pigalle"],
                   ["Avenue Matignon","Boulevard Malesherbes","Avenue Henri-Martin"],
                   ["Faubourg Saint-Honoré","Place de la Bourse","Rue la Fayette"],
                   ["Avenue de Breteuil","Avenue Foch","Boulevard des Capucines"],
                   ["Avenue des Champs-Elysées","Rue de la Paix"],
                   ["Gare Montparnasse","Gare de Lyon","Gare du Nord","Gare Saint-Lazare"],
                   ["Compagnie d'Électricité","Compagnie des Eaux"]]
liste_prixpropriete = [["2","10","30","90","160","250","50","50","30"],
                       ["4","20","60","180","320","450","50","50","30"],
                       ["6","30","90","270","400","550","50","50","50"],
                       ["6","30","90","270","400","550","50","50","50"],
                       ["8","40","100","300","450","600","50","50","60"],
                       ["10","50","150","450","625","750","100","100","70"],
                       ["10","50","150","450","625","750","100","100","70"],
                       ["12","60","180","500","700","900","100","100","80"],
                       ["14","70","200","550","750","950","100","100","90"],
                       ["14","70","200","550","750","950","100","100","90"],
                       ["16","80","220","600","800","1000","100","100","100"],
                       ["18","90","250","700","875","1050","150","150","110"],
                       ["18","90","250","700","875","1050","150","150","110"],
                       ["20","100","300","750","925","1100","150","150","120"],
                       ["22","110","330","800","975","1150","150","150","130"],
                       ["22","110","330","800","975","1150","150","150","130"],
                       ["24","120","360","850","1025","1200","150","150","140"],
                       ["26","130","390","900","1100","1275","200","200","150"],
                       ["26","130","390","900","1100","1275","200","200","150"],
                       ["28","150","450","1000","1200","1400","200","200","160"],
                       ["35","175","500","1100","1300","1500","200","200","175"],
                       ["50","200","600","1400","1700","2000","200","200","200"],
                       ["25","50","100","200","100"],
                       ["75"]]
liste_nom_ville = ["Boulevard de Belleville","Rue Lecourbe","Gare Montparnasse",
                   "Rue de Vaugirard","Rue de Courcelles","Avenue de la République",
                   "Boulevard de la Villette","Compagnie d'Électricité","Avenue de Neuilly","Rue de Paradis",
                   "Gare de Lyon","Avenue de Mozart","Boulevard Saint-Michel","Place Pigalle",
                   "Avenue Matignon","Boulevard Malesherbes","Avenue Henri-Martin",
                   "Gare du Nord","Faubourg Saint-Honoré","Place de la Bourse","Compagnie des Eaux","Rue la Fayette",
                   "Avenue de Breteuil","Avenue Foch","Boulevard des Capucines",
                   "Gare Saint-Lazare","Avenue des Champs-Elysées","Rue de la Paix"]
case_achetable = [1,3,5,6,8,9,11,12,13,14,15,16,18,19,21,23,24,25,26,27,28,29,31,32,34,35,37,39]
case_simple = [1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39]
liste_cout_propriete = [60,60,200,100,100,120,140,150,140,160,200,180,180,200,220,220,240,200,260,260,150,280,300,300,320,200,350,400]
case_gare = [5,15,25,35]
case_compagnie = [12,28]
liste_secteur = [[1,3],[6,8,9],[11,13,14],[16,18,19],[21,23,24],[26,27,29],[31,32,34],[37,39]]


# Pannel de couleurs utiles
couleurs = [(147, 72, 36),(187, 228, 248),(218, 45, 135),(246, 144, 2),(226, 1, 17),(254, 237, 1),(31, 166, 72),(4, 102, 180),(255, 255, 255),(255, 255, 255)]

