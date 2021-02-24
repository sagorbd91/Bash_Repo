#!/bin/bash
echo "Multiplicatuion Table"
echo -n "Enter Number: "
read num

while [ $num -ne 0 ]
do
    cntr=1
    iters=10
    while [ $cntr -le $iters ]
    do
        res=`expr $num \* $cntr`
        printf "%3d * %2d = %3d\n" $num $cntr $res
        cntr=`expr $cntr + 1`
    done
    echo -n "Enter Number: "
    read num
done
