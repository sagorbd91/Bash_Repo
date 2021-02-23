#!/bin/bash
for((cntr=1;cntr <=5;cntr++))
do
    echo "$cntr"
    ls 
    pwd
    echo "============"
done

#============================

echo -n "Enter Number: "
read num
for((cntr=num;cntr >=1; cntr--))
do
    echo $cntr
done

