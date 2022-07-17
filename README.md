![Lines of code](https://img.shields.io/tokei/lines/github/pacourbet/hta-api?style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pacourbet/hta-api)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pacourbet/hta-api)

# HTA-app ❤️‍🔥

🙋‍♂️

Ce projet est une app qui permet d'assurer un suivi de sa tension artérielle 📓.
Le backend est développé avec Django 🐍 , une api Rest Framework et une base de donnée MySQL.
Le backend et la database sont lancés dans des containeurs Docker via le `docker-compose.yml`
L'api tourne en local chez moi sur un rapsberry pi. C'est la raison pour laquelle je n'utilise pas une image classique pour le container `MySQL`

## Configuration 📝

### Step 1: créer un fichier .env avec les données d'environement
> 🔒 `.env` à mettre dans le `.gitignore` pour garder les infos secrètes

```
# db env data used in django 
# database server data
MYSQL_ROOT_PASSWORD=password_db_root

# DJANGO settings
# database
MYSQL_DATABASE=databaseName
MYSQL_USER=username
MYSQL_PASSWORD=userpass
MYSQL_HOST=urlMysql
MYSQL_PORT=portMysql
# parameters
DJANGO_SECRET_KEY=secret_key
SERVER_IP=server_running_djangoApp

# airflow env data
AIRFLOW_UID=userId

```

### Step 2: lancer le docker-compose 🐳

`docker-compose up`

#### Effectuer les migrations

`docker container exec -it hta-app_backend_1 bash`

> *Note*:
> Obtenez le nom du containeur django avec `docker container ps`

Une fois dans le containeur:

`python manage.py migrate`

`python manage.py makemigrations`

option:

création d'un admin django

`python manage.py createsuperuser`

> Notes:
> - dans `docker-compose.yml` changer `hypriot/rapi-mysql` par `ubuntu/mysql` si le système hôte est différent d'un raspberry pi

Peut être qu'il faudra relancer le docker-compose une fois la migration effectuée pour que tout soit fonctionnel:

`docker-compose down`

`docker-compose up`

## Utilisation 🚀

Si tout a bien été configuré, on devrait avoir une api qui peut interragir avec une base de donnée sur notre réseau local. 
Dans mon cas les containeurs tournent sur un raspberry pi, donc il suffit de repérer l'IP du raspberry pi. On peut ensuite s'y connecter via un navigateur ou avec des commandes comme `curl` comme on le ferait avec n'importe quelle API.

**Exemple**

tapez: `http://IP_LOCAL:8000/api/mesures` dans un navigateur pour visualiser les mesures
ou `http://IP_LOCAL:8000/api/add` pour en ajouter

> 👉 IP_LOCAL du type: `192.168.XX.XX` si l'app tourne sur un raspberry pi
> 
> 👉 IP_LOCAL: `127.0.0.1` si l'app tourne sur votre machine

## Amélioration 💪

- [x] Brancher 🔌 un container Apache Airflow
- [ ] Ajouter la possibilité d'ajouter plusieurs mesures d'un coup
- [x] Brancher un containeur pour interface graphique (streamlit) (pas fonctionnel sur raspberry pi pour l'instant)
