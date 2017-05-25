#!/bin/bash

# Atualização de Dados na Tela

if [ "$2" = "RX" ]; then

    if [ "$1" = "0" ];then
        ./com0rx &
        echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB0
    fi

    if [ "$1" = "1" ]; then
        ./com1rx &
        echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB1
    fi

    if [ "$1" = "2" ]; then
        ./com2rx &
        echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB2
    fi
fi

# Envio de Dados para à Carga

frame="\x55\xaa\x30\xMODO\x00\x0s\xA\xB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xC"

if [ "$2" = "TX" ]; then

    if [ "$3" = "V" ]; then
        frame=${frame/MODO/00}
    fi

    if [ "$3" = "I" ]; then
        frame=${frame/MODO/03}
    fi

    if [ "$3" = "P" ]; then
        frame=${frame/MODO/07}
    fi

    VALOR="$4"
    BYTE1=${VALOR:2:2}
    BYTE2=${VALOR:4:4}

    CRC="$5"
    CRC=${CRC:2:2}

    s="$6"

    frame=${frame/A/$BYTE1}
    frame=${frame/B/$BYTE2}
    frame=${frame/C/$CRC}
    frame=${frame/s/$s}

    if [ "$1" = "0" ]; then
        echo -e $frame > /dev/ttyUSB0
    fi
    if [ "$1" = "1" ]; then
        echo -e $frame > /dev/ttyUSB1
    fi
    if [ "$1" = "2" ]; then
        echo -e $frame > /dev/ttyUSB2
    fi

fi
