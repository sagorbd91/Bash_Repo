#!/bin/bash

# No input --> Output

myrandomnumber()
{
   num=$((RANDOM%100))
   echo $num
   return $num
   }

myrandomnumber
echo $?
