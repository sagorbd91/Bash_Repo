#!/bin/bash
echo -n "Enter a number 1: "
read num1
echo -n "Enter number 2: "
read num2
echo -n "Enter operator (+ for add, - for sub): "
read op

case $op in 
        +) res=`expr $num1 + $num2`
            #echo $res
            ;;
        -) res=`expr $num1 - $num2`
            #echo $res
            ;;
        *) echo "INvaild statement"
esac
echo "Result is $res"
