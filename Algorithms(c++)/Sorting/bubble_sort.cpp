// Bubble sort implementation using C++
// Time complexity = O(n^2)

#include <iostream>

using namespace std;

// declarations
void bubble_sort(int *arr, int size);
void swap(int *a, int *b);
void display(int *arr,int size);

// definitions
void swap(int *a, int *b)
{
    // swapping without using temporary variable
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}
void bubble_sort(int *arr, int size)
{
    int i,j,n;

    n = size; // size of array

    // iterate through the array
    for (i = 0; i < n-1; i++)
    {
        for(j = 0; j < n-1-i; j++)
        {
            if (arr[j] > arr[j+1])
            {
                swap(&arr[j+1], &arr[j]);
            }
        }
    }
}

void display(int *arr, int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main()
{
    int arr[7] = {55, 10, 12, 89, 51, 20, 11};
    int size = sizeof(arr)/sizeof(int);
    cout << "Before sorting" << endl;
    display(&arr[0], size);
    bubble_sort(&arr[0], size);
    cout << "Afer sorting" << endl;
    display(&arr[0], size);

    return 0;
}
