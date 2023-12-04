# Ubuntu DHCP Server
## Instalación
Instalación del paquete `isc-dhcp-server`:
```console
sudo apt install isc-dhcp-server
```
## Configuración
### Paso 1
Primeramente, procederemos a establecer las 2
interfaces de red de nuestro `Ubuntu Server`, configurando una interfaz `enp0s3` con dirección IP
`dinámica` (mediante DHCP) y una interfaz `enp0s8` con dirección IP `estática` `172.16.0.1` con
máscara de subred 255.255.0.0. Además, también especificaremos las direcciones IP de
los servidores de resolución de nombres de dominio, en este caso los de Google, `8.8.8.8` y
`8.8.4.4`:
```console
sudo nano /etc/netplan/00-install-config.yaml
```
*00-install-config.yaml*
```yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      dhcp4: true # Obtenemos la dirección IP por otro servidor DHCP
    enp0s8:
      dhcp4: no
      addresses: [172.16.0.1/16] # Dirección IP estática del servidor DHCP
      nameservers:
       addresses: # Servidores DNS a utilizar por dicha interfaz de red
        - 8.8.8.8
        - 8.8.4.4			
  version: 2
```
### Paso 2
Una vez establecida la configuración pertinente de nuestras interfaces de red de nuestro servidor DHCP, procederemos a aplicar dicha configuración mediante el comando:
```console
sudo netplan apply
```
A continuación, comprobaremos que dicha configuración se ha aplicado correctamente
verificando los valores de nuestras interfaces de red con el comando:
```yaml
ip a
```
```swift
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:2a:a7:27 brd ff:ff:ff:ff:ff:ff
    inet 10.0.9.163/24 brd 10.0.9.255 scope global dynamic enp0s3
       valid_lft 604701sec preferred_lft 604701sec
    inet6 fe80::a00:27ff:fe2a:a727/64 scope link 
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:1b:40:46 brd ff:ff:ff:ff:ff:ff
    inet 172.16.0.1/16 brd 172.16.255.255 scope global enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe1b:4046/64 scope link 
       valid_lft forever preferred_lft forever
```
### Paso 3
Ahora, procederemos a configurar nuestro servicio DHCP. Para ello, mediante
el comando:
```console
sudo nano /etc/default/isc-dhcp-server
```
accederemos al archivo `isc-dhcp-server` y definiremos la interfaz de red por la cual
serviremos las direcciones IP a nuestros clientes DHCP, en este caso la interfaz `enp0s8`:

