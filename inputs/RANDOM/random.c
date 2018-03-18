//Full Working Program
#include <stdio.h>
#include <stdlib.h>//required to use 'rand()'
#include <time.h>//required to use 'srand(time(NULL))'


int main (int argc, char *argv[])
{
srand(time(NULL));//required for "randomness"
 FILE *f = fopen(argv[2],"w+");
 int r,x,i;
 x  = strtol(argv[1], NULL, 0);
 for(i=0;i<x;i++)
{
 r=rand()%1000;//generate a number between 0 and 5
 fprintf(f,"%i\n",r);
 }
return 0;
}

