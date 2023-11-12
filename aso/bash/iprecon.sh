#!/bin/bash

# Script para realizar el reconocimiento de hosts activos en la red
# Autor: Mario Pereira aka DrDrunk3nst3in

function host() { # Comrpobamos si el host y puerto 22 estan activos
    if ping -c1 -W1 "$1" > /dev/null 2>&1 
    then
        mac_addr=$(arp -an | awk -v ip="($1)" '$2 == ip {print $4}') # Dirección MAC de cada host de la red
        if nmap -p22 -n -Pn "$1" | grep "22/tcp open" > /dev/null 2>&1 # Comprobamos si el puerto 22 (ssh) está abierto
        then
            echo -e "\t${red}[+]${reset} ${green}Host${reset} ${yellow}$1${reset} ${green}at${reset} ${yellow}$mac_addr${reset} ${green}is up (ssh open)${reset}"
        else
            echo -e "\t${red}[+]${reset} ${green}Host${reset} ${yellow}$1${reset} ${green}at${reset} ${yellow}$mac_addr${reset} ${green}is up${reset}" 
        fi
    fi
}

# Función para realizar el reconocimiento de hosts activos en la red
function ip_recon() {
    read net_addr msk_addr < <(ip a | awk '/inet /{split($2, msk, "/"); split(msk[1], net, "."); if (net[1] != 127 && net[1] != 172) {if (msk[2] == 24) {print net[1]"."net[2]"."net[3]".0" " " msk[2]} else if (msk[2] == 16) {print net[1]"."net[2]".0.0" " " msk[2]} else if (msk[2] == 8) {print net[1]".0.0.0" " " msk[2]}}}') # Dirección y máscara de red
    echo -e "${red}[+]${reset} ${cyan}Network${reset} ${yellow}${net_addr}/$msk_addr${reset}\n"
    i=j=k=0
    if [[ $msk_addr -eq 24 ]]
    then
        for (( k=1; k<=$1; k++ ))
        do
            {
            ip_addr=$(echo $net_addr | awk -v host24=$k '{split($1, ip, "."); {print ip[1]"."ip[2]"."ip[3]"."host24}}') # Dirección IP de cada host de la r
            host $ip_addr
            } &
        done
        wait
    elif [[ $msk_addr -eq 16 ]]
    then
        for (( j=0; j<=$1; j++ ))
        do
            for (( k=1; k<=$2; k++ ))
            do
                {
                ip_addr=$(echo $net_addr | awk -v host16=$j -v host24=$k '{split($1, ip, "."); {print ip[1]"."ip[2]"."host16"."host24}}') # Dirección IP de cada host de la red
                host $ip_addr
                } &
            done
            wait
        done
    elif [[ $msk_addr -eq 8 ]]
    then
        for (( i=0; i<=$1; i++ ))
        do
            for (( j=0; j<=$2; j++ ))
            do
                for (( k=1; k<=$3; k++ ))
                do
                    {
                    ip_addr=$(echo $net_addr | awk -v host8=$i -v host16=$j -v host24=$k '{split($1, ip, "."); {print ip[1]"."host8"."host16"."host24}}') # Dirección IP de cada host de la red
                    host $ip_addr
                    } &
                done
                wait
            done
        done
    fi 
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

if  [[ $1 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $1 ]] && [[ $2 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $2 ]] && [[ $3 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $3 ]] # Comprobamos si el argumento es un número entre 1 y 254
then
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
    if [[ $# -eq 0 ]]
    then
        ip_recon 254 254 254 # Por defecto se realizará el reconocimiento de todos los hosts de la red
        echo -e "\n${red}[!]${reset} ${cyan}Scan finished!${reset}\n"
    elif [[ $# -eq 1 ]]
    then
        ip_recon $1 # Se realizará el reconocimiento del número de hosts indicados
        echo -e "\n${red}[!]${reset} ${cyan}Scan finished!${reset}\n"
    elif [[ $# -eq 2 ]]
    then
        ip_recon $1 $2 # Se realizará el reconocimiento del número de hosts indicados
        echo -e "\n${red}[!]${reset} ${cyan}Scan finished!${reset}\n"
    elif [[ $# -eq 3 ]]
    then
        ip_recon $1 $2 $3 # Se realizará el reconocimiento del número de hosts indicados
        echo -e "\n${red}[!]${reset} ${cyan}Scan finished!${reset}\n"
    fi
elif ! ([[ $1 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $1 ]] && [[ $2 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $2 ]] && [[ $3 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || -z $3 ]])
then
    echo -e "${red}[!]${reset} ${yellow}$1${reset} ${cyan}is not a valid number${reset}"
    exit 1
fi