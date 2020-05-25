# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args
import csv


def charger_csv_dict(nom_fic):
    """Fonction qui permet d'importer les données du fichier csv sous forme de liste de dictionnaires """
    liste = []  # resultat de la fonction
    # ouverture du fichier CSV
    with open(nom_fic,  # nom du fichier
              "r",  # ouverture en lecture
              newline="",  # évite les problèmes de codage du retour à la ligne
              encoding="utf-8-sig",  # permet de forcer la lecture en utf -8 (sig pour "UTF-8 codec with BOM signature")
              ) as csvfile:  # cvsfile est le fichier que l'on vient d'ouvrir
        # création du lecteur csv indiquant le caractère séparateur
        csv_reader = csv.reader(csvfile,    
                                delimiter=",",
                                quotechar="'",
                                quoting=csv.QUOTE_MINIMAL)
        # permet de sauter la ligne d'entête si pas besoin
        csv_reader.__next__()
        for enreg in csv_reader:  # boucle de parcours des enregistrements
            # enreg est une liste de str contenant chaque champ de l ' enregistrement
            # ajout du score dans la liste
            liste.append(
            {
                'Année' : enreg[0],
                'Athlète' : enreg[1],
                'Position' : enreg[2],
                'Age' : enreg[3],
                'Equipe' : enreg[4],
                'Matchs joués' : enreg[5],
                '%3Points' : enreg[6],
                '%2Points' : enreg[7],
                'Passes' : enreg[8],
                'Points' : enreg[9],
            }
            )
    return liste

saisons_NBA = charger_csv_dict('NBA_saisons.csv')

def nom_joueur_max_passes(annee):
    """
    Fonction qui en paramètre prend une année (int)
    et la liste des joueurs sous forme de liste de dictionnaires
    et qui retourne le nombre de joueurs ayant joués l'année donnée
    """
    max = 0
    nom = ''
    for enreg in saisons_NBA :
        if int(enreg['Passes']) > max and int(enreg['Année']) == annee:            
            max = int(enreg['Passes'])
            nom = str(enreg['Athlète'])
    return nom
                                                               

inputs_nom_joueur_max_passes = [Args(1953),Args(1960),Args(1970),Args(1980),Args(1990),Args(2000),Args(2010),Args(2017)]

exo_nom_joueur_max_passes = ExerciseFunction(
    nom_joueur_max_passes,
    inputs_nom_joueur_max_passes,
    layout='pprint',
    layout_args=(40, 25, 25),
)
