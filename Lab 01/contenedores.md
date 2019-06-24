# Contenedores de Docker

### Introducción

La contenedorización es una herramienta relativamente nueva pero sumamente útil para los desarrolladores de hoy en día. Docker nos permite empaquetar aplicaciones junto a el kernel de linux de nuestra elección, las librerías y el ambiente necesario para correr nuestra aplicación siempre bajo las mismas condiciones y sin importar la computadora (servidor) en el cual vayamos a realizar el deployment.  

Obtenemos un contenedor a partir de una imagen. Una **imagen** es un ejecutable que contiene toda la configuración, código, comandos, librerías, y demás necesario para correr nuestra aplicación. Un **contenedor** no es más que una instancia corriendo a partir de una imagen.  

Para visualizar mejor lo que una imagen es, [este ejemplo](https://github.com/nathsmo/Sistemas-Operativos-2019/blob/master/Lab%2001/Dockerfile) muestra el docker file (*imagen*) de una imagen que utiliza ubuntu 18.04 e instala python 3.

Para empezar a aprender los comandos básicos de docker, primero es necesario [instalarlo](https://docs.docker.com/install/).  

### Comandos 

A continuación se presentan ejemplos de los comandos principales de docker.

#### Pull

El comando `docker pull [nombre-imagen]` permite descargar imágenes previamente realizadas y publicadas en [dockerhub](www.hub.docker.com) por otras personas. Por ejemplo, podemos descargar a nuestro directorio esta imagen de [redis](https://hub.docker.com/_/redis) de la siguiente manera:

```console
user@ubuntu:~$ docker pull redis
```

#### Run

El comando `docker run [nombre-imagen]` crea una instancia a partir de la imagen indicada en el comando e inicia su ejecución (determinada por el dockerfile). Además, existen parámetros que podemos configurar en el comando, como un mapeo de puertos por ejemplo, agregando `-p puerto_externo:puerto_interno`. Por ejemplo, para correr la imagen de redis previamente descargada, el comando sería:

```console
user@ubuntu:~$ docker run --name contenedor-redis redis
```

En este ejemplo, agregamos el parámetro `--name contenedor-redis` para asignarle un nombre específico al contenedor que se crea.  

#### Image

El comando `docker image` permite manejar las imágenes disponibles. 

Para listar las imágenes disponibles utilizamos el comando `ls`:

```console
user@ubuntu:~$ docker image ls
```

Y para eliminar una imagen existente el se utiliza el comando `rm [id-de-imagen]`:

```console
user@ubuntu:~$ docker image rm d3e3588af517
```

#### Container

El comando `docker container` permite manejar los contenedores disponibles, ya sea estén corriendo o no.

Para listar los contenedor activos utilizamos el comando `ls`:

```console
user@ubuntu:~$ docker container ls
```

Para listar os contenedores tanto activos como inactivos utilizamos el comando `ps`:

```console
user@ubuntu:~$ docker container ps
```

De igual forma, para detener la ejecución de un contenedor activo utilizamos el comando `stop [id-contenedor]`:

```console
user@ubuntu:~$ docker container stop d3e3588af517
```

#### Attach

El comando `docker attach` permite ingresar en la terminal al contenedor, utilizando el input y output estándar de la terminal para interactuar directamente con el contenedor.

Por ejemplo, podemos hacer attach al contenedor que previamente pusimos a correr bajo el nombre de *contenedor-redis* de la siguiente forma:

```console
user@ubuntu:~$ docker attach contenedor-redis
```

#### Commit

El comando `docker commit [contenedor] [repositorio:tag]` permite guardar una nueva versión de la imagen en cuestión, para obtener un control de versiones a la hora de publicar nuestras imágenes en [dockerhub](www.hub.docker.com).

Por ejemplo:

```console
user@ubuntu:~$ docker commit contenedor-redis tortolala/redis:v2
```

#### Config & Checkpoint 

El comando `docker config` nos permite manejar archivos de configuración al utilizar un *swarm orchestrador*. Y respectivamente utiliza los comandos de complemento `create`, `inspect`, `ls` y `rm`.

Este comando exprimental `docker checkpoint` permite manejar distintos checkpoints de contenedores, respectivamente utilizando los comandos de complemento `create`, `ls` y `rm`. 

Más información sobre [docker swarm](https://docs.docker.com/get-started/part4/).