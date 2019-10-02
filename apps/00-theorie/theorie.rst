################################################
Termes de Base et Petite Introduction Théorique
################################################

Ceci est une introduction très brève et générale sur ce qu'il faut savoir pour
développer des applications, c'est à dire lors que vous développez une
application/programme on attend qu'au moins vous sachiez les concepts qu'on
introduit ici.

A la fin de cette section vous allez trouver un petit glossaire pour des termes
qu'on emploi lors des notices des applications. Toutes les définitions
viennent de `FOLDOC <http://foldoc.org/>`_.


Unités de Base d'un Code
=========================

On emploi/rencontre en gros deux unités de base lors qu'on s'occupe avec le
code d'une `langue de niveau supérieur`_:

- valeur

- `fonction`_



Glossaire
==========

.. _`expression`: 

**Expression**:
Une partie d'un code d'une langue de niveau supérieur, qui produit une valeur
lors que son exécution a terminé.

.. _`langue de niveau supérieur`: 

**Langue de niveau supérieur**:
Un langage de programmation qui donne des abstractions sur le programme
d'assemblée.

.. _`fonction`:

**Fonction**:
Une correspondance. Si D et C sont des ensembles (domain et co-domain), une
fonction f est, écrit comme :math:`f: D → C`, un sous ensemble d'ensemble
:math:`{(d,c) | d ∈ D, c ∈ C}`. C'est ensemble est nommé l'ensemble de
multiplication cartésien de D et C, et il est désigné par le symbol
:math:`DxC`. Le sous ensemble f doit satisfaire les conditions suivantes:

- Pour chaque :math:`d ∈ D` il faut qu'il y a un correspondant dans C.

- Pour chaque :math:`d ∈ D`, s'il y a deux correspondants :math:`c1, c2 ∈ C`,
  alors :math:`c1=c2`.

Par contre l'usage des fonctions en informatique, malgré l'inspiration, est
beaucoup moins strict. On comprend par la fonction ce qui fait une
correspondance entre un `domain`_ et `codomain`_.

.. _`domain`:

**Domain**:
L'ensemble dont les membres sont des valeurs auxquelles la fonction est
défini.

.. _`codomain`:

**Codomain**:
L'ensemble dont les membres sont des valeurs possibles pour le résultat d'une
fonction.

.. _`range`:

**Range**:
L'ensemble dont les membres sont des valeurs qui sortent comme résultat d'une
fonction.
