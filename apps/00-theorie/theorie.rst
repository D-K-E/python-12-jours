################################################
Termes de Base et Petite Introduction Théorique
################################################

Ceci est une introduction très brève et générale sur ce qu'il faut savoir pour
développer des applications simples, c'est à dire lors que vous développez une
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


Sans la fonction le fichier ne sera qu'une donnée, sans la valeur, on n'aura
pas d'argument pour les fonctions, donc au bout du compte on n'aura pas une
computation. Ensemble, ils constituent l'unité principale d'une langue de
computation, qui est l'expression.

Le concept de valeur n'est pas difficile à saisir, c'est touts ce qu'on peut
appeler donnée. La fonction par contre est un peu plus difficile à saisir,
parce qu'il y a un divergence entre l'usage mathématique et l'usage en
informatique.

On appel une fonction tout ce qui donne une valeur de sortie en informatique.
Formellement on appel un `procédure`_ tout ce qui ne donne pas une valeur de
sortie mais effectue un changement d'état dans le programme.

Bash, par exemple est utilisé souvent pour écrire des procédures, plutôt que
des fonctions. Ces changements d'état dans le programme qui se passent lors de
l'exécution de programme s'appelle des effets de bords, ou des effets
secondaires (side effects).

A part de ces éléments primitives chaque langue puissante nous donne, d'après
le fameux ouvrage de Sussman et Abelson (Abelson, Harold, and Jay Sussman.
Structure and Interpretation of Computer Programs. MIT Electrical Engineering
and Computer Science. London, 1996), un moyen de combinaison, et un moyen
d'abstraction.

Les moyens de combinaison nous permet de simplement combiner des expressions.
Les moyens d'abstraction nous permet de référer aux unités, soit primitives,
soit combinés.


Ces éléments existent dans la plupart des langues de programmation, donc
l'identification de ces éléments dans une nouvelle langue vous permettrait de
facilement s'adapter à l'environnement.


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

L'expression est dans ce cas là :code:`1+5`

L'effet de bord est :code:`a=Expr`

Chaque langue a des expressions. Par exemple:


.. code:: python

    # python
    a = 2 + 1
    b = a + 3
    c = b + 4

.. code:: c++
    
    // c++
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

D'abord les dichotomies qu'on énumère ici sont simplement certains critères
qui nous permettent de mettre des langues en perspective. Ils ne sont pas des
défis insurmontables. En plus ces critères eux mêmes se sont révélé par
l'usage des langues à travers le temps. Cet usage avait affecté naturellement
à la fois l'évolution et à la fois le type de problème sur lequel on emploi
la langue en question, donc au bout du compte l'adoption d'une langue
determine la direction de son évolution et donc la communauté qui l'adopte est
de loin l'acquis le plus important pour une langue de programmation. Quant aux
les dichotomies qu'on énumère ici, elles viennent à la fois d'évolution de la
langue et à la fois certains choix dès le début de sa conception comme celles
qui sont liées à d'être faiblement typé ou fortement typé, etc.


La première dichotomie est lié à les privilèges des certains expressions,
et homoïconicité des expressions.

.. image:: ax1.png

Celle-là est déterminé par la réponse à la question "Est-ce qu'il faut être
capable d'exprimer certains computations plus facilement que les autres". Les
langues qui sont issues de la famille Lisp disent tout simplement "Non" à cela.
La famille ALGOL a tendance à faciliter les boucles par exemple. Cet enjeu
devient important lorsqu'on considère la rétrocompatibilité des nouvelles
versions des langues. Ce problème est évident pour la famille ALGOL, le
fameux exemple étant la rupture qui persiste entre Python 2 et Python 3.


La deuxième dichotomie est lié au temps de développement et au temps d'exécution
des programmes

.. image:: ax2.png

La comparaison fameuse est celle de python et de c++. La discussion se déroule
souvent autour de la question "d'être typé d'accord, mais comment ?". En gros,
les pythonista disent que ce n'est pas à nous de s'occuper avec les types,
parce que elle pourra être fait par l'interpréteur et on gagne le temps de
développement en laissant cette tache à l'interpréteur et quand on veut plus
de performance, c'est mieux de simplement d'acquérir des nouvelles mieux
machines ou d'écrire les parties critiques dans une différente langue, quelque
chose comme c.


La troisième dichotomie est lié à l'utilité et la pureté de la langue de
programmation

.. image:: ax3.png


La quatrième dichotomie est lié à d'être dynamiquement ou statiquement typé.
La cinquième dichotomie est lié à d'être fortement ou faiblement typé.



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
Une correspondance. Si D et C sont des ensembles (`domaine`_ et `codomaine`_), une
fonction f est, écrit comme :math:`f: D → C`, un sous ensemble d'ensemble
:math:`{(d,c) | d ∈ D, c ∈ C}`. C'est ensemble est nommé l'ensemble de
multiplication cartésien de D et C, et il est désigné par le symbol
:math:`DxC`. Le sous ensemble f doit satisfaire les conditions suivantes:

- Pour chaque :math:`d ∈ D` il faut qu'il y a un correspondant dans C.

- Pour chaque :math:`d ∈ D`, s'il y a deux correspondants :math:`c1, c2 ∈ C`,
  alors :math:`c1=c2`.

Par contre l'usage des fonctions en informatique, malgré l'inspiration, est
beaucoup moins strict. On comprend par la fonction ce qui fait une
correspondance entre un `domaine`_ et `codomaine`_.

.. _`procédure`:

**Procédure**:
Une séquence des instructions pour exécuter une tache. Il distingue des
fonctions par l'absence de valeur de retour. Ils sont exécuté pour l'`effet
de bord`_.

.. _`domaine`:

**Domain**:
L'ensemble dont les membres sont des valeurs auxquelles la fonction est
défini.

.. _`codomaine`:

**Codomaine**: L'ensemble d'arrivé, dont les membres sont des valeurs
possibles pour le résultat d'une fonction.

.. _`intervalle`:

**Intervalle** (aussi appelé Image): L'ensemble dont les membres sont des
valeurs qui sortent comme résultat d'une fonction, il correspond pour la
plupart de temps un sous-ensemble de `codomaine`_.

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
