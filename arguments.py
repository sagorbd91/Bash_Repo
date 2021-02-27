#!/bin/bash
count=$#
if [ $count -eq 0 ]
then
    echo "No arguments to sum: exiting"
    exit
fi

sum=0
for val in $@
do
    sum=`expr $sum + $val`
done
echo "Sum of numbers is $sum"

sum=0
cntr=1
while [ $cntr -le $count ]
do
    val=$1
    shift
    sum=`expr $sum + $val`
    cntr=`expr $cntr + 1`
done
echo "Sum of numbers is $sum"

