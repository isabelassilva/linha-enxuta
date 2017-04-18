#!/bin/bash

./test_rx &

echo -e "\x55\xaa\x00\x01" > /dev/ttyUSB1

