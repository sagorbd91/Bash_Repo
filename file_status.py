#!/bin/bash
echo -n "Enter file name: "
read fname
if [ ! -e $fname ]
then
    echo "Enter file name not exists"
fi

echo "Enter command (cat, wc, sort, rm, ls):"
read cmd

case $cmd in 
    "cat"|"sort")
        $cmd $fname
        ;;
    "ls")
        $cmd -l $fname
        ;;
    "wc")
        $cmd $fname
esac
