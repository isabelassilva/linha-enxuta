#!/bin/bash

# Atualização de Dados na Tela

if [ "$1" = "0" ];then
    ./com0rx &
    echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB0

elif [ "$1" = "1" ]; then
    ./com1rx &
    echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB1

elif [ "$1" = "2" ]; then
    ./com2rx &
    echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB2

fi
