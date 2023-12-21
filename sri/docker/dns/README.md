# Docker - DNS
Añade un `Readme.md` con la descripción de las opciones del fichero `docker-compose.yaml`.

## docker-compose.yml
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
      - 172.28.0.53 # Servidor DNS

networks: # Red Servicios
  mynetwork:
    ipam:
      config:
        - subnet: 172.28.0.0/24
          gateway: 172.28.0.254
```

### version
`version: '3.9'`

Especifica la versión de Docker Compose a utilizar. En este caso, se está utilizando la versión 3.9.

### services
`services:`

Define los servicios que se ejecutarán en los contenedores.

### dns
`dns:`

Es el nombre del servicio que se va a crear.

### container_name
`container_name: dns`

Define el nombre del contenedor que se creará a partir de este servicio.

### image
`image: ubuntu/bind9:latest`

Especifica la imagen de Docker que se utilizará para crear el contenedor. En este caso, se está utilizando la última versión de la imagen ubuntu/bind9.

### working_dir
`working_dir: /etc/bind`

Establece el directorio de trabajo dentro del contenedor.

### volumes
`volumes:`

Define los volúmenes que se montarán en el contenedor. Los volúmenes permiten compartir archivos entre el host y el contenedor.

- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf:/etc/bind/named.conf`
- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf.options:/etc/bind/named.conf.options`
- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf.local:/etc/bind/named.conf.local`
- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf.default-zones:/etc/bind/named.conf.default-zones`
- `/home/asir2/asir/github/sri/docker/dns/lib/:/var/lib/bind/`

siendo:

- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf:/etc/bind/named.conf`

  Monta el archivo `named.conf` del host en la ruta `/etc/bind/named.conf` del contenedor. Este archivo es la configuración principal de Bind9, el servidor DNS que se está utilizando.

- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf.options:/etc/bind/named.conf.options`

  Monta el archivo `named.conf.options` del host en la ruta `/etc/bind/named.conf.options` del contenedor. Este archivo contiene opciones globales para la configuración de Bind9.

- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf.local:/etc/bind/named.conf.local`

  Monta el archivo `named.conf.local` del host en la ruta `/etc/bind/named.conf.local` del contenedor. Este archivo se utiliza para definir zonas DNS locales.

- `/home/asir2/asir/github/sri/docker/dns/bind/named.conf.default-zones:/etc/bind/named.conf.default-zones`

  Monta el archivo `named.conf.default-zones` del host en la ruta `/etc/bind/named.conf.default-zones` del contenedor. Este archivo se utiliza para definir las zonas DNS predeterminadas.

- `/home/asir2/asir/github/sri/docker/dns/lib/:/var/lib/bind/`

  Monta el directorio `lib` del host en la ruta `/var/lib/bind/` del contenedor. Este directorio se utiliza para almacenar los archivos de datos de Bind9.

### ubuntu
`ubuntu:`

Es el nombre del servicio que se va a crear.

### container_name
`container_name: ubuntu`

Define el nombre del contenedor que se creará a partir de este servicio.

### image
`image: ubuntu:latest`

Especifica la imagen de Docker que se utilizará para crear el contenedor. En este caso, se está utilizando la última versión de la imagen de Ubuntu.

### working_dir
`working_dir: /home`

Establece el directorio de trabajo dentro del contenedor.

### volumes
`volumes:`

Define los volúmenes que se montarán en el contenedor. Los volúmenes permiten compartir archivos entre el host y el contenedor.

- `/home/asir2/asir/asir2/sri/ubuntu/home:/home`

  Monta el directorio `home` del host en la ruta `/home` del contenedor.

### networks
`networks:`

Define las redes a las que se conectará el contenedor. En este caso, el contenedor se conectará a la red "mynetwork".

### ipv4_address
`ipv4_address: 172.28.0.209`

Especifica la dirección IPv4 que se asignará al contenedor en la red "mynetwork".

### stdin_open
`stdin_open: true`

Mantiene el STDIN abierto incluso si no está adjunto. Esto puede ser útil para interactuar con el contenedor.

### tty
`tty: true`

Asigna una pseudo-TTY o terminal dentro del nuevo contenedor. Esto puede ser útil para interactuar con el contenedor.

### restart
`restart: on-failure`

Define la política de reinicio del contenedor. En este caso, el contenedor se reiniciará si se produce un fallo.

### dns
`dns:`

Define el servidor DNS que utilizará el contenedor. En este caso, se está utilizando el servidor DNS en la dirección IP `172.28.0.53`.

### networks
`networks:`

Define las redes a las que se conectará el contenedor. En este caso, el contenedor se conectará a la red "mynetwork".

### ipv4_address
`ipv4_address: 172.28.0.53`

Especifica la dirección IPv4 que se asignará al contenedor en la red "mynetwork".

### ports
`ports:`

Define los puertos que se expondrán en el contenedor. En este caso, se expone el puerto 53 en UDP.

### expose
`expose:`

Especifica los puertos que se expondrán en el contenedor sin publicarlos al host.

### restart
`restart: on-failure`

Define la política de reinicio del contenedor. En este caso, el contenedor se reiniciará si se produce un fallo.

### networks (fuera de services)
`networks:`

Define las redes que se crearán. En este caso, se creará la red "mynetwork".

### ipam
`ipam:`

Define la configuración de IPAM (IP Address Management) para la red.

### config
`config:`

Define la configuración de la red. En este caso, se establece la subred y la puerta de enlace.