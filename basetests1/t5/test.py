"""
Module de test pour les 30 fonctions définies dans le module précédent.
Pour exécuter : python -m unittest test_fonctions.py
"""
import unittest
from fonctions import (
    # Fonctions documentées et commentées
    calculer_aire_cercle, est_palindrome, compteur_mots, calculer_moyenne, generer_mot_de_passe,
    
    # Fonctions documentées mais non commentées
    fibonacci, est_premier, inverser_dictionnaire, celsius_vers_fahrenheit, compter_voyelles,
    
    # Fonctions commentées mais non documentées
    pgcd, factorielle, filtrer_pairs, formater_nom, fusionner_listes, convertir_temps,
    
    # Fonctions ni documentées ni commentées
    somme_liste, trouver_maximum, inverser_chaine, est_anagramme, appliquer_tva,
    compter_occurrences, extraire_extension, est_bissextile
)


class TestFonctions(unittest.TestCase):
    """Test unitaires pour l'ensemble des 30 fonctions."""
    
    def test_fonctions_documentees_commentees(self):
        """Teste les fonctions documentées et commentées."""
        # Test calculer_aire_cercle
        self.assertAlmostEqual(calculer_aire_cercle(2), 12.566370614359172)
        self.assertAlmostEqual(calculer_aire_cercle(0), 0)
        
        # Test est_palindrome
        self.assertTrue(est_palindrome("radar"))
        self.assertTrue(est_palindrome("A man a plan a canal Panama"))
        self.assertFalse(est_palindrome("python"))
        
        # Test compteur_mots
        self.assertEqual(compteur_mots("Ceci est un test"), 4)
        self.assertEqual(compteur_mots(""), 0)
        self.assertEqual(compteur_mots("  Espaces  multiples  "), 2)
        
        # Test calculer_moyenne
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculer_moyenne([0]), 0)
        self.assertIsNone(calculer_moyenne([]))
        
        # Test generer_mot_de_passe
        self.assertEqual(len(generer_mot_de_passe(10)), 10)
        self.assertEqual(len(generer_mot_de_passe()), 8)  # Valeur par défaut
        self.assertNotEqual(generer_mot_de_passe(8), generer_mot_de_passe(8))  # Aléatoire
    
    def test_fonctions_documentees_non_commentees(self):
        """Teste les fonctions documentées mais non commentées."""
        # Test fibonacci
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(7), 13)
        
        # Test est_premier
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(17))
        self.assertTrue(est_premier(97))
        self.assertFalse(est_premier(1))
        self.assertFalse(est_premier(15))
        self.assertFalse(est_premier(100))
        
        # Test inverser_dictionnaire
        self.assertEqual(inverser_dictionnaire({"a": 1, "b": 2}), {1: "a", 2: "b"})
        self.assertEqual(inverser_dictionnaire({}), {})
        
        # Test celsius_vers_fahrenheit
        self.assertEqual(celsius_vers_fahrenheit(0), 32)
        self.assertEqual(celsius_vers_fahrenheit(100), 212)
        self.assertEqual(celsius_vers_fahrenheit(-40), -40)
        
        # Test compter_voyelles
        self.assertEqual(compter_voyelles("Python"), 2)
        self.assertEqual(compter_voyelles("AEIOUYaeiouy"), 12)
        self.assertEqual(compter_voyelles("bcdfg"), 0)
    
    def test_fonctions_commentees_non_documentees(self):
        """Teste les fonctions commentées mais non documentées."""
        # Test pgcd
        self.assertEqual(pgcd(48, 18), 6)
        self.assertEqual(pgcd(17, 5), 1)
        self.assertEqual(pgcd(0, 5), 5)
        
        # Test factorielle
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(5), 120)
        
        # Test filtrer_pairs
        self.assertEqual(filtrer_pairs([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filtrer_pairs([1, 3, 5]), [])
        self.assertEqual(filtrer_pairs([]), [])
        
        # Test formater_nom
        self.assertEqual(formater_nom("jean", "dupont"), "Jean DUPONT")
        self.assertEqual(formater_nom("MARIE", "curie"), "Marie CURIE")
        
        # Test fusionner_listes
        self.assertEqual(fusionner_listes([1, 2], [2, 3]), [1, 2, 3])
        self.assertEqual(fusionner_listes([1, 2], [3, 4], [5]), [1, 2, 3, 4, 5])
        self.assertEqual(fusionner_listes(), [])
        
        # Test convertir_temps
        self.assertEqual(convertir_temps(0), "00:00:00")
        self.assertEqual(convertir_temps(3661), "01:01:01")
        self.assertEqual(convertir_temps(86399), "23:59:59")
    
    def test_fonctions_non_documentees_non_commentees(self):
        """Teste les fonctions ni documentées ni commentées."""
        # Test somme_liste
        self.assertEqual(somme_liste([1, 2, 3]), 6)
        self.assertEqual(somme_liste([]), 0)
        
        # Test trouver_maximum
        self.assertEqual(trouver_maximum([5, 3, 8, 2]), 8)
        self.assertEqual(trouver_maximum([-5, -3, -1]), -1)
        self.assertIsNone(trouver_maximum([]))
        
        # Test inverser_chaine
        self.assertEqual(inverser_chaine("python"), "nohtyp")
        self.assertEqual(inverser_chaine(""), "")
        
        # Test est_anagramme
        self.assertTrue(est_anagramme("chien", "niche"))
        self.assertTrue(est_anagramme("Paris", "Pari S"))
        self.assertFalse(est_anagramme("test", "texte"))
        
        # Test appliquer_tva
        self.assertEqual(appliquer_tva(100), 120)
        self.assertEqual(appliquer_tva(100, 10), 110)
        self.assertEqual(appliquer_tva(0), 0)
        
        # Test compter_occurrences
        self.assertEqual(compter_occurrences([1, 2, 2, 3, 2], 2), 3)
        self.assertEqual(compter_occurrences([1, 2, 3], 4), 0)
        self.assertEqual(compter_occurrences([], 1), 0)
        
        # Test extraire_extension
        self.assertEqual(extraire_extension("fichier.txt"), "txt")
        self.assertEqual(extraire_extension("document.pdf.zip"), "zip")
        self.assertEqual(extraire_extension("sans_extension"), "")
        
        # Test est_bissextile
        self.assertTrue(est_bissextile(2024))
        self.assertTrue(est_bissextile(2000))
        self.assertFalse(est_bissextile(2023))
        self.assertFalse(est_bissextile(1900))


if __name__ == "__main__":
    unittest.main()