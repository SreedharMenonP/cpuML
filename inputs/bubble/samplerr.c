#include <stdio.h>
#include <sched.h>
 
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
 
/* Function to print an array */
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    //printf("n");
}
 
// Driver program to test above functions
int main()
{
	struct timespec ts;
	int ret;
    int arr[] = {64, 34, 25, 12, 22, 11, 90,67,89,32,41,64, 34, 25, 12, 22, 11, 90,67,89,32,4164, 34, 25, 12, 22, 11, 90,67,89,32,4164, 34, 25, 12, 22, 11, 90,67,89,32,41,64, 34, 25, 12, 22, 11, 90,67,89,32,41,64, 34, 25, 12, 22, 11, 90,67,89,32,41,64, 34, 25, 12, 22, 11, 90,67,89,32,41,64, 34, 25, 12, 22, 11, 90,67,89,32,41};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    ret = sched_rr_get_interval(0, &ts);
    printf("Timeslice: %lu.%lu\n", ts.tv_sec, ts.tv_nsec);
    return 0;
}
