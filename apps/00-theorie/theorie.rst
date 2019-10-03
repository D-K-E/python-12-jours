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


Sans la fonction le fichier ne sera qu'une donnée, sans la valeur, on n'aura pas 
d'argument pour les fonctions, donc au bout du compte on n'aura pas une computation.

Le concept de valeur n'est pas difficile à saisir, c'est touts ce qu'on peut appeler
donnée. La fonction par contre est un peu plus difficile à saisir, parce qu'il y a
un divergence entre l'usage mathématique et l'usage en informatique.

On appel une fonction tout ce qui donne une valeur de sortie en informatique.
Formalement on appel un procédure tout ce qui ne donne pas une valeur de sortie
mais effectue un changement d'état dans le programme.

Bash, par exemple est utilisé souvent pour écrire des procédures, plutôt que des
fonctions. Ces changements d'état dans le programme qui se passent lors de l'exécution
de programme s'appel des effets de bords, ou des effets sécondaires (side effects).


Elements d'une Fonction
-------------------------


Valeurs d'Entrée
-----------------

On l'appel argument aussi. Il pouvait être typé ou pas.


Corps d'une Fonction
---------------------

Une expression est une partie d'un code d'une langue de niveau supérieur, qui produit une valeur
lors que son exécution a terminé.


.. code:: python

   a = 1 + 5
   print(a)

L'expréssion est dans ce cas là :code:`1+5`

L'effet de bord est :code:`a=Expr`

Chaque langue a des expréssions. Par exemple:


.. code:: python

    a = 2 + 1
    b = a + 3
    c = b + 4

.. code:: c++
        
    int a = 2 + 1;
    int b = a + 3;
    int c = b + 4;

.. code:: clojure

    ;; clojure
    (
      def a (+ 1 2)
    )
    (
        def b  (+ a 3 ) 
    )
    (
        def c  (+ b 4)
    )




Computation et Langues de Programmation
==========================================


3 Dicathomies Pratiques des langues de programmation
-----------------------------------------------------

La première dicathomie est lié à les privilèges des certains expréssions,
et homoïconicité des expréssions.

.. image:: ax1.png


La deuxième dicathomie est lié au temps de dévéloppement et au temps d'exécution
des programmes

.. image:: ax2.png


La troisième dicathomie est lié à l'utilité et la pureté de la langue de
programmation

.. image:: ax3.png


Erreurs
--------

Ils sont inévitables. Il faut trouver des façons pour combattre contre eux.


Type
-----




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

.. _`effet de bord`:

**Effet de Bord**:
Un construit de la langue qui modifie l'état de système. Les plus courants sont
l'affectation, entrée, sortie. Une langue sans les effets de bord est purement
fonctionnelle, dont exécution est constitué par l'évaluation des expressions, 
et tout les sous-expréssions ont une transparence référentielle.

.. _`transparence référentielle`:

**Transparence Référentielle**:
L'Expréssion E a une transparence référentielle si toutes les sous expressions
sont interchangeable avec leurs valeurs sans un changement de valeur de E.
