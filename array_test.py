#!/bin/bash
fruits=(apple banana orange mango) # array initialization

echo "All fruits: ${fruits[*]}"
echo "All fruits: ${fruits[@]}"
echo "Indicies of fruits: ${!fruits[*]}"  # indices will get and ! sign before the variable.

echo "number of fruits: ${#fruits[*]}" # numner of fruits will get # sign

total=${#fruits[*]}
echo $total


# How to print all fruits one by one with index.
index=0
while [ $index -lt $total ]
do
    echo "Fruits $index are ${fruits[$index]}"
    index=`expr $index + 1`
done


# Now another fruits wants to add in the array how to do that?
fruits[$total]="pine apple" # you can see the total contains all fruit item so we just add one element in total.

echo "All Fruits: ${fruits[*]}"
echo "number of fruits: ${#fruits[*]}" # numner of fruits will get # sign
total=${#fruits[*]}
index=0
while [ $index -lt $total ]
do
    echo "Fruits $index are ${fruits[$index]}"
    index=`expr $index + 1`
done





for fruit in ${fruits[*]}
do
    echo "$fruit"
done

#problem is that pine apple will be printed in different lines. it has more than one string. 
# how can we solve this issue?
# solution we can use the indices to get the indidces and print the result with indices.
for fruit in ${!fruits[*]}
do
    echo ${fruits[fruit]}
done

# we need to find specific fruit

echo "4th index of fruit ${fruits[4]}"

# how to find length of the particular fruit

echo "length of the specific fruit ${#fruits[4]}"


# =====================================================

# more checking

nums=(10 20 30 40 50)
num[5]=60
echo ${nums[*]} #print all
nums[10]=100
echo "sequence of numbers ${nums[*]}" #print all
echo "sequence of indices: ${!nums[*]}"
echo "number of elements: ${#nums[*]}"



# How to calculate total in array by for loop
sum=0
for num in ${nums[*]}
do
    sum=`expr $sum + $num`
done
echo "$sum"


# how to get lenth of array?
len_array=(10 30 46 34 23)
len=${#len_array[@]}
echo "Length of array is $len"
