Ce code est un ensemble de fonctions pour l'analyse de séquences d'ADN.

Fonctions:

is_adn(s): Vérifie si une chaîne de caractères s est une séquence d'ADN valide (c'est-à-dire qu'elle ne contient que les caractères "a", "t", "c", "g", "A", "T", "C" et "G").

positions(s, p): Trouve les positions de la sous-chaîne p dans la chaîne s.

distance_h(s1, s2): Calcule la distance de Hamming entre deux séquences d'ADN s1 et s2 (c'est-à-dire le nombre de positions où les deux séquences diffèrent).

distances_matrices(l): Construit une matrice de distances de Hamming entre toutes les paires de séquences d'ADN dans la liste l.