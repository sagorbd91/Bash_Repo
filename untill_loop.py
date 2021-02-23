#!/bin/bash
count=20
cntr=$count
until [ $cntr -lt 1 ]
do
    echo -n "$cntr "
    cntr=`expr $cntr - 1`
done
echo ""
