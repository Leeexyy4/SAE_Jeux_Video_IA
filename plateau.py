from utils.logique import CASE_TYPE
import random
class Plateau():
    """La classe Plateau définit le type des cases présentes sur le plateau."""

    def __init__(self) -> None:
        """_summary_
            Initialisation du Plateau
        """
        # Définir le plateau
        self.__plateau:list[CASE_TYPE] = []
        self.__casesDecouvertes:list = []
        self.__tailleCase = 800 // 17

        self.__nomCase:dict = {
            CASE_TYPE.BOSS: "Boss",
            CASE_TYPE.LUCK: "Chance",
            CASE_TYPE.UNLUCK: "Malus",
            CASE_TYPE.TP: "Pouf",
            CASE_TYPE.REPLAY: "Rejoue",
            CASE_TYPE.RANDOM_TP: "Grrr",
            CASE_TYPE.WITCH: "Hutte",
            CASE_TYPE.SPECIAL: "Spéciale",
            CASE_TYPE.WELL: "Puit",
            CASE_TYPE.NOTHING: "Vide",
            CASE_TYPE.DEATH: "Mort",
            CASE_TYPE.SPAWN: "Départ"
        }

        self.__maxCases:dict = {
            CASE_TYPE.BOSS: 4,
            CASE_TYPE.LUCK: 26,
            CASE_TYPE.UNLUCK: 29,
            CASE_TYPE.TP: 2,
            CASE_TYPE.REPLAY: 20,
            CASE_TYPE.RANDOM_TP: 20,
            CASE_TYPE.WITCH: 1,
            CASE_TYPE.SPECIAL: 10,
            CASE_TYPE.WELL: 1,
            CASE_TYPE.DEATH: 1,
            CASE_TYPE.SPAWN:1,
            CASE_TYPE.NOTHING:55
        }

        # A retirer à la fin
        for ligne in range(10):
            for colonne in range(17):
                self.setCasesDecouvertes(((ligne, colonne)))
        ########################
        
        self.remplirPlateauAleatoirement()

    def getPlateau(self):
        """Renvoie le plateau de jeu."""
        return self.__plateau

    def getMaxCase(self):
        """Renvoie le plateau de jeu."""
        return self.__maxCases
    
    def getTailleCase(self):
        """Renvoie le plateau de jeu."""
        return self.__tailleCase

    def getNomCase(self):
        """Renvoie le nom_case de jeu."""
        return self.__nomCase
    
    def getCasesDecouvertes(self):
        """Renvoie les cases decouvertes de jeu."""
        return self.__casesDecouvertes

    def getCases(self, ligne, colonne):
        """Renvoie la couleur de la case à la position spécifiée."""
        return self.getPlateau()[ligne][colonne]
        
    def getNom(self, ligne, colonne):
        """Renvoie le nom de la case à la position spécifiée."""
        couleur_case = self.getPlateau()[ligne][colonne]  # Obtenir la couleur de la case
        nom_case = self.getNomCase()[couleur_case]
        return nom_case
    
    def getCaseJaune(self):
        """Renvoie les coordonnées correspondant à la case jaune."""
        for ligne in range(10):
            for colonne in range(17):
                if self.getPlateau()[ligne][colonne] == CASE_TYPE.SPAWN:
                    coord_case_jaune = (ligne, colonne)
        return coord_case_jaune

    def getCaseIndigo(self, joueur):
        """Renvoie les coordonnées correspondant aux cases indigo."""
        for ligne in range(10):
            for colonne in range(17):
                if self.getPlateau()[ligne][colonne] == CASE_TYPE.TP:
                    if joueur.getPlateaux() == ligne and joueur.getPlateauy() == colonne:
                        pass
                    else:
                        coord_case_indigo = (ligne, colonne)
        return coord_case_indigo

    def setPlateau(self, plateau):
        """Modifie le plateau de jeu."""
        self.__plateau = plateau

    def setCasesDecouvertes(self, casesDecouvertes):
        """Modifie les cases decouvertes de jeu."""
        self.__casesDecouvertes = casesDecouvertes
        
    def remplirPlateauAleatoirement(self):
        """Remplit le plateau de manière aléatoire en fonction de max_couleur."""
        # Crée une liste des couleurs disponibles en fonction de max_couleur
        couleurs_disponibles = []
        for couleurs, nombre_max in self.getMaxCase().items():
            couleurs_disponibles.extend([couleurs] * nombre_max)

         # Remplit le plateau de manière aléatoire
        for i in range(10):
            ligne_plateau = []
            for j in range(17):
                if couleurs_disponibles:  # Vérifiez si des couleurs sont disponibles
                    couleur_aleatoire = random.choice(couleurs_disponibles)
                    couleurs_disponibles.remove(couleur_aleatoire)  # Supprime la couleur de la liste
                    ligne_plateau.append(couleur_aleatoire)
        
            self.getPlateau().append(ligne_plateau)
        return self.getPlateau()