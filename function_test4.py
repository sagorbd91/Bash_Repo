#!/bin/bash
sum_two_num1()
{
    n1=$1
    n2=$2
    sum=`expr $n1 + $n2`
    return $sum
        }

sum_two_num2()
{

    sum=`expr $1 + $2`
    totaol=$3
    eval $total=$sum
}

sum_two_num1 10 20
echo $?

sum_two_num2 100 200 total
echo $?


#========================================
sum_numbers()
{
    #count=$#
    echo "Argument: way 1: $@, way 2: $*"
    sum=0
    for val in $@
    do
        sum=`expr $sum + $val`
    done
    return $sum
        }


sum_numbers 10 20 30
echo $?

sum_numbers 10 20 30 40 
echo $?

sum_numbers 10 20 40 50 60
echo $?

#=============================


