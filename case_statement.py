#!/bin/bash
echo -n "Enter a number 1: "
read num1
echo -n "Enter number 2: "
read num2
echo -n "Enter operator (1 for add, 2 for sub): "
read op

case $op in 
        1) res=`expr $num1 + $num2`
            #echo $res
            ;;
        2) res=`expr $num1 - $num2`
            #echo $res
            ;;
        *) echo "INvaild statement"
esac
echo "Result is $res"
