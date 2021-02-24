#!/bin/bash
total=20
cntr=1

absent1=5
absent2=10
absent3=15
absent4=18
echo -n "Enter number of students present"

while [ $cntr -le $total ]
do
    if [ $cntr -eq $absent1 -o $cntr -eq $absent2 -o $cntr -eq $absent3 -o $cntr -eq $absent4 ]
    then
        cntr=`expr $cntr + 1`
        continue
    fi
    echo -n "Processing for student $cntr "

    echo "......Done"
    cntr=`expr $cntr + 1`
done
