#!/bin/bash

function ip_recon() {
    net_addr=$(ip a | awk '/inet /{print $2}' | grep -vE '^(127|172)\.' | cut -d "." -f1-3)
    echo -e "${red}[+]${reset} ${green}Network${reset} ${yellow}$net_addr.0/24${reset}\n"
    for (( i=1; i<=$1; i++ )) 
    do 
        ip_addr=${net_addr}.${i}
        ping -c1 -W1 "$ip_addr" &> /dev/null
        if [[ $? -eq 0 ]]
        then
            mac_addr=$(arp -an | grep "($ip_addr)" | awk '{print $4}')
            nmap -p22 -n -Pn "$ip_addr" | grep "22/tcp open" &> /dev/null
            if [[ $? -eq 0 ]] 
            then
                echo -e "\t${red}[!]${reset} ${green}Host${reset} ${yellow}$ip_addr${reset} ${green}at${reset} ${yellow}$mac_addr${reset} ${green}is up (ssh open)${reset}"
            else
                echo -e "\t${red}[!]${reset} ${green}Host${reset} ${yellow}$ip_addr${reset} ${green}at${reset} ${yellow}$mac_addr${reset} ${green}is up${reset}"
            fi
        fi
    done
}

#Colores y estilos
green=$'\001\033[1;92m\002' # Color verde
yellow=$'\001\033[1;93m\002' # Color amarillo 
red=$'\001\033[1;91m\002' # Color rojo
reset=$'\001\033[0m\002' # Reset de colores
italic=$'\001\033[3m\002' # Itálica
normal=$'\001\033[m\002' # Normal

echo "                                                                                                                           ";
echo "██╗██████╗     ██╗  ██╗ ██████╗ ███████╗████████╗    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗";
echo "██║██╔══██╗    ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝";
echo "██║██████╔╝    ███████║██║   ██║███████╗   ██║       ██║  ██║██║███████╗██║     ██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝ ";
echo "██║██╔═══╝     ██╔══██║██║   ██║╚════██║   ██║       ██║  ██║██║╚════██║██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝  ";
echo "██║██║         ██║  ██║╚██████╔╝███████║   ██║       ██████╔╝██║███████║╚██████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║   ██║   ";
echo "╚═╝╚═╝         ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ";
echo "                                                                                                                           ";
echo -e "${italic}Starting Active Host Discovery...${normal}\n"

if [[ -z $1 ]]
then
    ip_recon 254
    echo -e ""
else
    ip_recon $1
    echo -e ""
fi

