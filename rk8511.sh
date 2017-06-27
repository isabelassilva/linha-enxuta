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

frame="\x55\xaa\x30\xMODO\x00\xs\xA\xB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xC"

if [ "$2" = "TX" ]; then

    MODO="$3"

    CRC="$7"
    CRC=${CRC:2:2}

    frame=${frame/MODO/$MODO}
    frame=${frame/C/$CRC}

    if [ $MODO != "10" ]; then

        s="$4"

        VALOR="$5"
        BYTE1=${VALOR:2:2}
        BYTE2=${VALOR:4:4}

        frame=${frame/s/$s}
        frame=${frame/A/$BYTE1}
        frame=${frame/B/$BYTE2}
    fi

    if [ $MODO = "10" ]; then

        t="$4"
        m="$5"
        p="$6"

        frame=${frame/s/$t}
        frame=${frame/A/$m}
        frame=${frame/B/$p}
    fi

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
