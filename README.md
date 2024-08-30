## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement du site

### Prérequis
- Un compte Docker et l'application Docker.
- Un compte Render.

### Définition des variables d'environnement

- Créez un fichier .env à la racine de votre projet, ajoutez-y les variables suivantes : 
  - DSN(Votre Clé d'URL Sentry que vous n'avez pas encore)
  - SECRET_KEY(Votre clé secrète Django)
  - DOCKER_USERNAME(Votre nom d'utilisateur Docker)
  - COMMIT_HASH(Mettez juste "hash", vous pouvez mettre ce que vous voulez dans la mesure où ça respecte la casse, c'est nécessaire pour faire fonctionner le fichier compose.yaml)

#### Créez votre service web sur Render
- Accédez au tableau de bord de Render et cliquez sur "New" en haut à droite à côté de votre nom d'utilisateur.
- Créez un web service en indiquant votre repository et cliquez sur "Connect"
- Descendez dans les paramètre et à l'option "StartCommand", entrez "gunicorn oc_lettings_site.wsgi"
- Dans la partie Instance Type, cliquez sur "Free"
- Cliquez sur "Advanced" et paramétrez "Auto-Deploy" sur "No"

- Déployez manuellement le web service

- Ajoutez l'adresse du déploiement aux ALLOWED_HOSTS dans votre fichier settings.py

#### Créez votre projet Sentry

- Accédez à votre compte Sentry, cliquez sur "Create Project"
- Sélectionnez Django dans la partie "Choose your platform"
- Donnez un nom à votre projet, et cliquez sur "Create Project"
- Dans le fichier settings.py,  la valeur de la variable "dsn" et collez la en tant que valeur de "DSN" dans votre fichier .env

### Définition des secrets de Github Actions

- Sur Github, allez sur la page de votre repository, et cliquez sur Settings.
- Dans l'onglet General, changez le nom de votre branche en "master" pour éviter tout problème avec le workflow.
- Allez dans Secrets and Variables, puis dans le sous menu "Actions".
- Dans l'onglet "Secrets", cliquez sur "New repository secret", et renseignez y les variables suivantes : 
  - DOCKER_PASSWORD(Votre mot de passe docker)
  - DOCKER_USERNAME
  - RENDER_DEPLOY_HOOK(Allez dans les settings de votre service web sur Render, descendez et copiez la valeur de Deploy Hook, puis collez là comme valeur de ce secret.)
  - SECRET_KEY(Copiez collez la SECRET_KEY de votre fichier .env)
  - SENTRY_KEY_URL(Copiez collez la valeur DSN de votre fichier .env)

- Dans votre terminal de commandes, entrez les commandes : 
  -`docker compose build`
  -`docker compose up`

- Redéployez manuellement votre projet sur Render ou bien il se redéploiera automatiquement au prochain commit.
