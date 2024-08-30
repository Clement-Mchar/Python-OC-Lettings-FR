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

### Définition des variables d'environnement

- Créez un fichier .env à la racine de votre projet, ajoutez-y les variables suivantes : 
  - DSN(Votre Clé d'URL Sentry que vous n'avez pas encore)
  - SECRET_KEY(Votre clé secrète Django, que vous pouvez générer sur `https://djecrety.ir`)
  - DOCKER_USERNAME(Votre nom d'utilisateur Docker)
  - COMMIT_HASH(Mettez juste "hash", vous pouvez mettre ce que vous voulez dans la mesure où ça respecte la casse, c'est nécessaire pour faire fonctionner le fichier compose.yaml)

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
- Compte Docker avec l'application Docker installée.
- Compte Render.
- Compte Sentry.

### Étapes de déploiement

#### 1. Création du service web sur Render
- Accédez à votre tableau de bord Render.
- Cliquez sur **New** > **Web Service**, puis connectez votre repository.
- Configurez les paramètres suivants :
  - **Start Command** : `gunicorn oc_lettings_site.wsgi`
  - **Instance Type** : Free
  - **Auto-Deploy** : No (dans **Advanced**).
- Déployez manuellement le service.
- Ajoutez l'adresse Render aux `ALLOWED_HOSTS` dans `settings.py`.

#### 2. Configuration de Sentry
- Créez un projet Sentry et sélectionnez **Django** comme plateforme.
- Récupérez le DSN de Sentry et collez à la variable DSN dans le fichier `.env`.

#### 3. Définir les secrets pour GitHub Actions
- Sur GitHub, accédez à **Settings** de votre repository.
- Dans **General**, renommez la branche principale en **master**.
- Allez dans **Secrets and Variables** > **Actions** > **New repository secret**, puis ajoutez les secrets suivants :
  - `DOCKER_USERNAME`
  - `DOCKER_PASSWORD`
  - `RENDER_DEPLOY_HOOK` (disponible dans les paramètres de votre service Render).
  - `SECRET_KEY` (depuis votre fichier `.env`).
  - `SENTRY_KEY_URL` (DSN de Sentry depuis `.env`).

### Exécution locale (optionnel)
- Pour tester localement, exécutez les commandes suivantes :
  ```bash
  docker compose build
  docker compose up


- Redéployez manuellement votre projet sur Render ou bien il se redéploiera automatiquement au prochain commit.
