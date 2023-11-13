# Examen SRI Docker DNS

## 1) Explica métodos para 'abrir' una consola/shell a un contenedor que se está ejecutando.
- Terminal: mediante el comando:
```console
docker -exec -it <contenedor> bash
``````
- Visual Studio Code: una vez instalado el plugin de Docker, en el apartado de la lista de contenedores, hacemos click derecho encima de una contenedor activo y seleccionamos la opción de "Attach Shell".
### 2)  En el contenedor anterior, con que opciones tiene que haber sido arrancado para poder interactuar con las entradas y salidas del contenedor?
`-t:` mantiene la entrada estándar abierta.

`-i:` asigna una pseudoterminal.
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
Tenemos que especificar la dirección IP del contenedor en el apartado de al red.
## 5) ¿Que comando de consola puedo usar para saber las ips de los contenedores anteriores? Filtra todo lo que puedas la salida. El comando no es "ip a", tiene que ser desde fuera del contenedor.
- Dirección IP de un contenedor activo en específico:
```yaml
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <contenedor>
```
- Direcciones IP de todos los contenedores activos:
```yaml
docker network inspect -f '{{range $key, $value := .Containers}}{{if $value.Name}}{{.IPv4Address}}{{end}}{{end}}' docker_mynetwork
```
## 6) ¿Cual es la funcionalidad del apartado "ports" en docker compose?
El apartado `ports` en Docker Compose se utiliza para exponer los puertos de un contenedor en el host.

Cuando se define un servicio en `Docker Compose`, se puede especificar una lista de puertos que el contenedor expone y que se pueden acceder desde el host. La sintaxis para definir los puertos es `<puerto_host>:<puerto_contenedor>/<protocolo>`. Por ejemplo, si se desea exponer el puerto 80 del contenedor en el puerto 8080 del host, se puede utilizar la siguiente definición:

```yaml
services:
  httpd:
    image: httpd:latest
    ports:
      - "8080:80"
```

En el ejemplo anterior, el servicio `httpd` utiliza la última imagen de 'httpd' y expone el puerto `80` del contenedor en el puerto `8080` del host. 

La opción `ports` también se puede utilizar para exponer puertos `UDP` en lugar de `TCP`, especificando el protocolo en la definición del puerto. Por ejemplo, para exponer el puerto `53 UDP` del contenedor en el puerto `53 UDP` del host, se puede utilizar la siguiente definición:

```yaml
services:
  dns:
    image: ubuntu/bind9:latest
    ports:
      - "53:53/udp"
```

En este caso, el servicio `dns` utiliza la imagen de Ubuntu con Bind9 y expone el puerto 53 UDP del contenedor en el puerto 53 UDP del host.
## 7) ¿Para que sirve el registro CNAME? Pon un ejemplo
El registro `CNAME` se utiliza para crear un alias de un nombre de dominio a otro nombre de dominio. Esto es útil cuando se desea que un nombre de dominio tenga varios nombres alternativos que apunten al mismo servidor:
```yaml
ejemplo.com.      IN  A      8.8.8.8
www.ejemplo.com.  IN  CNAME  ejemplo.com.
```
## 8) ¿Como puedo hacer para que la configuración de un contenedor DNS no se borre si creo otro contenedor?
Se pueden crear volúmenes que contengan el contenido mapeado desde nuestro contenedor docker, es decir, la configuración básica del DNS, a nuestro equipo local:
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
De esta forma, al eliminar un contenedor (buena práctica por cierto) al terminar su uso, podemos recuperar el contenido mapeado del mismo utilizando los mismo volúmenes. 
## 9) Añade una zona tiendadeelectronica.int en tu docker DNS que tenga:
    a) www a la IP 172.16.0.1
    b) owncloud sea un CNAME de www
    c) un registro de texto con el contenido "1234ASDF"
    d)Comprueba que todo funciona con el comando "dig y muestra en los logs que el servicio arranca correctamente
### a), b) y c):
named.conf.local:
```yaml
zone "castelao.int" {
  type master;
  file "/var/lib/bind/db.castelao.int";
  allow-query {
    any;
    };
  };

zone "tiendadeelectronica.int" {
  type master;
  file "/var/lib/bind/db.tiendadeelectronica.int";
  allow-query {
    any;
    };
  };
