![Lines of code](https://img.shields.io/tokei/lines/github/pacourbet/hta-api?style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pacourbet/hta-api)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pacourbet/hta-api)

# HTA-api

Ce projet est une api qui permet d'assurer un suivi de sa tension artérielle.
Le backend est développé avec Django Rest Framework et une base de donnée MySQL.
Le backend et la database sont lancés dans des containeurs Docker via le `docker-compose.yml`
L'api tourne en local chez moi sur un rapsberry pi. C'est la raison pour laquelle je n'utilise pas une image classique pour le container `MySQL`

## Configuration

### Step 1: créer un fichier .env avec les données d'environement
> :warning: `.env` à mettre dans le `.gitignore` pour garder ces data secrètes

```
  #.env file
  MYSQL_ROOT_PASSWORD=password
  MYSQL_DATABASE=databaseName
  MYSQL_USER=userName
  MYSQL_PASSWORD=otherPassword
  MYSQL_HOST=dbName
  MYSQL_PORT=portNumber
  DJANGO_SECRET_KEY=secretKey
```

### step 2: lancer le docker-compose

`docker-compose up`

Une fois que le container backend est lancé il faut l'executer en mode interactif pour y effectuer les migrations et créer l'utilisateur admin de l'application django

`docker container exec -it hta-app_backend_1 bash`

Une fois dans le containeur:

`python manage.py migrate`

Ensuite on créé l'admin

`python manage.py createsuperuser`

> :warning: il faut que le mot de passe entré pour le superuser soit le même que celui indiqué dans le fichier `.env`

## utilisation

Si tout a bien été configuré, on devrait avoir une api qui peut interragir avec une base de donnée sur notre réseau local. 
Dans mon cas les containeurs tournent sur un raspberry pi, donc il suffit de repérer l'IP du raspberry pi. On peut ensuite s'y connecter via un navigateur ou avec des commandes comme `curl` comme on le ferait avec n'importe quelle API.

**exemple**

tapez: `http://IP_LOCAL_PI/api/mesure` dans un navigateur pour visualiser les mesures
ou logez vous en tant qu'admin via: `http://IP_LOCAL_PI/admin` pour ajouter des valeurs. 

> IP_LOCAL_PI du type: 192.168.XX.XX
