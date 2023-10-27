#!/bin/bash

n=0
while [[ $n -ne 9 ]]
do
    read -n1 -rep "Posición: " n_pos # Número de posición
    while ! [[ $n_pos =~ ^[1-9]$ ]]
    do
        read -n1 -rep "Número inválido!. Posición: " n_pos
    done
    
    read -n1 -rep "Símbolo: " simb # Símbolo
    while ! [[ $simb == "X" && $simb == "O" ]]
    do
        read -n1 -rep "Símbolo inválido!. Símbolo: " simb
    done
    n=$(($n+1))
    for (( i=1; i<=9; i++ ))
    do
        pos="pos${i}"
        if [[ $i -eq $n_pos ]]
        then
            declare "$pos"="$simb"
        else
            pos_e="${!pos}"
            if [[ $pos_e == "" || $pos_e == " " ]]
            then
                declare "$pos"=" "   
            fi
        fi
    clear    
    done
    
echo "|---|---|---|"
echo "| $pos1 | $pos2 | $pos3 |"
echo "|---|---|---|"
echo "| $pos4 | $pos5 | $pos6 |"
echo "|---|---|---|"
echo "| $pos7 | $pos8 | $pos9 |"
echo "|---|---|---|"

done