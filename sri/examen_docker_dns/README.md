# Examen SRI Docker DNS

## 1) Explica métodos para 'abrir' una consola/shell a un contenedor que se está ejecutando.
### - Terminal: mediante el comando:
```console
docker -exec -it <contenedor> bash
``````
### - Visual Studio Code: una vez instalado el plugin de Docker, en el apartado de la lista de contenedores, hacemos click derecho encima de una contenedor activo y seleccionamos la opción de "Attach Shell".
## 2)  En el contenedor anterior, con que opciones tiene que haber sido arrancado para poder interactuar con las entradas y salidas del contenedor?
### `-t:` mantiene la entrada estándar abierta.
### `-i:` asigna una pseudoterminal.
## 3) ¿Cómo sería un fichero docker-compose para que dos contenedores se comuniquen entre si en una red solo de ellos?
```yaml
version: '3.9'

services:
  dns: # Servidor DNS
    container_name: dns
    image: ubuntu/bind9:latest
    working_dir: /etc/bind
    volumes:
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf:/etc/bind/named.conf
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.options:/etc/bind/named.conf.options
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.local:/etc/bind/named.conf.local
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.default-zones:/etc/bind/named.conf.default-zones
      - /home/asir2/asir/github/sri/docker/dns/lib/:/var/lib/bind/
    networks:
      mynetwork:
    ports: 
      - '53:53/udp'
    expose:
      - '53/udp'
    restart: on-failure
  
  ubuntu: # Cliente Ubuntu
    container_name: ubuntu
    image: ubuntu:latest
    working_dir: /home
    volumes:
      - /home/asir2/asir/asir2/sri/ubuntu/home:/home
    networks:
      mynetwork:
    stdin_open: true
    tty: true
    restart: on-failure
    dns:
      - 172.28.0.53

networks: # Red Servicios
  mynetwork:
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/24
          gateway: 172.28.0.254
```
## 4) ¿Qué hay que añadir al fichero anterior para que un contenedor tenga la IP fija?
```yaml
version: '3.9'

services:
  dns: # Servidor DNS
    container_name: dns
    image: ubuntu/bind9:latest
    working_dir: /etc/bind
    volumes:
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf:/etc/bind/named.conf
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.options:/etc/bind/named.conf.options
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.local:/etc/bind/named.conf.local
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.default-zones:/etc/bind/named.conf.default-zones
      - /home/asir2/asir/github/sri/docker/dns/lib/:/var/lib/bind/
    networks:
      mynetwork:
        ipv4_address: 172.28.0.53
    ports: 
      - '53:53/udp'
    expose:
      - '53/udp'
    restart: on-failure
  
  ubuntu: # Cliente Ubuntu
    container_name: ubuntu
    image: ubuntu:latest
    working_dir: /home
    volumes:
      - /home/asir2/asir/asir2/sri/ubuntu/home:/home
    networks:
      mynetwork:
        ipv4_address: 172.28.0.209
    stdin_open: true
    tty: true
    restart: on-failure
    dns:
      - 172.28.0.53

networks: # Red Servicios
  mynetwork:
    ipam:
      config:
        - subnet: 172.28.0.0/24
          gateway: 172.28.0.254
```
### Tenemos que especificar la dirección IP del contenedor en el apartado de al red.
## 5) ¿Que comando de consola puedo usar para saber las ips de los contenedores anteriores? Filtra todo lo que puedas la salida. El comando no es "ip a", tiene que ser desde fuera del contenedor.
### - Dirección IP de un contenedor activo en específico:
```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <contenedor>
```
### - Direcciones IP de todos los contenedores activos:
```console
docker network inspect -f '{{range $key, $value := .Containers}}{{if $value.Name}}{{.IPv4Address}}{{end}}{{end}}' docker_mynetwork
```
## 6) ¿Cual es la funcionalidad del apartado "ports" en docker compose?
### El apartado `ports` en Docker Compose se utiliza para exponer los puertos de un contenedor en el host. 
### Cuando se define un servicio en `Docker Compose`, se puede especificar una lista de puertos que el contenedor expone y que se pueden acceder desde el host. La sintaxis para definir los puertos es `<puerto_host>:<puerto_contenedor>/<protocolo>`. Por ejemplo, si se desea exponer el puerto 80 del contenedor en el puerto 8080 del host, se puede utilizar la siguiente definición:

```yaml
services:
  httpd:
    image: httpd:latest
    ports:
      - "8080:80"
```

### En este ejemplo, el servicio `httpd` utiliza la última imagen de 'httpd' y expone el puerto `80` del contenedor en el puerto `8080` del host. 

### La opción `ports` también se puede utilizar para exponer puertos `UDP` en lugar de `TCP`, especificando el protocolo en la definición del puerto. Por ejemplo, para exponer el puerto `53 UDP` del contenedor en el puerto `53 UDP` del host, se puede utilizar la siguiente definición:

```yaml
services:
  dns:
    image: ubuntu/bind9:latest
    ports:
      - "53:53/udp"
```

### En este ejemplo, el servicio `dns` utiliza la imagen de Ubuntu con Bind9 y expone el puerto 53 UDP del contenedor en el puerto 53 UDP del host.
## 7) ¿Para que sirve el registro CNAME? Pon un ejemplo
### El registro `CNAME` se utiliza para crear un alias de un nombre de dominio a otro nombre de dominio. Esto es útil cuando se desea que un nombre de dominio tenga varios nombres alternativos que apunten al mismo servidor:
```yaml
ejemplo.com.      IN  A      8.8.8.8
www.ejemplo.com.  IN  CNAME  ejemplo.com.
```
## 8) ¿Como puedo hacer para que la configuración de un contenedor DNS no se borre si creo otro contenedor?
## Se pueden crear volúmenes que contengan el contenido mapeado desde nuestro contenedor docker, es decir, la configuración básica del DNS, a nuestro equipo local:
```yaml
version: '3.9'

services:
  dns: # Servidor DNS
    container_name: dns
    image: ubuntu/bind9:latest
    working_dir: /etc/bind
    volumes:
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf:/etc/bind/named.conf
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.options:/etc/bind/named.conf.options
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.local:/etc/bind/named.conf.local
      - /home/asir2/asir/github/sri/docker/dns/bind/named.conf.default-zones:/etc/bind/named.conf.default-zones
      - /home/asir2/asir/github/sri/docker/dns/lib/:/var/lib/bind/
    networks:
      mynetwork:
        ipv4_address: 172.28.0.53
    ports: 
      - '53:53/udp'
    expose:
      - '53/udp'
    restart: on-failure

networks: # Red Servicios
  mynetwork:
    ipam:
      config:
        - subnet: 172.28.0.0/24
          gateway: 172.28.0.254
```


