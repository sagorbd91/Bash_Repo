#!/bin/bash
cntr=1
while [ $cntr -le 10 ]
do
    echo -n "$cntr "
    cntr=`expr $cntr + 1`
done
echo " "
