#!/bin/sh
alias time='/usr/bin/time'
a=10000
f="rand"

while [ $a -lt 990001 ]
do
   j=$f$a".txt" 
   echo $a $j
   echo $a >> bubbletimes.txt
   { time ./a.out $a $j 1 ; } 2>>bubbletimes.txt
   a=`expr $a + 5000`
done
