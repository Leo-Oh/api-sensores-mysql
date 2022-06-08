# API-Passport

# DOCKER

Crear imagen de FastAPI

    sudo docker build -t fastapi-passport:0.1 .

Correr imagen creada de FastAPI

    sudo docker run --publish 9090:9090 --detach --name api-passport fastapi-passport:0.1 

# Docker para la base de datos    
Eliminamos todos los volúmenes ya que Docker crea volúmenes temporales sin pedirte permiso.

    sudo docker volume prune

Creamos un volumen

    sudo docker volume create mysql-db-data

Verificamos que se haya creado el volumen

    sudo docker volume ls

Correr imagen de mysql asignando la contraseña

    sudo docker run -d -p 9098:3306 --name mysql-db  -e MYSQL_ROOT_PASSWORD=password --mount src=mysql-db-data,dst=/var/lib/mysql mysql

Ejecutar mysql para entrar a la terminal y crear base de datos o querys

    sudo docker exec -it mysql-db  mysql -p
 

# Running

![image](https://user-images.githubusercontent.com/59150442/169755200-b78f6d7e-ebd2-43c0-b98f-23ab7501733b.png)
# api-sensores-mysql
