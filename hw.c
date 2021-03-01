#include <stdio.h>
#include <math.h>

void swap(int v[], size_t k)
{
  long long int temp;
  temp = v[k];
  v[k] = v[k+1];
  v[k+1] = temp;
}

void sort(int v[], int size) 
{ 
    // int i, j, min_idx; 
    // for (i = 0; i < n-1; i++) 
    // {  
    //     min_idx = i; 
    //     for (j = i+1; j < n; j++) 
    //       if (arr[j] < arr[min_idx]) 
    //         min_idx = j;  
    //     swap(&arr[min_idx], &arr[i]); 
    // } 
  int i, j;
  for (i = 0; i < size; i++) {
    for (j = i - 1; j >= 0 && v[j] > v[j+1]; j++) {
      swap(v, j);
    }
  }
}

void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
} 

int main()
{
  // int arr[] = {3,24,4,75,7,1};
  // printArray(arr, 6);
  // selectionSort(arr, 6);
  // printArray(arr, 6);

  int arr[] = {5,4,3,2,1};
  printArray(arr, 5);
  sort(arr, 5);
  printArray(arr, 5);
  return 0;
}
