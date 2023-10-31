#!/bin/bash

function board() {
    echo -e "\t${white}|---|---|---|"
    echo -e "\t| ${reset}${purple}$pos1${reset} | ${purple}$pos2${reset} | ${purple}$pos3${reset}${white} |"
    echo -e "\t|---|---|---|"
    echo -e "\t| ${reset}${purple}$pos4${reset} | ${purple}$pos5${reset} | ${purple}$pos6${reset}${white} |"
    echo -e "\t|---|---|---|"
    echo -e "\t| ${reset}${purple}$pos7${reset} | ${purple}$pos8${reset} | ${purple}$pos9${reset}${white} |"
    echo -e "\t|---|---|---|${reset}"
}

white=$'\001\033[1;97m\002' # Color blanco
purple=$'\001\033[1;95m\002' # Color morado
reset=$'\001\033[0m\002' # Reset
italic=$'\001\033[3m\002' # Itálica
normal=$'\001\033[m\002' # Normal

for (( i=1; i<=9; i++ ))
do
    pos="pos${i}"
    declare "$pos"=$reset$italic$i$normal
    done

board

n=1
while [[ $n -ne 10 ]]
do
    if [[ $n -eq 1 || $n -eq 3 || $n -eq 5 || $n -eq 7 || $n -eq 9 ]]
    then
        read -n1 -rep $'\tJugador 1: ' n_pos # Número de posición
        while [[ $n_pos -lt 1 || $n_pos -gt 9 ]]
        do
            read -n1 -rep $'\tNúmero inválido!. Jugador 1: ' n_pos
        done
        symb="X"
    else
        read -n1 -rep $'\tJugador 2: ' n_pos # Número de posición
        while [[ $n_pos -lt 1 || $n_pos -gt 9 ]]
        do
            read -n1 -rep $'\tNúmero inválido!. Jugador 2: ' n_pos
        done
        symb="O"
    fi
    pos="pos${n_pos}"
    declare "$pos"="$symb"
    n=$(($n+1))
    clear
    board

    for (( j=1+${i}; i<=7+${i}; i+=3 ))


done 