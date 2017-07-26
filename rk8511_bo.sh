#!/bin/bash

if [ "$2" = "0" ]; then
    if [ "$3" = "0" ]; then
        frame="\x55\xaa\x20\x00\xe1"

    elif [ "$3" = "1" ]; then
        frame="\x55\xaa\x20\x03\xde"

    elif [ "$3" = "2" ]; then
        frame="\x55\xaa\x20\x07\xda"

    elif [ "$3" = "3" ]; then
        frame="\x55\xaa\x20\x09\xd8"
    fi
elif [ "$2" = "1" ]; then
        frame="\x55\xaa\x20\x10\xd1"
fi

if [ "$1" = "0" ]; then
    echo -e $frame > /dev/ttyUSB0

elif [ "$1" = "1" ]; then
    echo -e $frame > /dev/ttyUSB1

elif [ "$1" = "2" ]; then
    echo -e $frame > /dev/ttyUSB2
fi