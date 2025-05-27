def calculer_moyenne_ponderee(nombres: list[float], coefficients: list[float]) -> float:
    """
    Calcule la moyenne pondérée d'une liste de nombres avec leurs coefficients.

    La formule utilisée est :
    ∑(nombre * coefficient) / ∑coefficients

    Args:
        nombres (list[float]): Liste des nombres à moyenner.
            Exemple : [15.5, 18.0, 12.5]
        coefficients (list[float]): Liste des coefficients correspondants.
            Exemple : [2, 3, 1]
            Doit être de même longueur que 'nombres'

    Returns:
        float: La moyenne pondérée calculée.
            Exemple : 16.25 pour les entrées ci-dessus

    Raises:
        ValueError: Si les listes sont vides ou de tailles différentes
        TypeError: Si les entrées ne sont pas numériques

    Exemples:
        >>> calculer_moyenne_ponderee([10, 20], [1, 2])
        16.666666666666668
        >>> calculer_moyenne_ponderee([15.5, 18.0, 12.5], [2, 3, 1])
        16.25
    """
    # Vérification des entrées
    if len(nombres) != len(coefficients):
        raise ValueError("Les listes doivent avoir la même longueur")
    if not nombres:
        raise ValueError("Les listes ne peuvent pas être vides")

    # Vérification du type des éléments
    if not all(isinstance(n, (int, float)) for n in nombres) or \
       not all(isinstance(c, (int, float)) for c in coefficients):
        raise TypeError("Les éléments doivent être numériques")

    # Calcul du numérateur (∑n*c) et dénominateur (∑c)
    somme_produits = sum(n * c for n, c in zip(nombres, coefficients))
    somme_coefficients = sum(coefficients)

    # Éviter la division par zéro (même si coefficients vide déjà capté plus haut)
    if somme_coefficients == 0:
        raise ValueError("La somme des coefficients ne peut pas être nulle")

    # Retourner le résultat arrondi à 2 décimales
    return round(somme_produits / somme_coefficients, 2)