# HTA-api

Ce projet est une api qui permet d'assurer un suivi de sa tension artérielle.
Le backend est développé avec Django Rest Framework et une base de donnée MySQL.
Le backend et la database sont lancée dans des containeurs Docker via le `docker-compose.yml`
L'api tourne en local chez moi sur un rapsberry pi. C'est la raison pour laquelle je n'utilise pas une image classique pour le container `MySQL`

## Configuration

### Step 1: créer un fichier .env avec les données d'environement
> :warning: `.env` à mettre dans le `.gitignore` pour garder ces data secrètes
