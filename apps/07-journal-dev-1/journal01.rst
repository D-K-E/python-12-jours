#############################
Journal de Développement: 01
#############################

Auteur: Kaan Eraslan
Date de Création: 

Ceci est la première entrée de notre journal de développement de notre
application au but pédagogique.

Cette entrée va contenir un peu plus d'information que les autres parce que
c'est la première. Les autres entrées seront plus cours. Une entrée doit
répondre à trois questions suivantes:

- Est-ce que les changements sont critiques ?

- Est-ce que les changements sont compatibles avec le code existante ?

- Qu'est-ce qui est changé, pourquoi et comment ?

Les termes qu'on utilise pour regrouper les changements qu'on a fait sont:

- Ajouté (Added)
- Supprimé (Removed)
- Modifié (Changed)
- Fixé (Fixed)
- Obsolète (Deprecated)
- Sécurité (Security)

Les dates qu'on utilise suivent le format d'ISO: 2019-11-30

La gestion des versions de programme se fait en fonction de `SemVer standard
<https://semver.org/>`_. En gros Maj.Min.Patch:

- *Maj* introduit un changement incompatible avec la version ancienne, comme
  python 2 à python 3.

- *Min* introduit un changement compatible avec la version ancienne qui ajoute
  des nouvelles fonctionnalités

- *Patch* introduit des fixes compatibles pour les bogues du programme.

Le mise en page de journal est le suivant:

+---------------------------------------------------------+
| Titre: Journal Dev (Changelog)                          |
+---------------------------------------------------------+
|                                                         |
+---------------------------------------------------------+
| Sous Titre: Inédit                                      |
+---------------------------------------------------------+
| Liste des changements qu'on a pas encore fait           |
+----------------------------------------+----+---+---+---+
|                                        |    |   |   |   |
+----------------------------------------+----+---+---+---+
| Sous titre: Nouveau numéro de version  | Date de Commit |
+----------------------------------------+----+---+---+---+
| Sous sous titre: Ajouté                |    |   |   |   |
+----------------------------------------+----+---+---+---+
| Liste des fonctionnalités ajoutés      |    |   |   |   |
+----------------------------------------+----+---+---+---+
|                                        |    |   |   |   |
+----------------------------------------+----+---+---+---+
| Sous sous titre: Supprimé, etc         |    |   |   |   |
+----------------------------------------+----+---+---+---+
|                                        |    |   |   |   |
+----------------------------------------+----+---+---+---+
| Sous titre: L'ancien numéro de version | Date de Commit |
+----------------------------------------+----+---+---+---+
|                                        |    |   |   |   |
| Sous sous titre: Ajouté etc            |    |   |   |   |
+----------------------------------------+----+---+---+---+


Notez bien que les changements récents sont dans le tête du document
