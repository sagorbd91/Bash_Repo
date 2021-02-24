#!/bin/bash
total=20
cntr=1
echo -n "Enter number of students present"
read pcount
while [ $cntr -le $total ]
do
    if [ $cntr -gt $pcount ]
    then
        echo "end of processing"
        break
    fi
    echo -n "Processing for student $cntr "

    echo "......Done"
    cntr=`expr $cntr + 1`
done
