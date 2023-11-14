#!/bin/bash

# Script para realizar el reconocimiento de hosts activos en la red
# Autor: Mario Pereira aka DrDrunk3nst3in

# Función para realizar el reconocimiento de hosts activos en la red
function ip_recon() {
    read net_addr msk_addr localhost < <(ip a | awk '/inet /{split($2, msk, "/"); split(msk[1], net, "."); if (net[1] != 127 && net[1] != 172) {print net[1]"."net[2]"."net[3]".0" " " msk[2] " " net[1]"."net[2]"."net[3]"."net[4]}}') # Dirección y máscara de red
    echo -e "${red}[+] ${cyan}Network ${yellow}$net_addr/$msk_addr${reset}\n"
    for (( host=1; host<=$1; host++ ))
    do
        {
        IFS='.' read -a ip_parts <<< "$net_addr" # Separamos la dirección IP en 4 partes
        ip_addr="${ip_parts[0]}.${ip_parts[1]}.${ip_parts[2]}.$host" # Dirección IP de cada host de la red 
        if [[ $ip_addr != $localhost ]]
        then
            if ping -c1 -W1 "$ip_addr" > /dev/null 2>&1 
            then
                ttl=$(ping -c1 "$ip_addr" | awk '/ttl/ {print $1}') # TTL del paquete ICMP  
                if [[ $ttl -ge 1 && $ttl -le 64 ]]
                then
                    OS="Linux/Unix"
                elif [[ $ttl -ge 65 && $ttl -le 128 ]]
                then
                    OS="Windows"
                elif [[ $ttl -ge 129 && $ttl -le 255 ]]
                then
                    OS="Solaris/AIX"
                else
                    OS="Unknown"
                fi
                mac_addr=$(arp -an | awk -v ip="($ip_addr)" '$2 == ip {print $4}') # Dirección MAC del host
                if nmap -p22 --min-rate 5000 -n -Pn "$ip_addr" | grep -q 'open' # Comprobamos si el puerto 22 (ssh) está abierto
                then
                    echo -e "\t${red}[+] ${green}Host ${yellow}$ip_addr ${green}at ${yellow}$mac_addr ${green}running ${yellow}$OS ${green}with ${yellow}22/tcp open ssh${green} is ${yellow}UP${reset}"
                else
                echo -e "\t${red}[+] ${green}Host ${yellow}$ip_addr ${green}at ${yellow}$mac_addr ${green}running ${yellow}$OS ${green}is ${yellow}UP${reset}" 
                fi
            fi
        fi
        } &
    done
    wait
}

# Colores y estilos
green=$'\001\033[1;92m\002' # Color verde
yellow=$'\001\033[1;93m\002' # Color amarillo 
red=$'\001\033[1;91m\002' # Color rojo
cyan=$'\001\033[1;96m\002' # Color cian
reset=$'\001\033[0m\002' # Reset de colores
italic=$'\001\033[3m\002' # Itálica
normal=$'\001\033[m\002' # Normal

num_commands=0 # Contador de comandos no instalados
commands=("ip" "arp" "ping" "nmap") # Comandos necesarios para el script
for command in "${commands[@]}"
do
    if ! command -v "${command}" > /dev/null 2>&1 # Comprobamos si el comando está instalado
    then
        echo -e "${red}[!] ${yellow}$command ${green}is not installed${reset}"
        num_commands=$((num_commands+1)) # Se incrementa el contador de comandos no instalados
    fi
done
if [[ $num_commands -eq 0 ]] 
then
    if  [[ $1 =~ ^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-4])$ || $# -eq 0 ]] # Comprobamos si el parámetro es un número entre 1 y 254
    then
        echo -e "\n███╗   ██╗███████╗████████╗███████╗ ██████╗ █████╗ ███╗   ██╗";
        echo "████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║";
        echo "██╔██╗ ██║█████╗     ██║   ███████╗██║     ███████║██╔██╗ ██║";
        echo "██║╚██╗██║██╔══╝     ██║   ╚════██║██║     ██╔══██║██║╚██╗██║";
        echo "██║ ╚████║███████╗   ██║   ███████║╚██████╗██║  ██║██║ ╚████║";
        echo -e "╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ by DrDrunk3nst3in\n";

        # Comprobamos si se ha pasado un argumento
        if [[ $# -eq 0 ]]
        then
            ip_recon 254 # Por defecto se realizará el reconocimiento de todos los hosts de la red
            echo -e "\n${red}[!] ${cyan}Scan finished!${reset}\n"
        else
            ip_recon $1 # Se realizará el reconocimiento del número de hosts indicados
            echo -e "\n${red}[!] ${cyan}Scan finished!${reset}\n"
        fi
    else # Si el parámetro no es un número entre 1 y 254 o vacío, se aborta el script
        echo -e "${red}[!] ${yellow}$1 ${cyan}is not a valid number${reset}"
        exit 1
    fi
else # Si el contador de comandos no instalados es distinto de 0, se aborta el script
    exit 1
fi