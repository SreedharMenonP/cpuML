#!/bin/sh
alias time='/usr/bin/time'
a=10000
f="rand"

while [ $a -lt 990001 ]
do
   j=$f$a".txt" 
   echo $a $j
   touch $j  
   echo $a >> fileinput2.txt
   { time ./a.out $a $j 1 ; } 2>>fileinput2.txt 
   a=`expr $a + 5000`
done
