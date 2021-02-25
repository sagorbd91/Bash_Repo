#!/bin/bash

mixed_array=(10 hello world 30)
sum=`expr ${mixed_array[0] + ${mixed_array[3] }}`
echo $sum

# how could i club that particular word hello world?

mystr=${mixed_array[1]}" "${mixed_array[2]} 
echo "total number is $mystr"