```
db.tiendaelectronica.int:
```yaml
$TTL 38400	; 10 hours 40 minutes
@   IN SOA	ns.tiendadeelectronica.int. mario.tiendadeelectronica.int. (
        10000002   ; serial
        10800      ; refresh (3 hours)
        3600       ; retry (1 hour)
        604800     ; expire (1 week)
        38400      ; minimum (10 hours 40 minutes)
        )
; Server name
@		    IN      NS	    ns.tiendadeelectronica.int.
; Addresses
ns			IN		a		172.28.0.53
www         IN      A       172.16.0.1
owncloud    IN      CNAME   www
;Text record
texto       IN      TXT     "1234ASDF"
```
### d)
Logs de arranque del servicio `bind9`:
```yaml
Starting named...
exec /usr/sbin/named -u "bind" "-g" ""
13-Nov-2023 15:55:03.506 starting BIND 9.18.18-0ubuntu0.23.04.1-Ubuntu (Extended Support Version) <id:>
13-Nov-2023 15:55:03.506 running on Linux x86_64 6.1.0-12-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.52-1 (2023-09-07)
13-Nov-2023 15:55:03.506 built with  '--build=x86_64-linux-gnu' '--prefix=/usr' '--includedir=${prefix}/include' '--mandir=${prefix}/share/man' '--infodir=${prefix}/share/info' '--sysconfdir=/etc' '--localstatedir=/var' '--disable-option-checking' '--disable-silent-rules' '--libdir=${prefix}/lib/x86_64-linux-gnu' '--runstatedir=/run' '--disable-maintainer-mode' '--disable-dependency-tracking' '--libdir=/usr/lib/x86_64-linux-gnu' '--sysconfdir=/etc/bind' '--with-python=python3' '--localstatedir=/' '--enable-threads' '--enable-largefile' '--with-libtool' '--enable-shared' '--disable-static' '--with-gost=no' '--with-openssl=/usr' '--with-gssapi=yes' '--with-libidn2' '--with-json-c' '--with-lmdb=/usr' '--with-gnu-ld' '--with-maxminddb' '--with-atf=no' '--enable-ipv6' '--enable-rrl' '--enable-filter-aaaa' '--disable-native-pkcs11' 'build_alias=x86_64-linux-gnu' 'CFLAGS=-g -O2 -ffile-prefix-map=/build/bind9-VMBSpu/bind9-9.18.18=. -flto=auto -ffat-lto-objects -fstack-protector-strong -Wformat -Werror=format-security -fdebug-prefix-map=/build/bind9-VMBSpu/bind9-9.18.18=/usr/src/bind9-1:9.18.18-0ubuntu0.23.04.1 -fno-strict-aliasing -fno-delete-null-pointer-checks -DNO_VERSION_DATE -DDIG_SIGCHASE' 'LDFLAGS=-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -Wl,-z,relro -Wl,-z,now' 'CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=2'
13-Nov-2023 15:55:03.506 running as: named -u bind -g
13-Nov-2023 15:55:03.506 compiled by GCC 12.3.0
13-Nov-2023 15:55:03.506 compiled with OpenSSL version: OpenSSL 3.0.8 7 Feb 2023
13-Nov-2023 15:55:03.506 linked to OpenSSL version: OpenSSL 3.0.8 7 Feb 2023
13-Nov-2023 15:55:03.506 compiled with libuv version: 1.44.2
13-Nov-2023 15:55:03.506 linked to libuv version: 1.44.2
13-Nov-2023 15:55:03.506 compiled with libxml2 version: 2.9.14
13-Nov-2023 15:55:03.506 linked to libxml2 version: 20914
13-Nov-2023 15:55:03.506 compiled with json-c version: 0.16
13-Nov-2023 15:55:03.506 linked to json-c version: 0.16
13-Nov-2023 15:55:03.506 compiled with zlib version: 1.2.13
13-Nov-2023 15:55:03.506 linked to zlib version: 1.2.13
13-Nov-2023 15:55:03.506 ----------------------------------------------------
13-Nov-2023 15:55:03.506 BIND 9 is maintained by Internet Systems Consortium,
13-Nov-2023 15:55:03.506 Inc. (ISC), a non-profit 501(c)(3) public-benefit 
13-Nov-2023 15:55:03.506 corporation.  Support and training for BIND 9 are 
13-Nov-2023 15:55:03.506 available at https://www.isc.org/support
13-Nov-2023 15:55:03.506 ----------------------------------------------------
13-Nov-2023 15:55:03.506 found 12 CPUs, using 12 worker threads
13-Nov-2023 15:55:03.506 using 12 UDP listeners per interface
13-Nov-2023 15:55:03.506 DNSSEC algorithms: RSASHA1 NSEC3RSASHA1 RSASHA256 RSASHA512 ECDSAP256SHA256 ECDSAP384SHA384 ED25519 ED448
13-Nov-2023 15:55:03.506 DS algorithms: SHA-1 SHA-256 SHA-384
13-Nov-2023 15:55:03.506 HMAC algorithms: HMAC-MD5 HMAC-SHA1 HMAC-SHA224 HMAC-SHA256 HMAC-SHA384 HMAC-SHA512
13-Nov-2023 15:55:03.506 TKEY mode 2 support (Diffie-Hellman): yes
13-Nov-2023 15:55:03.506 TKEY mode 3 support (GSS-API): yes
13-Nov-2023 15:55:03.506 config.c: option 'trust-anchor-telemetry' is experimental and subject to change in the future
13-Nov-2023 15:55:03.506 loading configuration from '/etc/bind/named.conf'
13-Nov-2023 15:55:03.510 reading built-in trust anchors from file '/etc/bind/bind.keys'
13-Nov-2023 15:55:03.510 looking for GeoIP2 databases in '/usr/share/GeoIP'
13-Nov-2023 15:55:03.510 using default UDP/IPv4 port range: [32768, 60999]
13-Nov-2023 15:55:03.510 using default UDP/IPv6 port range: [32768, 60999]
13-Nov-2023 15:55:03.510 listening on IPv4 interface lo, 127.0.0.1#53
13-Nov-2023 15:55:03.510 listening on IPv4 interface eth0, 172.28.0.53#53
13-Nov-2023 15:55:03.510 generating session key for dynamic DNS
13-Nov-2023 15:55:03.510 sizing zone task pool based on 7 zones
13-Nov-2023 15:55:03.510 none:99: 'max-cache-size 90%' - setting to 14187MB (out of 15763MB)
13-Nov-2023 15:55:03.510 obtaining root key for view _default from '/etc/bind/bind.keys'
13-Nov-2023 15:55:03.510 set up managed keys zone for view _default, file 'managed-keys.bind'
13-Nov-2023 15:55:03.510 configuring command channel from '/etc/bind/rndc.key'
13-Nov-2023 15:55:03.510 command channel listening on 127.0.0.1#953
13-Nov-2023 15:55:03.510 configuring command channel from '/etc/bind/rndc.key'
13-Nov-2023 15:55:03.510 command channel listening on ::1#953
13-Nov-2023 15:55:03.510 not using config file logging statement for logging due to -g option
13-Nov-2023 15:55:03.510 managed-keys-zone: loaded serial 6
13-Nov-2023 15:55:03.510 zone 255.in-addr.arpa/IN: loaded serial 1
13-Nov-2023 15:55:03.510 zone 127.in-addr.arpa/IN: loaded serial 1
13-Nov-2023 15:55:03.510 zone 0.in-addr.arpa/IN: loaded serial 1
13-Nov-2023 15:55:03.510 zone localhost/IN: loaded serial 2
13-Nov-2023 15:55:03.510 zone tiendadeelectronica.int/IN: loaded serial 10000002
13-Nov-2023 15:55:03.510 zone castelao.int/IN: loaded serial 10000002
13-Nov-2023 15:55:03.514 all zones loaded
13-Nov-2023 15:55:03.514 running
13-Nov-2023 15:55:03.554 managed-keys-zone: Key 20326 for zone . is now trusted (acceptance timer complete)
```
Salida del comando `dig`:
```yaml
root@cccea14cd4c2:/home# dig www.tiendadeelectronica.int               

