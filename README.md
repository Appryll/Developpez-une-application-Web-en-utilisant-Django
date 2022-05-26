# Projet 9 - Développez une application Web en utilisant Django - OpenClassrooms

<img src="media/img/LogoLITReview.png" widht="250" height="250">

Cet application web permet à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres ou d’articles à la demande.

## Mise en place du projet: 

#### I) Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.

###### - Récupération du projet

    $ git clone https://github.com/Appryll/Projet-9-Developpez-une-application-Web-en-utilisant-Django.git

    Se déplacer dans le repertoire du projet :

    $ cd Projet-9-Developpez-une-application-Web-en-utilisant-Django-master

###### -Créer et activer l'environnement virtuel 
    $ python -m venv env 
    $ ~env\scripts\activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    Se déplacer vers le repertoire config: 
    $ cd config
    $ python manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas disponible :
    $ python manage.py runserver <your_port>

###### - Créer un super user :
    $ python manage.py createsuperuser
    
    Suivre les indications de la console. Une fois le super user créé, vous pouvez vous connecter à l'espace d'admin du site grâce à son identifiant et mot de passe.

###### - Naviguer vers l'éspace d'administration
    Ouvrir un navigateur, et aller à l'adresse du site en ajouter /admin. ex : http://127.0.0.1:8000/admin/

    Entrez l'identifiant et le mot de passe du super user créé.

###### - Naviguer sur le site
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel
    deactivate

-----
#### II) MacOS, Linux :
Dans le terminal, naviguer vers le dossier souhaité.

###### - Récupération du projet
     $ git clone https://github.com/Appryll/Projet-9-Developpez-une-application-Web-en-utilisant-Django.git

    Se déplacer dans le repertoire du projet :
    $ cd Projet-9-Developpez-une-application-Web-en-utilisant-Django-master

###### -Créer et activer l'environnement virtuel
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### - Installer les paquets requis
    $ pip install -r requirements.txt

###### - Démarrer le serveur de developpement :
    Se déplacer vers le repertoire config: 
    $ cd config
    $ python3 manage.py runserver

    Le site sera accéssible à l'adresse local : 127.0.0.1:8000 sur le port 8000 par défaut. Si le port n'est pas disponible :
    $ python3 manage.py runserver <your_port>

###### - Créer un super user :
    $ python3 manage.py createsuperuser
    
    Suivre les indications de la console. Une fois le super user créé, vous pouvez vous connecter à l'espace d'admin du site grâce à son identifiant et mot de passe.

###### - Naviguer vers l'éspace d'administration
    Ouvrir un navigateur, et aller à l'adresse du site en ajouter /admin. ex : http://127.0.0.1:8000/admin/

    Entrez l'identifiant et le mot de passe du super user créé.

###### - Naviguer sur le site
    Ouvrir un navigateur, et aller à l'adresse du site. ex : http://127.0.0.1:8000/

###### - Quitter l'envirement virtuel
    deactivate
 
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

## L’application permet de :
    ● demander des critiques de livres ou d’articles, en créant un ticket ;
    ● publier des critiques de livres ou d’articles

## Un utilisateur peut :
    ●  s’inscrire et se connecter
    ● consulter un flux contenant les derniers tickets et les commentaires des utilisateurs qu'il suit, classés par ordre chronologique, les plus récents en premier ;
    ● créer de nouveaux tickets pour demander une critique sur un livre/article ;
    ● créer des critiques en réponse à des tickets ;
    ● créer des critiques qui ne sont pas en réponse à un ticket. Dans le cadre d'un processus en une étape, l'utilisateur créera un ticket puis un commentaire en réponse à son propre ticket ;
    ● voir, modifier et supprimer ses propres tickets et commentaires ;
    ● suivre les autres utilisateurs en entrant leur nom d'utilisateur ;
    ● voir qui il suit et suivre qui il veut ;
    ● cesser de suivre un utilisateur.

## Un développeur peut :
    ● créer un environnement local en utilisant env, et gérer le site en se basant sur cette documentation.