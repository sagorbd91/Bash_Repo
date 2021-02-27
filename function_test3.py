#!/bin/bash

# Fibonnacci series (0,1 or 1,1 )
# 1 1 --> initial value
# 1 1 2 3 5 8 .................. series
# n1 n2 --> initial value 
# sum we will calculate
# n1 become n2 and n2 become sum
# again sum will be produce
fibo_series()
{
   count=$1   # [count $1 is getting from a function ]
   n1=1
   n2=1
   echo -n "$n1 $n2 "
   cntr=1
   while [ $cntr -lt $count ]
   do
        sum=`expr $n1 + $n2`
        cntr=`expr $cntr + 1`
        echo -n "$sum "
        n1=$n2
        n2=$sum

    done
    echo
        }

fibo_series 10
