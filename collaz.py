#!/bin/bash
echo "Enter a number: "
read num
while [ $num -ne 1 ]
do 
    echo -n "$num "
    rem=`expr $num % 2`
    if [ $rem -eq 0 ]
    then
        num=`expr $num / 2`
    else
        num=`expr $num \* 3 + 1`
    fi

done
echo " "  
