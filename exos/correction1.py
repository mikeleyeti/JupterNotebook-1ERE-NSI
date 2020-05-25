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


def liste_doublons(liste):
    """
    fonction qui prend comme entrée une liste
    et qui renvoie la liste des doublons.
    Cette liste sera vide si il n'y a aucun doublons.
    """
    doublons = []
    for i in range(len(liste)) :
        # Permet d'exclure les doublons déjà trouvés
        if liste[i] not in doublons:
            # On cherche des doublons après l'élément sélectionné
            for j in range(i+1,len(liste)):
                # On ajoute le doublons si celui-ci existe.
                if liste[i] == liste[j]:
                    doublons.append(liste[i])
    return doublons


def nombre_joueurs_annee(annee,liste):
    """
    Fonction qui en paramètre prend une année (int)
    et la liste des joueurs sous forme de liste de dictionnaires
    et qui retourne le nombre de joueurs ayant joués l'année donnée
    """
    compteur = 0
    for enreg in liste :
        if int(enreg['Année']) == annee:            
            compteur += 1
    return compteur

inputs_liste_doublons = [Args([1,1,2,3,4]), Args([1,1,2,1,2,3,3,4]), Args([1,1,2,3,4,5,5])]

exo_liste_doublons = ExerciseFunction(
    liste_doublons,
    inputs_liste_doublons,
    layout='pprint',
    layout_args=(40, 25, 25),
)
                                                                           

inputs_nombre_joueurs_annee = [Args(1950,charger_csv_dict('NBA_saisons.csv'))]

exo_nombre_joueurs_annee = ExerciseFunction(
    nombre_joueurs_annee,
    inputs_nombre_joueurs_annee,
    layout='pprint',
    layout_args=(40, 25, 25),
)