*isc-dhcp-server*
```yaml
# Defaults for isc-dhcp-server (sourced by /etc/init.d/isc-dhcp-server)

# Path to dhcpd's config file (default: /etc/dhcp/dhcpd.conf).
#DHCPDv4_CONF=/etc/dhcp/dhcpd.conf
#DHCPDv6_CONF=/etc/dhcp/dhcpd6.conf

# Path to dhcpd's PID file (default: /var/run/dhcpd.pid).
#DHCPDv4_PID=/var/run/dhcpd.pid
#DHCPDv6_PID=/var/run/dhcpd6.pid

# Additional options to start dhcpd with.
#	Don't use options -cf or -pf here; use DHCPD_CONF/ DHCPD_PID instead
#OPTIONS=""

# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
#	Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACESv4="enp0s8"
INTERFACESv6=""
```
### Paso 4
A continuación, mediante el comando:
```console
sudo nano /etc/dhcp/dhcpd.conf
```
accederemos al archivo `dhcpd.conf` y estableceremos la configuración de la red a la cuál
pertenecerán nuestros clientes DHCP:
```yaml
# dhcpd.conf
#
# Sample configuration file for ISC dhcpd
#
# Attention: If /etc/ltsp/dhcpd.conf exists, that will be used as
# configuration file instead of this file.
#

# option definitions common to all supported networks...
#option domain-name "example.org";
#option domain-name-servers ns1.example.org, ns2.example.org;

default-lease-time 600;
max-lease-time 7200;

# The ddns-updates-style parameter controls whether or not the server will
# attempt to do a DNS update when a lease is confirmed. We default to the
# behavior of the version 2 packages ('none', since DHCP v2 didn't
# have support for DDNS.)
ddns-update-style none;

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.
authoritative;

# Use this to send dhcp log messages to a different log file (you also
# have to hack syslog.conf to complete the redirection).
#log-facility local7;

# No service will be given on this subnet, but declaring it helps the 
# DHCP server to understand the network topology.

#subnet 10.152.187.0 netmask 255.255.255.0 {
#}

# This is a very basic subnet declaration.

#subnet 10.254.239.0 netmask 255.255.255.224 {
#  range 10.254.239.10 10.254.239.20;
#  option routers rtr-239-0-1.example.org, rtr-239-0-2.example.org;
#}

# This declaration allows BOOTP clients to get dynamic addresses,
# which we don't really recommend.

#subnet 10.254.239.32 netmask 255.255.255.224 {
#  range dynamic-bootp 10.254.239.40 10.254.239.60;
#  option broadcast-address 10.254.239.31;
#  option routers rtr-239-32-1.example.org;
#}

# A slightly different configuration for an internal subnet.
#subnet 10.5.5.0 netmask 255.255.255.224 {
#  range 10.5.5.26 10.5.5.30;
#  option domain-name-servers ns1.internal.example.org;
#  option domain-name "internal.example.org";
#  option subnet-mask 255.255.255.224;
#  option routers 10.5.5.1;
#  option broadcast-address 10.5.5.31;
#  default-lease-time 600;
#  max-lease-time 7200;
#}

subnet 172.16.0.0 netmask 255.255.0.0 {
   range 172.16.0.2 172.16.0.254;
   option subnet-mask 255.255.0.0;
   option broadcast-address 172.16.255.255;
   option routers 172.16.0.1;
   option domain-name-servers 8.8.8.8, 8.8.4.4;
   option domain-name "router";
}

# Hosts which require special configuration options can be listed in
# host statements.   If no address is specified, the address will be
# allocated dynamically (if possible), but the host-specific information
# will still come from the host declaration.

#host passacaglia {
#  hardware ethernet 0:0:c0:5d:bd:95;
#  filename "vmunix.passacaglia";
#  server-name "toccata.example.com";
#}

# Fixed IP addresses can also be specified for hosts.   These addresses
# should not also be listed as being available for dynamic assignment.
# Hosts for which fixed IP addresses have been specified can boot using
# BOOTP or DHCP.   Hosts for which no fixed address is specified can only
# be booted with DHCP, unless there is an address range on the subnet
# to which a BOOTP client is connected which has the dynamic-bootp flag
# set.
#host fantasia {
#  hardware ethernet 08:00:07:26:c0:a5;
#  fixed-address fantasia.example.com;
#}
host mario {
    hardware ethernet 08:00:27:87:06:55
    fixed-address 172.16.0.5
}

# You can declare a class of clients and then do address allocation
# based on that.   The example below shows a case where all clients
# in a certain class get addresses on the 10.17.224/24 subnet, and all
# other clients get addresses on the 10.0.29/24 subnet.

#class "foo" {
#  match if substring (option vendor-class-identifier, 0, 4) = "SUNW";
#}

#shared-network 224-29 {
#  subnet 10.17.224.0 netmask 255.255.255.0 {
#    option routers rtr-224.example.org;
#  }
#  subnet 10.0.29.0 netmask 255.255.255.0 {
#    option routers rtr-29.example.org;
#  }
#  pool {
#    allow members of "foo";
#    range 10.17.224.10 10.17.224.250;
#  }
#  pool {
#    deny members of "foo";
#    range 10.0.29.10 10.0.29.230;
#  }
#}

```
### Paso 5
Una vez establecida toda la configuración necesaria para el correcto funcionamiento de nuestro
servicio DHCP, lo reiniciaremos mediante el comando:
```yaml
sudo service isc-dhcp-server restart
```
y a continuación comprobaremos su inicialización mediante el comando:
```yaml
sudo service isc-dhcp-server status
```
```swift
● isc-dhcp-server.service - ISC DHCP IPv4 server
     Loaded: loaded (/lib/systemd/system/isc-dhcp-server.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2023-12-04 14:54:00 UTC; 15min ago
       Docs: man:dhcpd(8)
   Main PID: 691 (dhcpd)
      Tasks: 4 (limit: 4595)
     Memory: 5.6M
     CGroup: /system.slice/isc-dhcp-server.service
             └─691 dhcpd -user dhcpd -group dhcpd -f -4 -pf /run/dhcp-server/dhcpd.pid -cf /etc/dhcp/dhcpd.conf enp0s8

dic 04 14:54:00 router dhcpd[691]: For info, please visit https://www.isc.org/software/dhcp/
dic 04 14:54:00 router dhcpd[691]: Config file: /etc/dhcp/dhcpd.conf
dic 04 14:54:00 router dhcpd[691]: Database file: /var/lib/dhcp/dhcpd.leases
dic 04 14:54:00 router dhcpd[691]: PID file: /run/dhcp-server/dhcpd.pid
dic 04 14:54:00 router dhcpd[691]: Wrote 2 leases to leases file.
dic 04 14:54:00 router dhcpd[691]: Listening on LPF/enp0s8/08:00:27:1b:40:46/172.16.0.0/16
dic 04 14:54:00 router dhcpd[691]: Sending on   LPF/enp0s8/08:00:27:1b:40:46/172.16.0.0/16
dic 04 14:54:00 router dhcpd[691]: Sending on   Socket/fallback/fallback-net
dic 04 14:54:00 router dhcpd[691]: Server starting service.
```
## Verificación
### Configuración de red
En un cliente DHCP, visualizamos su cofiguración de red con el comando:
```yaml
ip a
```
```swift
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:87:09:39 brd ff:ff:ff:ff:ff:ff
    inet 172.16.0.2/16 brd 172.16.255.255 scope global dynamic noprefixroute enp0s3
       valid_lft 306sec preferred_lft 306sec
    inet6 fe80::ca8a:89d5:8d2:1bdf/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: enp0s8: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 08:00:27:61:42:78 brd ff:ff:ff:ff:ff:ff

```
Ahora, en el cliente DHCP con una configuración estática, haremos lo mismo:
```swift
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:87:06:55 brd ff:ff:ff:ff:ff:ff
    inet 172.16.0.5/16 brd 172.16.255.255 scope global dynamic noprefixroute enp0s3
       valid_lft 306sec preferred_lft 306sec
    inet6 fe80::ca8a:89d5:9d6:1bdf/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: enp0s8: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 08:00:27:48:82:31 brd ff:ff:ff:ff:ff:ff

```
### Wireshark
Ahora, para verificar que nuestro servicio DHCP funciona correctamente, monitorizaremos el tráfico `UDP` de nuestra interfaz de red por DHCP en nuestro client DHCP. Para ello, mediante el comando:
```console
sudo dhclient -r
```
liberaremos nuestra dirección IP por DHCP obtenida con anterioridad.

