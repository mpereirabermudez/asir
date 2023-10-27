#!/bin/bash

stty -echo # Deshabilitación de la entrada de texto por teclado

# Función de impresión del título inicial
function init_title() {
    echo -e "\n\n"
    echo "███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗██████╗ ";
    echo "████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗";
    echo "██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║██║  ██║";
    echo "██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██║  ██║";
    echo "██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██████╔╝";
    echo "╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ";
    echo "                                                                                    ";                  
}

# Función de impresión del titulo final
function  end_title() {
    echo -e "\n"
    echo " ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗";
    echo "██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║";
    echo "██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║";
    echo "██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝";
    echo "╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗";
    echo " ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝";
    echo "                                                               ";
}

# Función de generación de un dígito aleatorio entre 0 y 9
function sys_random() {
    echo $(($RANDOM%10))
}

# Función de animación del título inicial
function title_animation() {
    local i=0 # Inicialización de la variable de control del bucle
    for (( i=1; i<=${2}; i++ ))
    do
        echo -ne "${1}|${reset}"
        sleep ${3}
    done
}

# Función que pide al usuario un dígito entre 0 y 9 y verifica que lo es
function user_prompt() {
    read -n1 -rep "${purple}[${reset}${white}${1}${reset}${purple}] Introduce un dígito del ${white}0${reset} ${purple}al${reset} ${white}9${reset}${purple}:${reset} " user_digit$1
    local digit="user_digit${1}" # Dígito introducido por el usuario en variable local para evitar conflictos con la variable global

    # Bucle que se ejecuta mientras el dígito introducido por el usuario no sea un dígito entre 0 y 9
    while ! [[ ${!digit} =~ ^[0-9]$ ]]
    do
        read -n1 -rep "${red}[!] Valor no admitido!${reset} ${purple}Introduce un dígito del ${white}0${reset} ${purple}al${reset} ${white}9${reset}${purple}:${reset} " user_digit$1
    done
    user_num="$user_num${!digit}  " # Concatenación de los dígitos introducidos por el usuario
}

# Función que compara el dígito introducido por el usuario con el dígito aleatorio generado por el sistema
function sys_engine() {
    local user_digit=$1 # Dígito introducido por el usuario en variable local para evitar conflictos con la variable global
    local sys_digit=$2 # Dígito generado por el sistema en variable local para evitar conflictos con la variable global

    # Comprobación de si el dígito introducido por el usuario es igual al dígito generado por el sistema o no y generación de la pista correspondiente
    if [[ $user_digit == $sys_digit ]]
    then
        output="$output$O  "
    elif [[ $user_digit != $sys_digit ]]
    then
        n_X=0 # Número de dígitos correctos en valor pero incorrectos en posición
        local j=0 # Inicialización de la variable local de control del bucle
        for (( j=1; j<=$n_digit; j++ ))
        do
            local sys_digit_pos="sys_digit${j}" # Posición del dígito generado por el sistema en variable local para evitar conflictos con la variable global
            if [[ $user_digit == ${!sys_digit_pos} ]] 
            then
                n_X=$(($n_X+1)) # Incremento del número de dígitos correctos en valor pero incorrectos en posición
            fi
        done
        if [[ $n_X -ne 0 ]]
        then
            output="$output$X  "  
        else
            output="$output$g  "
        fi
    fi
}

init_title # Llamada a la función de impresión del título inicial                                                                              

#Colores y estilos
green=$'\001\033[1;92m\002' # Color verde
yellow=$'\001\033[1;93m\002' # Color amarillo 
red=$'\001\033[1;91m\002' # Color rojo
purple=$'\001\033[1;95m\002' # Color morado
cyan=$'\001\033[1;96m\002' # Color cian
white=$'\001\033[1;97m\002' # Color blanco
reset=$'\001\033[0m\002' # Reset de colores
italic=$'\001\033[3m\002' # Itálica
normal=$'\001\033[m\002' # Normal

echo -ne "\n\n${yellow}Cargando${reset}"
title_animation ${yellow} 76 0.006
stty echo # Habilitación de la entrada de texto por teclado
echo -e "\n"
read -n1 -rep "${purple}Número de dígitos a generar:${reset} " n_digit # Número de dígitos a generar
while [[ -z $n_digit ]]
do
    echo -e "\n"
    read -n1 -rep "${red}[!] Valor no admitido!${reset} ${purple}Número de dígitos a generar:${reset} " n_digit
