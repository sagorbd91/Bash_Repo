#!/bin/bash
num=5
res=1
while [ $num -ge 1 ]
do
    res=`expr $num \* $res`
    num=`expr $num - 1`
done
echo "Factorial is $res"
