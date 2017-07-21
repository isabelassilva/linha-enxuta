#!/bin/bash

frame="\x55\xaa\x30\x10\xn\xm\x0\xH\xH\xH\xt\xu\x0\xI\xI\xI\x0\xJ\xJ\xJ\xa3"

frame=${frame/n/$2}             # passo
frame=${frame/m/$3}             # modo
    X=$4
    XA=${X:2:2}
    XB=${X:4:2}
    XC=${X:6:2}
frame=${frame/H/$XA}            # byte1 de X
frame=${frame/H/$XB}            # byte2 de X
frame=${frame/H/$XC}            # byte3 de X
frame=${frame/t/$5}             # tempo
frame=${frame/u/$6}             # comparação
    Y="$7"
    YA=${Y:2:2}
    YB=${Y:4:2}
    YC=${Y:6:2}
frame=${frame/I/$YA}            # byte1 de Xmin
frame=${frame/I/$YB}            # byte2 de Xmin
frame=${frame/I/$YC}            # byte3 de Xmin
    Z="$8"
    ZA=${Z:2:2}
    ZB=${Z:4:2}
    ZC=${Z:6:2}
frame=${frame/J/$ZA}            # byte1 de Xmax
frame=${frame/J/$ZB}            # byte2 de Xmax
frame=${frame/J/$ZC}            # byte3 de Xmax

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

