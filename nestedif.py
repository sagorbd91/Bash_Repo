#!/bin/bash
echo -n "Enter any number: "
read num
if [ $num -gt 0 ]
then
    echo "You have entered $num and is greater than zero"
else
    if [ $num -lt 0 ]
    then
        echo "You have entered $num is less than zero"
    else
        echo "you have entered zero"
    fi
fi
echo "End of statement"
