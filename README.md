# Experimental-Geometry-Lab

## TODOS

### Math

M1M2m1m2 := C

* Trouver une forme de tr(C) en terme de x = tr(M1), y = tr(M2) et z = tr(M1M2). *Hint*: Ish proche de x²+y²+z²-xyz+2? Par Cayley-Hamilton.

* Trouver une façon de générer tr(C) = -2, une transformation parabolique. (C n'aurait qu'un seul point fixe.)

* Voir fichier en date du 10 février sur Teams!

### Général

* Assurer que tr(M1M2m1m2)=-2

* Affichage d'un cercle.
  * Choix de librairie d'affichage. (Matplotlib?)
  * Paufinage

* Fonctions d'affichage récursive
  * **Note**: On peut itérer sur TreeNode avec un boucle `for` standard

* Fonction d'intialisation des 4 cercles en chaîne de tangeance 
  * "Sliders" pour les points arbitraires sur les cercles (seulement sur 2 des 4 cercles). Slider du style (0,1)?

### MoebTr

* Coder une fonction qui donne tous les points fixes d'une transformation de Möbius (MoebTr).

### HComplex

### TreeNode



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