; <<>> DiG 9.18.12-0ubuntu0.22.04.3-Ubuntu <<>> www.tiendadeelectronica.int
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 46859
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 6eebc167896a39c801000000655247e247ff0d5b5845b982 (good)
;; QUESTION SECTION:
;www.tiendadeelectronica.int.   IN      A

;; ANSWER SECTION:
www.tiendadeelectronica.int. 38400 IN   A       172.16.0.1

;; Query time: 0 msec
;; SERVER: 127.0.0.11#53(127.0.0.11) (UDP)
;; WHEN: Mon Nov 13 15:59:30 UTC 2023
;; MSG SIZE  rcvd: 100
```
## 10) Realiza el apartado 9 en la máquina virtual con DNS.
### a), b) y c):
named.conf.local
```yaml
//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";

zone "castelao.int" {
  type master;
  file "/var/lib/bind/db.castelao.int";
  allow-query {
    any;
    };
  };

zone "tiendadeelectronica.int" {
  type master;
  file "/var/lib/bind/db.tiendadeelectronica.int";
  allow-query {
    any;
    };
  };

logging {
    channel query.log {
        file "/var/log/named/query.log";
        severity debug 3;
    };
    category queries { query.log; };
};
```
db.tiendadeelectronica.int:
```yaml
$TTL 38400	; 10 hours 40 minutes
@   IN SOA	ns.tiendadeelectronica.int. mario.tiendadeelectronica.int. (
        10000002   ; serial
        10800      ; refresh (3 hours)
        3600       ; retry (1 hour)
        604800     ; expire (1 week)
        38400      ; minimum (10 hours 40 minutes)
        )
