#!/bin/bash

frame="\x55\xaa\x30\x10\xn\xm\x0\x0\x61\xa8\x02\x0\x0\x0\x55\xf0\x0\x0\x6d\x60\xa3"

frame=${frame/n/$2}             # passo
frame=${frame/m/$3}             # modo

if [ "$1" = "0" ]; then
    echo -e $frame > /dev/ttyUSB0
    echo $frame
fi

if [ "$1" = "1" ]; then
    echo -e $frame > /dev/ttyUSB1
fi
if [ "$1" = "2" ]; then
    echo -e $frame > /dev/ttyUSB2
fi