A continuación, con el comando:
```console
sudo tshark -i enp0s3 -f "udp port 67 or udp port 68" -Y "bootp"
```
procederemos a monitorizar el tráfico UDP por los puertos `67` y `68` (ambos DHCP) en la interfaz `enp0s3`.

Por último, mediante el comando:
```console
sudo dhclient
```
solicitaremos una nueva dirección IP a nuestro servidor DHCP, obteniendo así los paquetes deseados que verifican el correcto intercambio de paquetes DHCP entre nuestro cliente y servidor DHCP:
```swift
Running as user "root" and group "root". This could be dangerous.
Capturing on 'enp0s3'
 ** (tshark:4128) 11:49:15.510120 [Main MESSAGE] -- Capture started.
 ** (tshark:4128) 11:49:15.510188 [Main MESSAGE] -- File: "/tmp/wireshark_enp0s32NV9E2.pcapng"
    1 0.000000000      0.0.0.0 → 255.255.255.255 DHCP 342 DHCP Discover - Transaction ID 0x3e707761
    2 0.001078785  172.16.0.1 → 172.16.0.3  DHCP 342 DHCP Offer    - Transaction ID 0x3e707761
    3 0.002012963      0.0.0.0 → 255.255.255.255 DHCP 342 DHCP Request  - Transaction ID 0x3e707761
    4 0.006534574  172.16.0.1 → 172.16.0.3  DHCP 342 DHCP ACK      - Transaction ID 0x3e707761
```
A continuación, haremos lo mismo con el cliente DHCP con configuración estática:
```swift
Running as user "root" and group "root". This could be dangerous.
Capturing on 'enp0s3'
 ** (tshark:4402) 11:57:46.066735 [Main MESSAGE] -- Capture started.
 ** (tshark:4402) 11:57:46.066799 [Main MESSAGE] -- File: "/tmp/wireshark_enp0s3O86GF2.pcapng"
    1 0.000000000      0.0.0.0 → 255.255.255.255 DHCP 342 DHCP Discover - Transaction ID 0x2075a26b
    2 1.001796614  172.16.0.1 → 172.16.0.5  DHCP 342 DHCP Offer    - Transaction ID 0x2075a26b
    3 1.002397813      0.0.0.0 → 255.255.255.255 DHCP 342 DHCP Request  - Transaction ID 0x2075a26b
    4 1.019236179  172.16.0.1 → 172.16.0.5  DHCP 342 DHCP ACK      - Transaction ID 0x2075a26b

```

