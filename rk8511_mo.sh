#!/bin/bash

# Envio de Modos Operacionais

frame="\x55\xaa\x30\xMODO\x00\xJ\xJ\xJ\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCRC"

MODO="$2"
frame=${frame/MODO/$MODO}

VALOR="$3"
BYTE1=${VALOR:2:2}
BYTE2=${VALOR:4:2}
BYTE3=${VALOR:6:2}

frame=${frame/J/$BYTE1}
frame=${frame/J/$BYTE2}
frame=${frame/J/$BYTE3}

CRC="$4"
frame=${frame/CRC/$CRC}

if [ "$1" = "0" ]; then
    echo -e $frame > /dev/ttyUSB0

elif [ "$1" = "1" ]; then
    echo -e $frame > /dev/ttyUSB1

elif [ "$1" = "2" ]; then
    echo -e $frame > /dev/ttyUSB2
fi
