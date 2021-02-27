#!/bin/bash
# by this program you are not passing anything to the funtion and we are getting no output
draw_line()
{
    count=50
    cntr=1
    while [ $cntr -le $count ]
    do
        echo -n "-"
        cntr=`expr $cntr + 1`
    done
    echo
}

echo "Multiplication Table"
draw_line
echo -n "Enter number:"
read num

while [ $num -ne 0 ]
do
    cntr=1
    iters=10
    while [ $cntr -le $iters ]
    do
        res=`expr $num \* $cntr`
        printf "%3d * %2d = %3d\n" $num $cntr $res
        cntr=`expr $cntr + 1`
    done
    draw_line
    echo -n "Enter Number: "
    read num
done