; Server name
@		    IN      NS	    ns.tiendadeelectronica.int.
; Addresses
ns			IN		a		172.28.0.53
www         IN      A       172.16.0.1
owncloud    IN      CNAME   www
;Text record
texto       IN      TXT     "1234ASDF"
```
### d)
Logs de arranque del servicio `bind9`:
```yaml
● named.service - BIND Domain Name Server
     Loaded: loaded (/lib/systemd/system/named.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2023-11-13 11:12:22 EST; 14s ago
       Docs: man:named(8)
    Process: 3124 ExecStart=/usr/sbin/named $OPTIONS (code=exited, status=0/SUCCESS)
   Main PID: 3125 (named)
      Tasks: 4 (limit: 6910)
     Memory: 4.9M
        CPU: 13ms
     CGroup: /system.slice/named.service
             └─3125 /usr/sbin/named -u bind

Nov 13 11:12:22 mario-VirtualBox named[3125]: zone castelao.int/IN: loaded serial 10000002
Nov 13 11:12:22 mario-VirtualBox named[3125]: zone tiendadeelectronica.int/IN: loaded serial 10000002
Nov 13 11:12:22 mario-VirtualBox named[3125]: zone 0.in-addr.arpa/IN: loaded serial 1
Nov 13 11:12:22 mario-VirtualBox named[3125]: zone 127.in-addr.arpa/IN: loaded serial 1
Nov 13 11:12:22 mario-VirtualBox named[3125]: zone 255.in-addr.arpa/IN: loaded serial 1
Nov 13 11:12:22 mario-VirtualBox named[3125]: zone localhost/IN: loaded serial 2
Nov 13 11:12:22 mario-VirtualBox named[3125]: all zones loaded
Nov 13 11:12:22 mario-VirtualBox named[3125]: running
Nov 13 11:12:22 mario-VirtualBox systemd[1]: Started BIND Domain Name Server.
Nov 13 11:12:22 mario-VirtualBox named[3125]: managed-keys-zone: No DNSKEY RRSIGs found for '.': success
```
Salida del comando `dig`:
```yaml
❯ dig @10.0.9.165 www.tiendadeelectronica.int

; <<>> DiG 9.18.19-1~deb12u1-Debian <<>> @10.0.9.165 www.tiendadeelectronica.int
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54929
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 7e8c1826afc416d60100000065524bb3fa4ae775e2f3b06f (good)
;; QUESTION SECTION:
;www.tiendadeelectronica.int.   IN      A

;; ANSWER SECTION:
www.tiendadeelectronica.int. 38400 IN   A       172.16.0.1

;; Query time: 0 msec
;; SERVER: 10.0.9.165#53(10.0.9.165) (UDP)
;; WHEN: Mon Nov 13 17:15:47 CET 2023
;; MSG SIZE  rcvd: 100
```
