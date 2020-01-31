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

Puis, il faut cloner le répertoire git du projet à l'endroit que tu es:

```git clone https://github.com/Ju-Rien/Experimental-Geometry-Lab```

À partir de maintenant, ton workflow est assez simple. À tout moment, tu peux utiliser `git status` pour connaître l'état des modifications du code, **localement** (c'est-à-dire que ça donne des informations sur les modifications que tu as fait sur ton ordi.)

Pour updater ta version locale avec celle du serveur Github (si tu n'as pas travaillé dessus depuis longtemps, par exemple), il faut utliser la commande `pull`:

```git pull https://github.com/Ju-Rien/Experimental-Geometry-Lab```

Ensuite, tu peux modifier les fichiers localement sur ton ordinateur! Si tu fais une modification d'un fichier, tu verra en utilisant `git status` en rouge, les fichiers modifiés. Pour ajouter un fichier au commit, c'est-à-dire de le lister comme un fichier que tu veux éventuellement partager aux autres, tu dois utiliser la commande:

```git add NomDuFichier```

Refaire `git status` te les montreras en vert, maintenant.

La prochaine étape lorsque tu as ajouté le nom des fichiers modifiés que tu veux partager, il est temps de commit. Ceci crée un "snapshot" des modifications faites, localement:

```git commit -m "Message de commit"```

Il est obligatoire de fournir un message de commit, ceci est le message qu'on va lire pour savoir ce sur quoi tu as travaillé.

Finalement, l'ultime action à faire si tu veux qu'on soit au courant des modifications que tu as faites, c'est de publié sur Github ton commit, avec la commande `push`:

```git push```

Ceci requiert tes informations Github (username, password). Tu verras ensuite les changements sur le serveur Github!


