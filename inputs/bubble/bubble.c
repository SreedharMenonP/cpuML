/* C program for Merge Sort */
#include<stdlib.h>
#include<stdio.h>
int numbers[1000000];
 
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
// A function to implement bubble sort
void bubbleSort(int arr[], int n)
{
   int i, j;
   for (i = 0; i < n-1; i++)      
 
       // Last i elements are already in place   
       for (j = 0; j < n-i-1; j++) 
           if (arr[j] > arr[j+1])
              swap(&arr[j], &arr[j+1]);
}
 

/* Driver program to test above functions */
int main( int argc, char *argv[])
{   
    FILE *f = fopen(argv[2],"r+");
    int s = atoi(argv[1]);
     int n = 0, i = 0;
     // assuming there are only 5 numbers in the file

    while( fscanf(f, "%d", &n) > 0 ) // parse %d followed by ','
    {
        numbers[i++] = n;
    }

    fclose(f);



    //int arr[] = {12, 11, 13, 5, 6, 7};
    //int arr_size = sizeof(numbers)/sizeof(numbers[0]);
 
    //printf("Given array is \n");
    //printArray(numbers, arr_size);
 
    bubbleSort(numbers, s - 1);
 
    //printf("\nSorted array is \n");
    //printArray(arr, arr_size);
    return 0;
}

