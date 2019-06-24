# Contenedores de Docker

### Introducción

La contenedorización es una herramienta relativamente nueva pero sumamente útil para los desarrolladores de hoy en día. Docker nos permite empaquetar aplicaciones junto a el kernel de linux de nuestra elección, las librerías y el ambiente necesario para correr nuestra aplicación siempre bajo las mismas condiciones y sin importar la computadora (servidor) en el cual vayamos a realizar el deployment.  

Obtenemos un contenedor a partir de una imagen. Una **imagen** es un ejecutable que contiene toda la configuración, código, comandos, librerías, y demás necesario para correr nuestra aplicación. Un **contenedor** no es más que una instancia corriendo a partir de una imagen.  

Para visualizar mejor lo que una imagen es, [este ejemplo](https://github.com/nathsmo/Sistemas-Operativos-2019/blob/master/Lab%2001/Dockerfile) muestra el docker file (*imagen*) de una imagen que utiliza ubuntu e instala python.

Para empezar a aprender los comandos básicos de docker, primero es necesario [instalarlo](https://docs.docker.com/install/).  

### Comandos 

A continuación se presentan ejemplos de los comandos principales de docker:

#### Pull

```console
user@ubuntu:~$ docker pull [image-name]
```

#### Run

#### Image

#### Container

#### Attach

#### Checkpoint 

#### Commit

#### Config

