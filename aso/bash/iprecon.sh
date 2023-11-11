#!/bin/bash

# Script para realizar el reconocimiento de hosts activos en la red
# Autor: Mario Pereira aka DrDrunk3nst3in

# Función para realizar el reconocimiento de hosts activos en la red
function ip_recon() {
    read net_addr msk_addr < <(ip a | awk '/inet /{split($2, msk, "/"); split(msk[1], net, "."); if (net[1] != 127 && net[1] != 172) {print net[1]"."net[2]"."net[3]"." " " "/"msk[2]}}') # Dirección y máscara de red
    echo -e "${red}[+]${reset} ${green}Network${reset} ${yellow}${net_addr}0$msk_addr${reset}\n"
    for (( i=1; i<=$1; i++ )) 
    do 
        {
        ip_addr=${net_addr}${i} # Dirección IP de cada host de la red
        echo $ip_addr
        if ping -c1 -W1 "$ip_addr" > /dev/null 2>&1
        then
            mac_addr=$(arp -an | awk -v ip="($ip_addr)" '$2 == ip {print $4}') # Dirección MAC de cada host de la red
            if nmap -p22 -n -Pn "$ip_addr" | grep "22/tcp open" > /dev/null 2>&1 # Comprobamos si el puerto 22 (ssh) está abierto
            then
                echo -e "\t${red}[+]${reset} ${green}Host${reset} ${yellow}$ip_addr${reset} ${green}at${reset} ${yellow}$mac_addr${reset} ${green}is up (ssh open)${reset}"
            else
                echo -e "\t${red}[+]${reset} ${green}Host${reset} ${yellow}$ip_addr${reset} ${green}at${reset} ${yellow}$mac_addr${reset} ${green}is up${reset}" 
            fi
        fi
        } | cat &
    done
    wait
}

# Función para comprobar si los comandos necesarios están instalados
function cmd_check() {
    n_cmd=0 # Contador de comandos no instalados
    for (( i=1; i<=$#; i++ )) 
    do
        if ! command -v "${!i}" > /dev/null 2>&1 # Comprobamos si el comando está instalado
        then
            echo -e "${red}[!]${reset} ${yellow}${!i}${reset} ${green}is not installed${reset}"
            n_cmd=$((n_cmd+1)) # Se incrementa el contador de comandos no instalados
        fi
    done
    if [[ $n_cmd -ne 0 ]] # Si el contador de comandos no instalados es distinto de 0, se aborta el script
    then
        exit 1
    fi
}

# Colores y estilos
green=$'\001\033[1;92m\002' # Color verde
yellow=$'\001\033[1;93m\002' # Color amarillo 
red=$'\001\033[1;91m\002' # Color rojo
cyan=$'\001\033[1;96m\002' # Color cian
reset=$'\001\033[0m\002' # Reset de colores
italic=$'\001\033[3m\002' # Itálica
normal=$'\001\033[m\002' # Normal

if ! [[ $1 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $1 ]] # Comprobamos si el argumento es un número entre 1 y 254
then
    echo -e "${red}[!]${reset} ${yellow}$1${reset} ${cyan}is not a valid number${reset}"
    exit 1
fi

echo "                                                                                                                           ";
echo "██╗██████╗     ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗";
echo "██║██╔══██╗    ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝";
echo "██║██████╔╝    ███████║██║   ██║███████╗   ██║       ██║  ██║██║███████╗██║     ██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝ ";
echo "██║██╔═══╝     ██╔══██║██║   ██║╚════██║   ██║       ██║  ██║██║╚════██║██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝  ";
echo "██║██║         ██║  ██║╚██████╔╝███████║   ██║       ██████╔╝██║███████║╚██████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║   ██║   ";
echo "╚═╝╚═╝         ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ";
echo "                                                                                                                           ";

cmd_check ip arp ping nmap # Comprobamos si los comandos necesarios están instalados

echo -e "${italic}Starting Active Host Discovery...${normal}\n"

# Comprobamos si se ha pasado un argumento
if [[ -z $1 ]]
then
    ip_recon 254 # Por defecto se realizará el reconocimiento de todos los hosts de la red
    echo -e "\n${red}[!]${reset} ${cyan}Scan finished!${reset}\n"
else
    ip_recon $1 # Se realizará el reconocimiento del número de hosts indicados
    echo -e "\n${red}[!]${reset} ${cyan}Scan finished!${reset}\n"
fi