done
stty -echo # Deshabilitación de la entrada de texto por teclado
echo -ne "\n${yellow}Generando${reset} ${white}$n_digit${reset} ${yellow}números aleatorios${reset}"
title_animation ${yellow} 54 0.005

sys_num="" # Inicialización de la variable que almacena el número total generado por el sistema

# Bucle para la generación de los dígitos aleatorios del sistema y sus respectivos símbolos de incógnita
for (( i=1; i<=$n_digit; i++ ))
do
    sys_digit="sys_digit${i}" # Dígito generado por el sistema
    declare "$sys_digit"=$(sys_random) # Declaración como variable independiente de cada uno de los dígitos generados por el sistema 
    sys_num="${sys_num}${!sys_digit}  " # Número generado por el sistema 
    num_symbol+="?  " # Símbolo de incógnita por cada dígito generado
done
echo $sys_num > sys_num.txt # Almacenamiento del número generado por el sistema en un fichero de texto por si se quisiera consultar posteriormente
echo -ne "\n\n\t\t${white}$num_symbol${reset}\n" # Impresión por pantalla de los símbolos de incógnita

# Símbolos de pista
O="${green}O${reset}" # Dígito correcto
X="${yellow}X${reset}" # Dígito correcto en valor pero incorrecto en posición
g=$(echo -e "${red}-${reset}") # Dígito incorrecto en valor y posición

intentos=0 # Número de intentos del usuario

stty echo # Habilitación de la entrada de texto por teclado

# Bucle que se ejecuta mientras el número total generado por el sistema no sea igual al número total generado por el usuario
while [[ $sys_num != $user_num ]]
do
    echo -ne "\n"
    user_num="" # Inicialización de la variable que almacena los dígitos introducidos por el usuario
    # Bucle que pide al usuario los 4 dígitos
    for (( i=1; i<=$n_digit; i++ ))
    do 
        user_prompt $i # Llamada a la función que pide al usuario un dígito
    done
    
    output="" # Inicialización de la variable que almacena las pistas

    # Bucle que compara los dígitos introducidos por el usuario con los dígitos generados por el sistema
    for (( i=1; i<=$n_digit; i++ )) 
    do  
        user_digit="user_digit${i}" # Dígito introducido por el usuario
        sys_digit="sys_digit${i}"  # Dígito generado por el sistema
        sys_engine ${!user_digit} ${!sys_digit} $i # Llamada a la función que compara los 2 dígitos
    done

     # Limpieza de la pantalla
    intentos=$(($intentos+1)) # Incremento del número de intentos del usuario por vez intentada

    if [[ $sys_num != $user_num ]]
    then
        echo -e "\n\t\t$output" # Impresión de las pistas por pantalla
        echo -e "\t\t$user_num\n" # Impresión de los dígitos introducidos por el usuario por pantalla
        echo -e "$O: ${italic}Dígito correcto en valor y posición${normal}"
        echo -e "$X: ${italic}Dígito correcto en valor e incorrecto en posición${normal}"
        echo -e "$g: ${italic}Dígito incorrecto en valor y posición${normal}"
        # Impresión por pantalla de la palabra "intento" o "intentos" según el número de intentos del usuario
        if [[ $intentos -eq 1 ]]
        then
            echo -e "\n${white}Llevas${reset} ${cyan}$intentos${reset} ${white}intento, sigue intentándolo!${reset}\n"
        else
            echo -e "\n${white}Llevas${reset} ${cyan}$intentos${reset} ${white}intentos, sigue intentándolo!${reset}\n"
        fi
    fi
done

# Impresión por pantalla de la palabra "intento" o "intentos" según el número de intentos del usuario
if [[ $intentos -eq 1 ]]
then
    echo -e "\n${white}¡Enhorabuena! Has adivinado la combinación${reset}  ${green}${sys_num}${reset}${white}en${reset} ${cyan}$intentos${reset} ${white}intento.${reset}"
    end_title # Llamada a la función de impresión del título final
else
    echo -e "\n${white}¡Enhorabuena! Has adivinado la combinación${reset}  ${green}${sys_num}${reset}${white}en${reset} ${cyan}$intentos${reset} ${white}intentos.${reset}"
    end_title # Llamada a la función de impresión del título final
fi