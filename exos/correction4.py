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

def nom_top_categorie(categorie,annee_min,annee_max):
    """
    Fonction qui en paramètre prend une catégorie (parmi 'Passes', 'Points', '%2Points', '%3Points')
    et deux année
    et qui retourne le nom du meilleur joueurs dans cette catégorie durant l'intervalle de temps
    [annee_min ; annee_max]
    """
    max = 0
    nom = ''
    for enreg in saisons_NBA :
        if int(enreg['Année']) >= annee_min and int(enreg['Année']) <= annee_max and float(enreg[categorie]) > max :            
            max = float(enreg[categorie])
            nom = enreg['Athlète']
    return nom
                                                               

inputs_nom_top_categorie = [Args('Passes',1970,2000),Args('Points',1970,2000),Args('%2Points',1970,2000),Args('%3Points',1970,2000),Args('Points',1970,2000),
                           Args('Passes',2000,2017),Args('Points',2000,2017),Args('%2Points',2000,2017),Args('%3Points',2000,2017),Args('Points',2000,2017)]

exo_nom_top_categorie = ExerciseFunction(
    nom_top_categorie,
    inputs_nom_top_categorie,
    layout='pprint',
    layout_args=(40, 25, 25),
)
