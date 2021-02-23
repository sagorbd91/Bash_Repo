#!/bin/bash
sum=0
for num in 10 15 14 9 20
do
    echo "Number is $num"
    sum=`expr $sum + $num`
done
echo "Sum of number is $sum"
