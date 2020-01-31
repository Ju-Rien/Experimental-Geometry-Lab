# Experimental-Geometry-Lab

## TODOS

* Normaliser la transformation de Moebius par la racine du déterminant.
* Méthode pour calculer la trace (sur la transfo normalisée).

* Affichage d'un cercle.
  * Choix de librairie d'affichage. (Matplotlib?)

* Fonctions d'affichage récursive (le dernier générateur appliqué, les 3 autres générateurs et 1 cercle)
  * Cette fonction se rappellerait 3 fois, pour les 3 générateurs qui ne sont pas l'inverse du dernier appliqué. 

* Fonction d'intialisation des 4 cercles en chaîne de tangeance. (Initialiser 3 points, faire le cercle, prendre un 4e point sur le cercle, puis .)

* Bi-rapport(Cross-Ratio): 4 HComplex -> 1 HComplex. (Par le determinant des matrices [[z1, z2],[w1, w2]]).

## Pour utiliser le git:

Pour toutes les informations de base sur git: https://git-scm.com/book/en/v2

Github sert de serveur pour conserver ton répertoire git et le télécharger de n'importe où. Il faut comprendre que l'outil qu'on utilise vraiment est Git: Un gestionnaire de version (https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).

### Sous Linux:
Dans un terminal (Ctrl+Shift+T), rend toi dans le dossier dans lequel tu veux travailler:
```cd Ton/Chemin/vers/le/Workspace```

Puis, il faut cloner le répertoire du projet à l'endroit que tu es:
```git clone https://github.com/Ju-Rien/Experimental-Geometry-Lab```

À partir de maintenant, ton workflow est assez simple. À tout moment, tu peux utiliser `git status` pour connaître l'état des modifications du code, **localement** (c'est-à-dire que ça donne des informations sur les modifications que tu as fait sur ton ordi.)

(TODO: Suite de mini tuto git)


